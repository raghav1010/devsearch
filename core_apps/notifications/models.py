import uuid

from django.db import models

from core_apps.users.models import Profile


# Create your models here.

class InAppMessage(models.Model):
    sender_profile = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE, related_name="sender_profile")
    recipient_profile = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE, related_name="recipient_profile")
    content = models.CharField(max_length=512)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    dt_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-dt_created']

    def __str__(self):
        return str(self.id)




