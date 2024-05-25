from celery import shared_task
from channels.layers import get_channel_layer
import json
from celery.exceptions import Ignore
import asyncio


@shared_task(bind=True)
def broadcast_notification(*args, **kwargs):
    print("broadcast_notification: {}".format(kwargs))
    to_user = kwargs.get('recipient_profile_username')
    try:
        channel_layer = get_channel_layer()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(channel_layer.group_send(
            f"notification_{to_user}",
            {
                'type': 'send_notification',
                'message': {
                    'content': json.dumps(kwargs.get('content')),
                    'to_user': to_user,
                    'display_image': kwargs.get('display_image')
                }

            }))
        return 'Done'

    except:
        pass
        raise Ignore()
