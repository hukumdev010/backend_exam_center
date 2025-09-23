"""Anatomy & Physiology Certifications"""

from .basic import CERTIFICATION as basic_cert, QUESTIONS as basic_questions
from .advanced import (
    CERTIFICATION as advanced_cert,
    QUESTIONS as advanced_questions
)

CERTIFICATIONS = [basic_cert, advanced_cert]
QUESTIONS = basic_questions + advanced_questions