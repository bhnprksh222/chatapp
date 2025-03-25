from typing import Dict
from uuid import UUID

from fastapi import WebSocket, WebSocketDisconnect
from logger import logger
from models.message import Message
from schemas.message import MessageSchema
from utils.auth import get_user_from_token

# Keep track of connected clients
active_connections: Dict[UUID, WebSocket] = {}


async def chat_endpoint(websocket: WebSocket, token: str):
    user = await get_user_from_token(token)
    if not user:
        await websocket.close()
        return

    await websocket.accept()
    active_connections[user.id] = websocket
    logger.info(f"User {user.username} connected via WebSocket")

    try:
        while True:
            data = await websocket.receive_json()
            message_data = MessageSchema(**data)

            # Save to database
            await Message.create(
                sender_id=user.id,
                receiver_id=message_data.receiver_id,
                content=message_data.content,
            )

            # Forward to the recipient if online
            receiver_ws = active_connections.get(UUID(message_data.receiver_id))
            if receiver_ws:
                await receiver_ws.send_json(
                    {"from": str(user.id), "content": message_data.content}
                )

    except WebSocketDisconnect:
        active_connections.pop(user.id, None)
        logger.info(f"User {user.username} disconnected from WebSocket")

    except Exception as e:
        logger.error(f"WebSocket Error: {e}")
        await websocket.close()
