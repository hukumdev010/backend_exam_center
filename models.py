from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
    Float,
    Enum,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    slug = Column(String, unique=True, nullable=False)
    icon = Column(String, nullable=True)  # Icon name for UI
    color = Column(String, nullable=True)  # Color theme for UI
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    certifications = relationship("Certification", back_populates="category")


class Certification(Base):
    __tablename__ = "certifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    slug = Column(String, unique=True, nullable=False)
    # Associate, Professional, Specialty, etc.
    level = Column(String, nullable=True)
    duration = Column(Integer, nullable=True)  # Exam duration in minutes
    # Number of questions in the exam
    questions_count = Column(Integer, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    category = relationship("Category", back_populates="certifications")
    questions = relationship("Question", back_populates="certification")
    user_progress = relationship(
        "UserProgress",
        back_populates="certification")
    quiz_attempts = relationship("QuizAttempt", back_populates="certification")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    explanation = Column(String, nullable=True)
    # URL reference for additional information
    reference = Column(String, nullable=True)
    points = Column(Integer, default=1)
    certification_id = Column(
        Integer,
        ForeignKey("certifications.id"),
        nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    certification = relationship("Certification", back_populates="questions")
    answers = relationship(
        "Answer", back_populates="question", cascade="all, delete-orphan"
    )


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    question_id = Column(
        Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False
    )
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    question = relationship("Question", back_populates="answers")


# NextAuth.js Models


class Account(Base):
    __tablename__ = "accounts"

    id = Column(String, primary_key=True)
    user_id = Column(
        String,
        ForeignKey(
            "users.id",
            ondelete="CASCADE"),
        nullable=False)
    type = Column(String, nullable=False)
    provider = Column(String, nullable=False)
    provider_account_id = Column(String, nullable=False)
    refresh_token = Column(Text, nullable=True)
    access_token = Column(Text, nullable=True)
    expires_at = Column(Integer, nullable=True)
    token_type = Column(String, nullable=True)
    scope = Column(String, nullable=True)
    id_token = Column(Text, nullable=True)
    session_state = Column(String, nullable=True)

    # Relationships
    user = relationship("User", back_populates="accounts")

    __table_args__ = (UniqueConstraint("provider", "provider_account_id"),)


class Session(Base):
    __tablename__ = "sessions"

    id = Column(String, primary_key=True)
    session_token = Column(String, unique=True, nullable=False)
    user_id = Column(
        String,
        ForeignKey(
            "users.id",
            ondelete="CASCADE"),
        nullable=False)
    expires = Column(DateTime, nullable=False)

    # Relationships
    user = relationship("User", back_populates="sessions")


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    email_verified = Column(DateTime, nullable=True)
    image = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    accounts = relationship(
        "Account", back_populates="user", cascade="all, delete-orphan"
    )
    sessions = relationship(
        "Session", back_populates="user", cascade="all, delete-orphan"
    )
    progress = relationship(
        "UserProgress", back_populates="user", cascade="all, delete-orphan"
    )
    quiz_attempts = relationship(
        "QuizAttempt", back_populates="user", cascade="all, delete-orphan"
    )
    # Teacher-Student system relationships
    teacher_qualifications = relationship(
        "TeacherQualification", 
        back_populates="user", 
        cascade="all, delete-orphan"
    )
    teacher_profile = relationship(
        "TeacherProfile", 
        back_populates="user", 
        cascade="all, delete-orphan",
        foreign_keys="TeacherProfile.user_id"
    )
    session_bookings = relationship(
        "SessionBooking", 
        back_populates="student", 
        cascade="all, delete-orphan"
    )


class VerificationToken(Base):
    __tablename__ = "verification_tokens"

    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(String, nullable=False)
    token = Column(String, unique=True, nullable=False)
    expires = Column(DateTime, nullable=False)

    __table_args__ = (UniqueConstraint("identifier", "token"),)


# User Progress Tracking


class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(String, primary_key=True)
    user_id = Column(
        String,
        ForeignKey(
            "users.id",
            ondelete="CASCADE"),
        nullable=False)
    certification_id = Column(
        Integer,
        ForeignKey("certifications.id"),
        nullable=False)
    current_question = Column(Integer, default=0)
    total_questions = Column(Integer, nullable=False)
    correct_answers = Column(Integer, default=0)
    points = Column(Integer, default=0)
    is_completed = Column(Boolean, default=False)
    last_active_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="progress")
    certification = relationship(
        "Certification",
        back_populates="user_progress")

    __table_args__ = (UniqueConstraint("user_id", "certification_id"),)


class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    id = Column(String, primary_key=True)
    user_id = Column(
        String,
        ForeignKey(
            "users.id",
            ondelete="CASCADE"),
        nullable=False)
    certification_id = Column(
        Integer,
        ForeignKey("certifications.id"),
        nullable=False)
    score = Column(Integer, nullable=False)
    total_questions = Column(Integer, nullable=False)
    correct_answers = Column(Integer, nullable=False)
    points = Column(Integer, nullable=False)
    completed_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())

    # Relationships
    user = relationship("User", back_populates="quiz_attempts")
    certification = relationship(
        "Certification",
        back_populates="quiz_attempts")


# Teacher-Student System Enums
class TeacherStatus(enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    SUSPENDED = "suspended"


class SessionType(enum.Enum):
    ONE_ON_ONE = "one_on_one"
    GROUP = "group"


class SessionStatus(enum.Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    NO_SHOW = "no_show"


class BookingStatus(enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


# Teacher Qualification Model
class TeacherQualification(Base):
    __tablename__ = "teacher_qualifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        String,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False
    )
    certification_id = Column(
        Integer,
        ForeignKey("certifications.id"),
        nullable=False
    )
    quiz_attempt_id = Column(
        String,
        ForeignKey("quiz_attempts.id"),
        nullable=False
    )
    score_percentage = Column(Float, nullable=False)  # The 90%+ score
    is_active = Column(Boolean, default=True)
    qualified_at = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="teacher_qualifications")
    category = relationship("Category")
    certification = relationship("Certification")
    quiz_attempt = relationship("QuizAttempt")
    
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "certification_id",
            name="unique_user_certification_qualification"
        ),
    )


# Teacher Profile Model
class TeacherProfile(Base):
    __tablename__ = "teacher_profiles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        String,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )
    bio = Column(Text, nullable=True)
    experience_years = Column(Integer, nullable=True)
    hourly_rate_one_on_one = Column(Float, nullable=True)  # USD per hour 1:1
    hourly_rate_group = Column(Float, nullable=True)  # USD/hour/student group
    max_group_size = Column(Integer, default=10)
    status = Column(Enum(TeacherStatus), default=TeacherStatus.PENDING)
    is_available = Column(Boolean, default=True)
    languages_spoken = Column(String, nullable=True)  # JSON array as string
    timezone = Column(String, nullable=True)
    approved_by = Column(String, ForeignKey("users.id"), nullable=True)
    approved_at = Column(DateTime, nullable=True)
    rejection_reason = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship(
        "User", 
        back_populates="teacher_profile", 
        foreign_keys=[user_id]
    )
    approved_by_user = relationship(
        "User", 
        foreign_keys=[approved_by]
    )
    sessions = relationship("TeachingSession", back_populates="teacher")
    

# Teaching Session Model (for both one-on-one and group sessions)
class TeachingSession(Base):
    __tablename__ = "teaching_sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_id = Column(
        Integer,
        ForeignKey("teacher_profiles.id", ondelete="CASCADE"),
        nullable=False
    )
    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False
    )
    certification_id = Column(
        Integer,
        ForeignKey("certifications.id"),
        nullable=True  # Can be general category teaching
    )
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    session_type = Column(Enum(SessionType), nullable=False)
    max_participants = Column(Integer, nullable=False, default=1)  # 1:1 or >1
    current_participants = Column(Integer, default=0)
    duration_minutes = Column(Integer, nullable=False)  # Session duration
    price_per_participant = Column(Float, nullable=False)  # Price per student
    scheduled_at = Column(DateTime, nullable=False)
    status = Column(Enum(SessionStatus), default=SessionStatus.SCHEDULED)
    meeting_link = Column(String, nullable=True)  # Zoom, Google Meet, etc.
    meeting_password = Column(String, nullable=True)
    notes = Column(Text, nullable=True)  # Teacher's notes for the session
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    teacher = relationship("TeacherProfile", back_populates="sessions")
    category = relationship("Category")
    certification = relationship("Certification")
    bookings = relationship(
        "SessionBooking",
        back_populates="session",
        cascade="all, delete-orphan"
    )


# Session Booking Model
class SessionBooking(Base):
    __tablename__ = "session_bookings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(
        Integer,
        ForeignKey("teaching_sessions.id", ondelete="CASCADE"),
        nullable=False
    )
    student_id = Column(
        String,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    status = Column(Enum(BookingStatus), default=BookingStatus.PENDING)
    amount_paid = Column(Float, nullable=False)
    payment_method = Column(String, nullable=True)  # stripe, paypal, etc.
    payment_transaction_id = Column(String, nullable=True)
    booking_notes = Column(Text, nullable=True)  # Student's notes/questions
    attendance_confirmed = Column(Boolean, default=False)
    feedback_rating = Column(Integer, nullable=True)  # 1-5 stars
    feedback_comment = Column(Text, nullable=True)
    booked_at = Column(DateTime, default=func.now())
    cancelled_at = Column(DateTime, nullable=True)
    cancellation_reason = Column(Text, nullable=True)

    # Relationships
    session = relationship("TeachingSession", back_populates="bookings")
    student = relationship("User", back_populates="session_bookings")
