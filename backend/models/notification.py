from uuid import uuid4

from tortoise import fields
from tortoise.models import Model


class Notification(Model):
    id = fields.UUIDField(pk=True, default=uuid4)
    user = fields.ForeignKeyField("models.User", related_name="notifications")
    content = fields.TextField()
    type = fields.CharField(max_length=50)
    is_read = fields.BooleanField(default=False)
    timestamp = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "notification"
