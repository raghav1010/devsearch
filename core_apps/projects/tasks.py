import logging

from celery import shared_task
from channels.layers import get_channel_layer
import json
from celery.exceptions import Ignore
import asyncio

from core_apps.notifications.models import InAppMessage
from core_apps.users.models import Profile


@shared_task(bind=True)
def create_in_app_message(*args, **kwargs):
    print("create_in_app_message: {}".format(kwargs))
    try:
        sender_profile_id = kwargs.get('sender_profile_id')
        receiver_profile_id = kwargs.get('receiver_profile_id')
        sender_profile = Profile.objects.get(id=sender_profile_id)
        receiver_profile = Profile.objects.get(id=receiver_profile_id)

        if not (sender_profile and receiver_profile):
            return

        record = InAppMessage(sender_profile=sender_profile, recipient_profile=receiver_profile,
                              content=kwargs.get('content'))
        record.save()
        return 'Done'

    except Exception as exc:
        logging.info("Something went wrong: {}".format(exc))
        raise Ignore()
