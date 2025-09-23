"""English Language Certifications Data"""

from .ielts_academic import CERTIFICATION as IELTS_ACADEMIC_CERT
from .ielts_general import CERTIFICATION as IELTS_GENERAL_CERT
from .toefl_ibt import CERTIFICATION as TOEFL_IBT_CERT
from .toefl_essentials import CERTIFICATION as TOEFL_ESSENTIALS_CERT
from .cambridge_a2_key import CERTIFICATION as CAMBRIDGE_A2_KEY_CERT
from .cambridge_b1_preliminary import CERTIFICATION as CAMBRIDGE_B1_PRELIMINARY_CERT
from .cambridge_b2_first import CERTIFICATION as CAMBRIDGE_B2_FIRST_CERT
from .cambridge_c1_advanced import CERTIFICATION as CAMBRIDGE_C1_ADVANCED_CERT
from .cambridge_c2_proficiency import CERTIFICATION as CAMBRIDGE_C2_PROFICIENCY_CERT
from .cambridge_business_preliminary import CERTIFICATION as CAMBRIDGE_BUSINESS_PRELIMINARY_CERT
from .cambridge_business_vantage import CERTIFICATION as CAMBRIDGE_BUSINESS_VANTAGE_CERT
from .cambridge_business_higher import CERTIFICATION as CAMBRIDGE_BUSINESS_HIGHER_CERT
from .toeic_listening_reading import CERTIFICATION as TOEIC_LISTENING_READING_CERT
from .toeic_speaking_writing import CERTIFICATION as TOEIC_SPEAKING_WRITING_CERT
from .pte_academic import CERTIFICATION as PTE_ACADEMIC_CERT
from .duolingo_english_test import CERTIFICATION as DUOLINGO_ENGLISH_TEST_CERT
from .oxford_test_english import CERTIFICATION as OXFORD_TEST_ENGLISH_CERT

CERTIFICATIONS = [
    # Modern Comprehensive English Certifications with Questions
    IELTS_ACADEMIC_CERT,
    IELTS_GENERAL_CERT,
    TOEFL_IBT_CERT,
    TOEFL_ESSENTIALS_CERT,
    CAMBRIDGE_A2_KEY_CERT,
    CAMBRIDGE_B1_PRELIMINARY_CERT,
    CAMBRIDGE_B2_FIRST_CERT,
    CAMBRIDGE_C1_ADVANCED_CERT,
    CAMBRIDGE_C2_PROFICIENCY_CERT,
    CAMBRIDGE_BUSINESS_PRELIMINARY_CERT,
    CAMBRIDGE_BUSINESS_VANTAGE_CERT,
    CAMBRIDGE_BUSINESS_HIGHER_CERT,
    TOEIC_LISTENING_READING_CERT,
    TOEIC_SPEAKING_WRITING_CERT,
    PTE_ACADEMIC_CERT,
    DUOLINGO_ENGLISH_TEST_CERT,
    OXFORD_TEST_ENGLISH_CERT,

    # Additional certifications can be added here as needed
]
