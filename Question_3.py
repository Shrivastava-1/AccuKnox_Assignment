# Ques: By default do Django signals run in the same database transaction as the caller?
# Ans: Yes, by default Django signals run in the same database transaction as the caller — but there are important nuances depending on when the signal is triggered and how you're using transactions.

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Signal Triggered: {instance.username}")
        print(f"Users: {User.objects.count()}")

def test_signal_with_transaction():
    try:
        with transaction.atomic():
            User.objects.create(username="signaltest")
            print("User created inside atomic block")
            print(f"User count inside transaction block: {User.objects.count()}")
            raise Exception("Simulating rollback")
    except Exception as e:
        print(f"Exception caught: {e}")
    final_count = User.objects.filter(username="signaltest").count()
    print(f"Final user count in DB after rollback: {final_count}")

test_signal_with_transaction()
