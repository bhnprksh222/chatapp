import os

from config import current_config
from database.db import db, migrate
from extensions import socketio
from flask import Flask
from flask_cors import CORS
from logger import logger
from routes.auth import auth_bp
from routes.chat import chat_bp
from routes.users import users_bp

app = Flask(__name__)
app.config.from_object(current_config)  # Load config

CORS(app)
socketio.init_app(app)  # Initialize socket.io here

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(chat_bp, url_prefix="/chat")
app.register_blueprint(users_bp, url_prefix="/users")

with app.app_context():
    db.create_all()

logger.info("Flask App has started successfully!")

debug_mode = os.getenv("FLASK_DEBUG", "0") == "1"
if __name__ == "__main__":
    logger.info("FLASK APP IS RUNNING")
    socketio.run(app, debug=debug_mode, host="0.0.0.0", use_reloader=True)
