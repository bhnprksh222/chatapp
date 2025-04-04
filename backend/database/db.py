# from config import current_config

from fastapi import HTTPException
from logger import logger
from tortoise import Tortoise

# DATABASE_URL = current_config.DATABASE_URL
DATABASE_URL = "postgres://postgres:postgres@db:5432/postgres"


async def init_db():
    try:
        await Tortoise.init(
            db_url=DATABASE_URL,
            modules={
                "models": [
                    "models.user",
                    "models.message",
                    "models.friend_request",
                    "models.notification",
                ]
            },
        )
        await Tortoise.generate_schemas()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization error: {e}")
        raise HTTPException(status_code=500, detail=f"Database init error: {e}")


async def close_db():
    try:
        await Tortoise.close_connections()
        logger.info("Database connections closed")
    except Exception as e:
        logger.error(f"Database closing error: {e}")
        raise HTTPException(status_code=500, detail=f"Database close error: {e}")
