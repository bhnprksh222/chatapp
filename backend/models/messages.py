import uuid

from tortoise import fields
from tortoise.models import Model


class Message(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    sender = fields.ForeignKeyField("models.User", related_name="sent_messages")
    receiver = fields.ForeignKeyField("models.User", related_name="received_messages")
    message = fields.TextField()
    timestamp = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "messages"
