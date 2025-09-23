"""Medical Certifications"""

from .anatomy_physiology import certifications as anatomy_physiology_certs
from .pharmacology.basic import (
    CERTIFICATION as pharmacology_basic_cert,
    QUESTIONS as pharmacology_basic_questions
)
from .nursing.fundamentals import (
    CERTIFICATION as nursing_fundamentals_cert,
    QUESTIONS as nursing_fundamentals_questions
)
from .medical_terminology.basic import (
    CERTIFICATION as medical_terminology_cert,
    QUESTIONS as medical_terminology_questions
)
from .pathology.fundamentals import (
    CERTIFICATION as pathology_fundamentals_cert,
    QUESTIONS as pathology_fundamentals_questions
)
from .radiology.basic import (
    CERTIFICATION as radiology_basic_cert,
    QUESTIONS as radiology_basic_questions
)
from .medical_ethics.fundamentals import (
    CERTIFICATION as medical_ethics_cert,
    QUESTIONS as medical_ethics_questions
)

CERTIFICATIONS = (
    anatomy_physiology_certs.CERTIFICATIONS +
    [pharmacology_basic_cert] +
    [nursing_fundamentals_cert] +
    [medical_terminology_cert] +
    [pathology_fundamentals_cert] +
    [radiology_basic_cert] +
    [medical_ethics_cert]
)

QUESTIONS = (
    anatomy_physiology_certs.QUESTIONS +
    pharmacology_basic_questions +
    nursing_fundamentals_questions +
    medical_terminology_questions +
    pathology_fundamentals_questions +
    radiology_basic_questions +
    medical_ethics_questions
)