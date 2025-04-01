from uuid import uuid4

from tortoise import fields
from tortoise.models import Model


class FriendRequest(Model):
    id = fields.UUIDField(pk=True, default=uuid4)
    sender = fields.ForeignKeyField("models.User", related_name="sent_requests")
    receiver = fields.ForeignKeyField("models.User", related_name="received_requests")
    status = fields.CharField(max_length=20, default="pending")
    timestamp = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "friend_request"
