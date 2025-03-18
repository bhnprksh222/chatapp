# from config import current_config
from tortoise import Tortoise

# DATABASE_URL = current_config.DATABASE_URL
DATABASE_URL = "postgres://postgres:postgres@db:5432/postgres"


async def init_db():
    await Tortoise.init(
        db_url=DATABASE_URL, modules={"models": ["models.users", "models.messages"]}
    )
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
