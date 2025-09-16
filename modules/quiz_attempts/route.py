from fastapi import APIRouter, Depends

from auth import UserSession, get_current_user
from database import get_db
from .controller import QuizAttemptController
from .model import QuizAttemptCreate, QuizAttempt

router = APIRouter()
quiz_attempt_controller = QuizAttemptController()


@router.post("/", response_model=QuizAttempt)
async def create_quiz_attempt(
    attempt_data: QuizAttemptCreate,
    current_user: UserSession = Depends(get_current_user),
    db=Depends(get_db),
):
    """Save a completed quiz attempt"""
    return await quiz_attempt_controller.create_quiz_attempt(
        attempt_data.dict(), current_user, db
    )