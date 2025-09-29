from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserActivityItem(BaseModel):
    """Single activity item for a user"""
    id: str
    type: str  # "quiz_attempt", "progress_update", etc.
    title: str
    description: Optional[str] = None
    score: Optional[int] = None
    certification_name: Optional[str] = None
    certification_id: Optional[int] = None
    points: Optional[int] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserActivity(BaseModel):
    """User activity response model"""
    activities: List[UserActivityItem]
    total_count: int
    
    class Config:
        from_attributes = True


class UserProfile(BaseModel):
    """User profile model"""
    id: str
    name: Optional[str] = None
    email: str
    email_verified: Optional[datetime] = None
    image: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True