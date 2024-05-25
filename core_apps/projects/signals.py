from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver

from .models import Review
from .tasks import create_in_app_message


@receiver(post_save, sender=Review)
def create_new_in_app_message(sender, instance, created, **kwargs):
    print("inside create_new_in_app_message signal, project url: {}".format(instance.project.get_absolute_url()))
    if created:
        create_in_app_message.delay(sender_profile_id=instance.owner.id,
                                    receiver_profile_id=instance.project.owner.id,
                                    content='{} reviewed your project'.format(instance.owner.username))
