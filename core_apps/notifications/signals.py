from django.db.models.signals import post_save, post_delete

from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile, InAppMessage
from .tasks import broadcast_notification


@receiver(post_save, sender=InAppMessage)
def send_new_message_notification(sender, instance, created, **kwargs):
    print("inside send_new_message_notification signal")
    if created:
        broadcast_notification.delay(sender_profile_username=instance.sender_profile.username,
                                     recipient_profile_username=instance.recipient_profile.username,
                                     content=instance.content)
