# Ques2: Do Django signals run in the same thread as the caller?
# Ans: Yes, Django signals run in the same thread as the caller by default.

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time
import threading

@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    print(f"Thread name: {threading.current_thread().name}")
    if created:
        print(f"New user created: {instance.username}")
        time.sleep(5)
        print("Signal finished")

new_user = User.objects.create_user(username="newuser", password="test123")
