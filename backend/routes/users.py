from fastapi import APIRouter, Depends, HTTPException
from logger import logger
from models.user import User
from schemas.user import UserOut, UserSearchResult
from utils.auth import get_current_user

router = APIRouter()


@router.get("/all", response_model=list[UserSearchResult])
async def get_all_users():
    try:
        users = await User.all()
        return [UserSearchResult.from_orm(user) for user in users]
    except Exception as e:
        logger.error(f"Fetch users failed: {e}")
        raise HTTPException(status_code=500, detail="Error fetching users")


@router.get("/me", response_model=UserOut)
async def get_me(current_user: User = Depends(get_current_user)):
    return await UserOut.from_tortoise_orm(current_user)
