import uuid

from fastapi import APIRouter, WebSocket
from logger import logger
from models.messages import Message
from models.users import User

router = APIRouter()

active_connections = []


@router.websocket("/chat/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: uuid.UUID):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            sender = await User.filter(id=data["sender_id"]).first()
            receiver = await User.filter(id=data["receiver_id"]).first()

            if not sender or not receiver:
                logger.warning("Invalud sender or receiver ID")
                await websocket.send_text("Invalid sender or receiver ID")
                continue

            message = await Message.create(
                sender=sender, receiver=receiver, message=data["message"]
            )

            for connection in active_connections:
                await connection.send_json(message.to_dict())
    except Exception:
        active_connections.remove(websocket)
