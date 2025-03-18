import uuid

from database.db import db
from flask import Blueprint, jsonify, request
from logger import logger
from models.users import User
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()

        if not data:
            logger.warning("Registration failed due to invalid input", data)
            return jsonify({"error": "Invalid input"}), 400
        logger.info(f"New Registration Attempt: {data['email']}")

        is_user_exists = (
            db.session.query(User.id).filter_by(username=data["username"]).first()
            is not None
        )

        logger.warning(f"User already exists: {data['username']}")
        if is_user_exists:
            return {
                "message": "User already exists!",
                "data": None,
                "returnCode": 409,
            }

        hashed_password = generate_password_hash(
            data["password"], method="pbkdf2:sha256"
        )

        user = User(
            id=uuid.uuid4(),
            username=data["username"],
            email=data["email"],
            password_hash=hashed_password,
            firstname=data["firstname"],
            lastname=data["lastname"],
        )

        db.session.add(user)
        db.session.commit()

        logger.info(f"User Registered successfully: {data['email']}")
        return {
            "message": "Successfully user registered.",
            "data": data["username"],
            "returnCode": 201,
        }
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"message": f"Error: {e}", "data": None, "returnCode": 500}


@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400
        user = User.query.filter_by(email=data["email"]).first()

        if user and check_password_hash(user.password_hash, data["password"]):
            return {"message": "Login Successful", "data": None, "returnCode": 200}
        else:
            return {"message": "Invalid credentials", "data": None, "returnCode": 401}
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"message": f"Error: {e}", "data": None, "returnCode": 500}


@auth_bp.route("/reset-password/<uuid:id>", methods=["PATCH"])
def reset_password(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400
        user = User.query.filter_by(email=data["email"]).first()

        logger.info(f"Resetting Password Attempt: {data['email']}")
        hashed_password = generate_password_hash(
            data["new_password"], method="pbkdf2:sha256"
        )
        user.password_hash = hashed_password
        db.session.commit()
        return {
            "message": "Password reset Successful.",
            "data": data["email"],
            "returnCode": 201,
        }

    except Exception as e:
        logger.error(f"Error: {e}")
        return {"message": f"Error: {e}", "data": None, "returnCode": 500}
