from .auth import router as auth_router
from .friends import router as friends_router
from .notifications import router as notifications_router
from .users import router as users_router

__all__ = ["auth_router", "users_router", "friends_router", "notifications_router"]
