from django.db.models.signals import post_save, post_delete

from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile, InAppMessage
from .tasks import broadcast_notification


@receiver(post_save, sender=InAppMessage)
def send_new_message_notification(sender, instance, created, **kwargs):
    print("inside send_new_message_notification signal")
    if created:
        broadcast_notification.delay(sender_profile_id=instance.sender_profile.id,
                                     srecipient_profile_id=instance.recipient_profile.id,
                                     content=instance.content)
