import uuid

from fastapi import APIRouter, HTTPException
from logger import logger
from models.users import User
from pydantic import BaseModel, EmailStr
from tortoise.transactions import in_transaction
from werkzeug.security import check_password_hash, generate_password_hash

router = APIRouter()


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    firstname: str
    lastname: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class ResetPasswordRequest(BaseModel):
    email: EmailStr
    new_password: str


@router.post("/register")
async def register(data: RegisterRequest):
    try:
        existing_user = await User.filter(username=data.username).first()
        if existing_user:
            logger.warning(f"User already exists: {existing_user.username}")
            raise HTTPException(status_code=409, detail="User already exists!")

        logger.info(f"New User Registration attempt: {data.username}")
        hashed_password = generate_password_hash(data.password, method="pbkdf2:sha256")

        async with in_transaction():
            user = await User.create(
                id=uuid.uuid4(),
                username=data.username,
                email=data.email,
                password_hash=hashed_password,
                firstname=data.firstname,
                lastname=data.lastname,
            )
        logger.info(f"User registered successfully: {user.username}")
        return {"message": "User registered successfully", "username": user.username}

    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@router.post("/login")
async def login(data: LoginRequest):
    try:
        user = await User.filter(email=data.email).first()

        logger.info(f"Login Attempt: {data.email}")
        if not user or not check_password_hash(user.password_hash, data.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        logger.info(f"Login successful: {data.email}")
        return {"message": "Login Successful"}

    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@router.patch("/reset-password/{user_id}")
async def reset_password(user_id: uuid.UUID, data: ResetPasswordRequest):
    try:
        logger.info(f"Password reset attempt: {data.email}")
        user = await User.filter(id=user_id).first()

        if not user:
            logger.warning(f"User not found: {data.email}")
            raise HTTPException(status_code=404, detail="User not found")

        hashed_password = generate_password_hash(
            data.new_password, method="pbkdf2:sha256"
        )
        user.password_hash = hashed_password
        await user.save()

        logger.info(f"Password reset successful: {user.email}")
        return {"message": "Password reset successful"}
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=f"Error: {e}")
