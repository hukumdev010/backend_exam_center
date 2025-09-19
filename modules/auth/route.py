from fastapi import APIRouter, Header, HTTPException

from .controller import AuthController
from .model import GoogleAuthURL


router = APIRouter()
auth_controller = AuthController()


@router.get("/me")
async def get_current_user(authorization: str = Header(None)):
    """Get current user info from session"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header required")
    
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header format")
    
    token = authorization.replace("Bearer ", "", 1)
    return await auth_controller.get_current_user(token)


@router.post("/logout")
async def logout(authorization: str = Header(None)):
    """Logout user by removing session"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header required")
    
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header format")
    
    token = authorization.replace("Bearer ", "", 1)
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