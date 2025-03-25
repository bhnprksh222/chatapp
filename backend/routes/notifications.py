from fastapi import APIRouter, Depends, HTTPException
from logger import logger
from models.notification import Notification
from models.user import User
from utils.auth import get_current_user

router = APIRouter()


@router.get("/")
async def get_notifications(current_user: User = Depends(get_current_user)):
    try:
        notifications = await Notification.filter(user_id=current_user.id).order_by(
            "-timestamp"
        )
        return [
            {
                "content": n.content,
                "type": n.type,
                "is_read": n.is_read,
                "timestamp": n.timestamp,
            }
            for n in notifications
        ]
    except Exception as e:
        logger.error(f"Notification fetch failed: {e}")
        raise HTTPException(status_code=500, detail="Unable to fetch notifications")


@router.post("/read-all")
async def mark_all_as_read(current_user: User = Depends(get_current_user)):
    try:
        await Notification.filter(user_id=current_user.id, is_read=False).update(
            is_read=True
        )
        return {"message": "All notifications marked as read"}
    except Exception as e:
        logger.error(f"Marking notifications failed: {e}")
        raise HTTPException(status_code=500, detail="Unable to update notifications")
