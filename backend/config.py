import os

from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Base configuration with default settings."""

    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    CORS_HEADERS: str = "Content-Type"


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG: bool = True
    DATABASE_URL: str = os.getenv("DATABASE_URL")


# Select the configuration based on FASTAPI_ENV
configurations = {
    "development": DevelopmentConfig,
}

current_config = configurations[os.getenv("FASTAPI_ENV", "development")]
