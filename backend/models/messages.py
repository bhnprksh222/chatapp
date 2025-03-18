import uuid

from database.db import db
from logger import logger
from sqlalchemy.dialects.postgresql import UUID


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    sender_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)
    receiver_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False
    )
    message = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        try:
            return {
                "id": self.id,
                "sender_id": self.sender_id,
                "receiver_id": self.receiver_id,
                "message": self.message,
                "timestamp": self.timestamp,
            }
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": f"Error: {e}", "data": None, "returnCode": 500}
