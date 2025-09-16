# Auth utilities for backwards compatibility
# This provides centralized auth functions that other modules expect

from typing import Optional
from pydantic import BaseModel
from fastapi import HTTPException, Query

from sessions import get_user_session


class User(BaseModel):
    """User model for session data"""
    id: str
    email: str
    name: Optional[str] = None
    image: Optional[str] = None


class UserSession(BaseModel):
    """User session data structure"""
    user: User
    
    @classmethod
    def from_session_data(cls, session_data: dict) -> "UserSession":
        """Create UserSession from raw session data"""
        return cls(
            user=User(
                id=session_data.get("id", ""),
                email=session_data.get("email", ""),
                name=session_data.get("name"),
                image=session_data.get("image")
            )
        )


async def get_current_user(token: str = Query(...)) -> UserSession:
    """
    Get current authenticated user from session token.
    Raises HTTPException if user is not authenticated.
    """
    user_data = get_user_session(token)
    if not user_data:
        raise HTTPException(
            status_code=401,
            detail="Invalid session token"
        )
    
    return UserSession.from_session_data(user_data)


async def get_optional_user(
    token: Optional[str] = Query(None)
) -> Optional[UserSession]:
    """
    Get current user from session token if provided and valid.
    Returns None if no token provided or token is invalid.
    Does not raise exceptions for invalid/missing auth.
    """
    if not token:
        return None
    
    try:
        user_data = get_user_session(token)
        if not user_data:
            return None
        
        return UserSession.from_session_data(user_data)
    except Exception:
        # If anything goes wrong, return None (don't raise)
        return None