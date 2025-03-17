import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration with default settings."""

    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = "Content-Type"


class DevelopmentConfig(Config):
    """Configuration for Development."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


# class ProductionConfig(Config):
#     """Configuration for Production."""
#
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = os.getenv(
#         "DATABASE_URL", "postgresql://user:password@aws-db-instance/chat_db"
# )
#
#
# class TestingConfig(Config):
#     """Configuration for Testing."""
#
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"


# Select the configuration based on the environment
configurations = {
    "development": DevelopmentConfig,
    # "production": ProductionConfig,
    # "testing": TestingConfig,
}

current_config = configurations[os.getenv("FLASK_ENV", "development")]
