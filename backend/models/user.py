from uuid import uuid4

from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.UUIDField(pk=True, default=uuid4)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password_hash = fields.CharField(max_length=200)
    firstname = fields.CharField(max_length=100)
    lastname = fields.CharField(max_length=100)
    bio = fields.TextField(null=True)
    profile_picture = fields.CharField(max_length=255, null=True)
    location = fields.CharField(max_length=255, null=True)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    friends: fields.ManyToManyRelation["User"] = fields.ManyToManyField(
        "models.User", related_name="friend_of", through="friend"
    )

    class Meta:
        table = "User"
