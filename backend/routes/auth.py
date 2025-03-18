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
    existing_user = await User.filter(username=data.username).first()
    if existing_user:
        raise HTTPException(status_code=409, detail="User already exists!")

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

    return {"message": "User registered successfully", "username": user.username}


@router.post("/login")
async def login(data: LoginRequest):
    user = await User.filter(email=data.email).first()

    if not user or not check_password_hash(user.password_hash, data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login Successful"}


@router.patch("/reset-password/{user_id}")
async def reset_password(user_id: uuid.UUID, data: ResetPasswordRequest):
    user = await User.filter(email=data.email).first()
    logger.info(f"USER: {user}")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    hashed_password = generate_password_hash(data.new_password, method="pbkdf2:sha256")
    user.password_hash = hashed_password
    await user.save()

    return {"message": "Password reset successful"}
