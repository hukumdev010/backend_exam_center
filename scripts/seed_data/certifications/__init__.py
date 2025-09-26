"""Certification Data Package"""

from . import academic
from . import information_technology
from . import languages  
from . import medical

CERTIFICATIONS = []
ALL_QUESTIONS = {}

if hasattr(academic, 'CERTIFICATIONS'):
    CERTIFICATIONS.extend(academic.CERTIFICATIONS)
if hasattr(information_technology, 'CERTIFICATIONS'):
    CERTIFICATIONS.extend(information_technology.CERTIFICATIONS)
if hasattr(languages, 'CERTIFICATIONS'):
    CERTIFICATIONS.extend(languages.CERTIFICATIONS)
if hasattr(medical, 'CERTIFICATIONS'):
    CERTIFICATIONS.extend(medical.CERTIFICATIONS)

if hasattr(academic, 'ALL_QUESTIONS'):
    ALL_QUESTIONS.update(academic.ALL_QUESTIONS)
if hasattr(information_technology, 'ALL_QUESTIONS'):
    ALL_QUESTIONS.update(information_technology.ALL_QUESTIONS)
if hasattr(languages, 'ALL_QUESTIONS'):
    ALL_QUESTIONS.update(languages.ALL_QUESTIONS)
if hasattr(medical, 'ALL_QUESTIONS'):
    ALL_QUESTIONS.update(medical.ALL_QUESTIONS)