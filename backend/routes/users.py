from fastapi import APIRouter, HTTPException
from logger import logger
from models.users import User
from pydantic import BaseModel

router = APIRouter()


class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    firstname: str
    lastname: str


@router.get("/all", response_model=list[UserResponse])
async def get_all_users():
    try:
        users_output = await User.all()
        users_list = [
            {
                "id": str(user.id),
                "username": user.username,
                "email": user.email,
                "firstname": user.firstname,
                "lastname": user.lastname,
            }
            for user in users_output
        ]
        logger.info(f"Users: {users_list}")
        return users_list
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {e}")
