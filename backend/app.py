import os

from database.db import close_db, init_db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logger import logger
from routes.auth import router as auth_router
from routes.chat import router as chat_router
from routes.users import router as users_router

# FastAPI App
app = FastAPI(
    title="ChatApp",
    description="A real-time chat application using FastAPI",
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


# Database Initialization
@app.on_event("startup")
async def startup():
    await init_db()
    logger.info("Database initialized successfully.")


@app.on_event("shutdown")
async def shutdown():
    await close_db()
    logger.info("Database closed.")


# Register Routes (Equivalent to Flask Blueprints)
app.include_router(auth_router, prefix="/auth")
app.include_router(chat_router, prefix="/chat")
app.include_router(users_router, prefix="/users")

# Run FastAPI Server
if __name__ == "__main__":
    import uvicorn

    debug_mode = os.getenv("FASTAPI_DEBUG", "0") == "1"
    logger.info("FASTAPI APP IS RUNNING")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=debug_mode)
