# Ques1: By default are Django signals executed synchronously or asynchronously?
# Ans: Yes, by default, Django signals are executed synchronously.

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):
    if created:
        print(f"Signal received: {instance.username}")
        print("Processing")
        time.sleep(5)
        print("Signal processed.")

user = User.objects.create(username="testuser_signal")
