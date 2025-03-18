import uuid

from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4, unique=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password_hash = fields.CharField(max_length=200)
    created_at = fields.DatetimeField(auto_now_add=True)
    firstname = fields.CharField(max_length=100)
    lastname = fields.CharField(max_length=100)

    class Meta:
        table = "users"
