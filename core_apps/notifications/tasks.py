from celery import shared_task
from channels.layers import get_channel_layer
import json
from celery.exceptions import Ignore
import asyncio


@shared_task(bind=True)
def broadcast_notification(*args, **kwargs):
    print("broadcast_notification: {}".format(kwargs))
    try:
        channel_layer = get_channel_layer()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(channel_layer.group_send(
            "notification_broadcast",
            {
                'type': 'send_notification',
                'message': json.dumps(kwargs.get('content')),
            }))
        return 'Done'

    except:
        pass
        raise Ignore()
