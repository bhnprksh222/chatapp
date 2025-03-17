from flask import Blueprint
from logger import logger
from models.users import User

users_bp = Blueprint("users", __name__)


@users_bp.route("/all", methods=["GET"])
def get_all_users():
    try:
        users_output = User.query.all()
        users_list = [
            {"id": user.username, "email": user.email} for user in users_output
        ]
        return {
            "message": "Successfully fetched all users.",
            "data": users_list,
            "returnCode": 200,
        }
    except Exception as e:
        logger.error(f"Error: {e}")
        return {"message": f"Error: {e}", "data": None, "returnCode": 500}
