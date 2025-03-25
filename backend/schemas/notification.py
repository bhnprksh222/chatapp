from datetime import datetime

from pydantic import BaseModel


class NotificationOut(BaseModel):
    content: str
    type: str
    is_read: bool
    timestamp: datetime
