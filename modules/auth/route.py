from fastapi import APIRouter, Query

from .controller import AuthController
from .model import GoogleAuthURL


router = APIRouter()
auth_controller = AuthController()


@router.get("/me")
async def get_current_user(token: str = Query(...)):
    """Get current user info from session"""
    return await auth_controller.get_current_user(token)


@router.post("/logout")
async def logout(token: str = Query(...)):
    """Logout user by removing session"""
    return await auth_controller.logout(token)


@router.get("/google", response_model=GoogleAuthURL)
async def get_google_auth_url():
    """Get Google OAuth2 authorization URL"""
    return await auth_controller.get_google_auth_url()


@router.get("/callback/google")
async def google_callback(code: str = None, error: str = None):
    """Handle Google OAuth2 callback"""
    return await auth_controller.google_callback(code, error)


@router.post("/logout/simple")
async def logout_simple():
    """Logout user (invalidate token)"""
    return await auth_controller.logout_simple()