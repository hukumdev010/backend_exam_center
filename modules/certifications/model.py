from typing import Optional, List
from pydantic import BaseModel


class AnswerSubmission(BaseModel):
    question_id: int
    answer_id: int


class AnswerVerificationResponse(BaseModel):
    is_correct: bool
    points_earned: int
    total_points: int
    explanation: Optional[str]
    reference: Optional[str]


class Answer(BaseModel):
    id: int
    text: str
    question_id: int
    # is_correct is intentionally not included to avoid exposing answers

    class Config:
        from_attributes = True


class Question(BaseModel):
    id: int
    text: str
    explanation: Optional[str]
    reference: Optional[str]
    points: int
    certification_id: int
    answers: List[Answer]

    class Config:
        from_attributes = True


class Category(BaseModel):
    id: int
    name: str
    description: Optional[str]
    slug: str
    icon: Optional[str]
    color: Optional[str]

    class Config:
        from_attributes = True


class Certification(BaseModel):
    id: int
    name: str
    slug: str
    description: Optional[str]
    level: Optional[str]
    duration: Optional[int]
    questions_count: Optional[int]
    is_active: bool
    category_id: int
    questions: List[Question] = []
    category: Optional[Category] = None

    class Config:
        from_attributes = True


class CertificationSearch(BaseModel):
    results: List[Certification]
    total: int
    query: str