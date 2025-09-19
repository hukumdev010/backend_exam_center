from typing import List, Optional
from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from .service import TeacherService
from .model import (
    TeacherProfile,
    TeacherProfileCreate,
    TeacherProfileUpdate,
    AdminApprovalRequest,
    TeacherWithQualifications,
    TeacherQualification,
    TeacherStatusEnum
)


class TeacherController:

    @staticmethod
    async def apply_as_teacher(
        profile_data: TeacherProfileCreate,
        user_id: str,
        db: AsyncSession = Depends(get_db)
    ) -> TeacherProfile:
        """
        Apply to become a teacher
        """
        try:
            teacher_profile = await TeacherService.create_teacher_profile(
                db, user_id, profile_data
            )
            return teacher_profile
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    async def update_teacher_profile(
        profile_data: TeacherProfileUpdate,
        user_id: str,
        db: AsyncSession = Depends(get_db)
    ) -> TeacherProfile:
        """
        Update teacher profile
        """
        teacher_profile = await TeacherService.update_teacher_profile(
            db, user_id, profile_data
        )
        if not teacher_profile:
            raise HTTPException(
                status_code=404,
                detail="Teacher profile not found"
            )
        return teacher_profile

    @staticmethod
    async def get_my_teacher_profile(
        user_id: str,
        db: AsyncSession = Depends(get_db)
    ) -> TeacherWithQualifications:
        """
        Get current user's teacher profile with qualifications
        """
        teacher_profile = await TeacherService.get_teacher_with_qualifications(
            db, user_id
        )
        if not teacher_profile:
            raise HTTPException(
                status_code=404,
                detail="Teacher profile not found"
            )

        # Get qualifications
        qualifications = await TeacherService.get_user_qualifications(
            db, user_id
        )

        return TeacherWithQualifications(
            **teacher_profile.__dict__,
            qualifications=qualifications
        )

    @staticmethod
    async def check_eligibility(
        user_id: str,
        db: AsyncSession = Depends(get_db)
    ) -> dict:
        """
        Check teaching eligibility
        """
        return await TeacherService.check_teaching_eligibility(db, user_id)

    @staticmethod
    async def get_my_qualifications(
        user_id: str,
        db: AsyncSession = Depends(get_db)
    ) -> List[TeacherQualification]:
        """
        Get current user's teaching qualifications
        """
        return await TeacherService.get_user_qualifications(db, user_id)

    @staticmethod
    async def process_quiz_result(
        quiz_attempt_id: str,
        user_id: str,
        db: AsyncSession = Depends(get_db)
    ) -> Optional[TeacherQualification]:
        """
        Process quiz result to create qualification if eligible
        (90%+)
        """
        qualification = await TeacherService.create_quiz_qualification(
            db,
            user_id,
            quiz_attempt_id
        )
        return qualification

    @staticmethod
    async def admin_approve_teacher(
        teacher_id: int,
        approval_data: AdminApprovalRequest,
        admin_user_id: str,
        db: AsyncSession = Depends(get_db)
    ) -> TeacherProfile:
        """
        Admin approval/rejection of teacher application
        """
        teacher_profile = await TeacherService.admin_approve_teacher(
            db, teacher_id, admin_user_id, approval_data
        )
        if not teacher_profile:
            raise HTTPException(
                status_code=404,
                detail="Teacher profile not found"
            )
        return teacher_profile

    @staticmethod
    async def list_teachers(
        status: Optional[TeacherStatusEnum] = None,
        is_available: Optional[bool] = None,
        category_id: Optional[int] = None,
        skip: int = 0,
        limit: int = 100,
        db: AsyncSession = Depends(get_db)
    ) -> List[TeacherProfile]:
        """
        List teachers with filters
        """
        return await TeacherService.list_teachers(
            db, status, is_available, category_id, skip, limit
        )

    @staticmethod
    async def get_teacher_profile(
        teacher_id: int,
        db: AsyncSession = Depends(get_db)
    ) -> TeacherWithQualifications:
        """
        Get teacher profile by ID with qualifications
        """
        # Get teacher profile by ID
        from sqlalchemy import select
        from models import TeacherProfile as TeacherProfileModel
        
        stmt = select(TeacherProfileModel).where(
            TeacherProfileModel.id == teacher_id
        )
        result = await db.execute(stmt)
        teacher_profile = result.scalar_one_or_none()
        
        if not teacher_profile:
            raise HTTPException(
                status_code=404,
                detail="Teacher profile not found"
            )

        # Get qualifications
        qualifications = await TeacherService.get_user_qualifications(
            db, teacher_profile.user_id
        )

        return TeacherWithQualifications(
            **teacher_profile.__dict__,
            qualifications=qualifications
        )