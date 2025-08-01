# Question_1: Are Django signals executed synchronously or asynchronously?
# Answer: Django signals are executed synchronously by default.
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):
    if created:
        print(f"Signal received for user: {instance.username}")
        print("Processing... Please wait 5 seconds.")
        time.sleep(5)
        print("Signal processed.")

user = User.objects.create(username="testuser_signal")