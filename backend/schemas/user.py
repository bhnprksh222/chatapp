from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    firstname: str
    lastname: str
    password: str


class UserOut(BaseModel):
    id: str
    username: str
    email: EmailStr
    firstname: str
    lastname: str
    is_active: bool
    created_at: datetime


class UserSearchResult(BaseModel):
    id: str
    username: str
    firstname: str
    lastname: str
    email: EmailStr
