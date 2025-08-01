# Question_3: Do Django signals run in the same database transaction as the caller?
# Answer: Yes, by default, Django signals run in the same database transaction as the caller if the signal is connected normally with async or thread-based triggers.

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        print(f"Signal Triggered for: {instance.username}")
        print(f"Users : {User.objects.count()}")

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

# Run the test function
test_signal_with_transaction()