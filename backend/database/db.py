# from config import current_config
from fastapi import HTTPException
from logger import logger
from tortoise import Tortoise

# DATABASE_URL = current_config.DATABASE_URL
DATABASE_URL = "postgres://postgres:postgres@db:5432/postgres"


async def init_db():
    try:
        await Tortoise.init(
            db_url=DATABASE_URL, modules={"models": ["models.users", "models.messages"]}
        )
        await Tortoise.generate_schemas()
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {e}")


async def close_db():
    try:
        await Tortoise.close_connections()

    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {e}")
