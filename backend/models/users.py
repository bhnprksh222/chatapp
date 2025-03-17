from database.db import db
from logger import logger


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        try:
            return {"id": self.id, "username": self.username, "email": self.email}
        except Exception as e:
            logger.error(f"Error: {e}")
            return {"message": f"Error: {e}", "data": None, "returnCode": 500}
