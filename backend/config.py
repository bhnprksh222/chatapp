import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration with default settings."""

    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    CORS_HEADERS = "Content-Type"


class DevelopmentConfig(Config):
    """Configuration for Development."""

    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_URL")


# Select the configuration based on the environment
configurations = {
    "development": DevelopmentConfig,
}

current_config = configurations[os.getenv("FASTAPI_ENV", "development")]
