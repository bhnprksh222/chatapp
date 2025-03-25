from fastapi import APIRouter, Depends, HTTPException
from logger import logger
from models.friend_request import FriendRequest
from models.user import User
from schemas.friend_request import FriendRequestSchema
from utils.auth import get_current_user

router = APIRouter()


@router.post("/request")
async def send_friend_request(
    payload: FriendRequestSchema, current_user: User = Depends(get_current_user)
):
    if str(current_user.id) != payload.sender_id:
        raise HTTPException(status_code=403, detail="Unauthorized sender")

    exists = await FriendRequest.get_or_none(
        sender_id=payload.sender_id, receiver_id=payload.receiver_id, status="pending"
    )
    if exists:
        raise HTTPException(status_code=400, detail="Friend request already sent")

    await FriendRequest.create(
        sender_id=payload.sender_id, receiver_id=payload.receiver_id
    )
    logger.info(
        f"Friend request sent from {payload.sender_id} to {payload.receiver_id}"
    )
    return {"message": "Friend request sent"}


@router.post("/approve/{request_id}")
async def approve_friend_request(
    request_id: str, current_user: User = Depends(get_current_user)
):
    request = await FriendRequest.get_or_none(id=request_id, status="pending")
    if not request or request.receiver_id != current_user.id:
        raise HTTPException(status_code=403, detail="Invalid or unauthorized request")

    request.status = "accepted"
    await request.save()

    sender = await User.get(id=request.sender_id)
    await current_user.friends.add(sender)
    await sender.friends.add(current_user)

    logger.info(f"Friend request {request_id} approved")
    return {"message": "Friend request accepted"}


@router.get("/list")
async def get_friends(current_user: User = Depends(get_current_user)):
    friends = await current_user.friends.all()
    return [
        {"id": str(friend.id), "username": friend.username, "email": friend.email}
        for friend in friends
    ]
