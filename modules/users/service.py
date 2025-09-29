from typing import Optional
from sqlalchemy import select
from sqlalchemy import desc as sql_desc
from sqlalchemy.ext.asyncio import AsyncSession
from models import User, QuizAttempt, UserProgress, Certification
from .model import UserActivityItem, UserActivity


class UserService:
    
    @staticmethod
    async def get_user_profile(
        db: AsyncSession, user_id: str
    ) -> Optional[User]:
        """Get user profile by ID"""
        result = await db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_user_activity(
        db: AsyncSession,
        user_id: str,
        limit: int = 10
    ) -> UserActivity:
        """Get user's recent activity (quiz attempts and progress updates)"""
        
        # Get quiz attempts
        quiz_result = await db.execute(
            select(QuizAttempt, Certification.name.label('cert_name'))
            .join(Certification,
                  QuizAttempt.certification_id == Certification.id)
            .where(QuizAttempt.user_id == user_id)
            .order_by(sql_desc(QuizAttempt.created_at))
            .limit(limit)
        )
        quiz_attempts = quiz_result.fetchall()

        # Get progress updates
        progress_result = await db.execute(
            select(UserProgress, Certification.name.label('cert_name'))
            .join(Certification,
                  UserProgress.certification_id == Certification.id)
            .where(UserProgress.user_id == user_id)
            .order_by(sql_desc(UserProgress.updated_at))
            .limit(limit)
        )
        progress_updates = progress_result.fetchall()
        
        # Combine and sort activities
        activities = []
        
        # Add quiz attempts
        for attempt, cert_name in quiz_attempts:
            desc = (f"Scored {attempt.score}% "
                    f"({attempt.correct_answers}/{attempt.total_questions})")
            activities.append(UserActivityItem(
                id=attempt.id,
                type="quiz_attempt",
                title=f"Quiz Attempt: {cert_name}",
                description=desc,
                score=attempt.score,
                certification_name=cert_name,
                certification_id=attempt.certification_id,
                points=attempt.points,
                created_at=attempt.created_at
            ))

        # Add progress updates
        for progress, cert_name in progress_updates:
            prog_id = (f"progress_{progress.user_id}_"
                       f"{progress.certification_id}")
            desc = f"Progress: {progress.progress_percentage}% completed"
            activities.append(UserActivityItem(
                id=prog_id,
                type="progress_update",
                title=f"Progress Update: {cert_name}",
                description=desc,
                certification_name=cert_name,
                certification_id=progress.certification_id,
                created_at=progress.updated_at
            ))
        
        # Sort by date (most recent first) and limit
        activities.sort(key=lambda x: x.created_at, reverse=True)
        activities = activities[:limit]
        
        # Get total count for pagination
        total_quiz_count_result = await db.execute(
            select(QuizAttempt).where(QuizAttempt.user_id == user_id)
        )
        total_quiz_count = len(total_quiz_count_result.fetchall())
        
        total_progress_count_result = await db.execute(
            select(UserProgress).where(UserProgress.user_id == user_id)
        )
        total_progress_count = len(total_progress_count_result.fetchall())
        
        total_count = total_quiz_count + total_progress_count
        
        return UserActivity(
            activities=activities,
            total_count=total_count
        )