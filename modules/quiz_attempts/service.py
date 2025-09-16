from datetime import datetime
from uuid import uuid4

from fastapi import HTTPException

from models import QuizAttempt as QuizAttemptModel


class QuizAttemptService:
    def __init__(self):
        pass

    async def create_quiz_attempt(
        self,
        db,
        user_id: str,
        attempt_data: dict
    ) -> QuizAttemptModel:
        """Save a completed quiz attempt"""
        try:
            quiz_attempt = QuizAttemptModel(
                id=str(uuid4()),
                user_id=user_id,
                certification_id=attempt_data["certification_id"],
                score=attempt_data["score"],
                total_questions=attempt_data["total_questions"],
                correct_answers=attempt_data["correct_answers"],
                points=attempt_data["points"],
                completed_at=datetime.now(),
            )

            db.add(quiz_attempt)
            await db.commit()
            await db.refresh(quiz_attempt)

            return quiz_attempt
        except Exception:
            raise HTTPException(
                status_code=500,
                detail="Failed to save quiz attempt")