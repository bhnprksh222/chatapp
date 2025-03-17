from database.db import db
from extensions import socketio
from flask import Blueprint, jsonify, request
from flask_socketio import emit
from logger import logger
from models.messages import Message

chat_bp = Blueprint("chat", __name__)


@socketio.on("message")
def handle_message(data):
    try:
        message = Message(
            sender_id=data["sender_id"],
            receiver_id=data["receiver_id"],
            message=data["message"],
        )
        db.session.add(message)
        db.session.commit()

        emit("message", message.to_dict(), broadcast=True)
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"message": f"Error: {e}", "data": None, "returnCode": 500}


@chat_bp.route("/messages/<int:user_id>", methods=["GET"])
def get_messages(user_id):
    try:
        messages = Message.query.filter(
            (Message.sender_id == user_id) | (Message.receiver_id == user_id)
        ).all()
        return jsonify([msg.to_dict() for msg in messages])
        return {
            "message": "Successfully fetched messages",
            "data": [msg.to_dict() for msg in messages],
            "returnCode": 200,
        }
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"message": f"Error: {e}", "data": None, "returnCode": 500}


@chat_bp.route("/send", methods=["POST"])
def send_message():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400

        message = data.get("message")
        socketio.emit("message", {"message": message})
        return {"message": "Message sent", "data": message, "returnCode": 200}

    except Exception as e:
        logger.error(f"Error: {e}")
        return {"message": f"Error: {e}", "data": None, "returnCode": 500}
