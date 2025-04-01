from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, Request

router = APIRouter
oauth = OAuth()

oauth.Register(
    name="google",
    client_id="",
    client_secret="",
    server_metadata_url="",
    client_kwargs={"scope": ""},
)


@router.get("/login/google")
async def login_google(request: Request):
    redirect_uri = "http://localhost:8000/auth/callback/google"
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/callback/google")
async def callback_google(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user_info = await oauth.google.parse_id_token(request, token)
    return {"user": user_info}
