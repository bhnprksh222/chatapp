from pydantic import BaseModel


class FriendRequestSchema(BaseModel):
    sender_id: str
    receiver_id: str
