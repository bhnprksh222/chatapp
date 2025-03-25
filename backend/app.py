import os

from database.db import close_db, init_db
from fastapi import FastAPI, HTTPException, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from logger import logger
from routes.auth import router as auth_router
from routes.friends import router as friends_router
from routes.notifications import router as notifications_router
from routes.users import router as users_router
from websockets.chat import chat_endpoint

# FastAPI App
app = FastAPI(
    title="ChatApp",
    description="A real-time chat application",
    version="1.0.0",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change for production security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket, token: str):
    await chat_endpoint(websocket, token)


# Database Initialization
@app.on_event("startup")
async def startup():
    try:
        await init_db()
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@app.on_event("shutdown")
async def shutdown():
    try:
        await close_db()
        logger.info("Database closed.")
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {e}")


# Register Routes (Equivalent to Flask Blueprints)
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(friends_router, prefix="/friends", tags=["Friends"])
app.include_router(
    notifications_router, prefix="/notifications", tags=["Notifications"]
)

# Run FastAPI Server
if __name__ == "__main__":
    import uvicorn

    debug_mode = os.getenv("FASTAPI_DEBUG", "0") == "1"
    logger.info("FASTAPI APP IS RUNNING")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=debug_mode)
