"""Certification Data Package"""

from .academic import certifications as academic_certs
from .information_technology import certifications as it_certs
from .languages import certifications as language_certs
from .medical import certifications as medical_certs

CERTIFICATIONS = (
    academic_certs.CERTIFICATIONS +
    it_certs.CERTIFICATIONS +
    language_certs.CERTIFICATIONS +
    medical_certs.CERTIFICATIONS
)

QUESTIONS = (
    academic_certs.QUESTIONS +
    it_certs.QUESTIONS +
    language_certs.QUESTIONS +
    medical_certs.QUESTIONS
)