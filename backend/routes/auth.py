from fastapi import APIRouter

router = APIRouter()

"""
@router.post("/signup", response_model=UserOut)
async def signup(user: UserCreate):
    try:
        existing_user = await User.get_or_none(email=user.email)
        if existing_user:
            raise HTTPException(status_code=409, detail="User already exists")
        user_obj = await User.create(
            username=user.username,
            email=user.email,
            firstname=user.firstname,
            lastname=user.lastname,
            password_hash=get_password_hash(user.password),
        )
        return await UserOut.from_tortoise_orm(user_obj)
    except Exception as e:
        logger.error(f"Signup error: {e}")
        raise HTTPException(status_code=500, detail="Signup failed")


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_or_none(email=form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}


class GoogleUserSchema(BaseModel):
    name: str
    email: EmailStr
    image: str


@router.post("/google")
async def google_auth(user: GoogleUserSchema):
    existing_user = await User.get_or_none(email=user.email)
    if existing_user:
        return {"message": "User already exists."}
    await User.create(
        username=user.email.split("@")[0],
        email=user.email,
        firstname=user.name.split()[0],
        lastname=user.name.split()[-1],
        profile_picture=user.image,
    )
    return {"message": "User created or exists."}
"""
