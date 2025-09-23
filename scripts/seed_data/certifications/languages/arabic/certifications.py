"""Arabic Language Certifications Data"""

from .msa_proficiency import CERTIFICATION as MSA_PROFICIENCY_CERT
from .business_arabic import CERTIFICATION as BUSINESS_ARABIC_CERT
from .quranic_arabic import CERTIFICATION as QURANIC_ARABIC_CERT
from .media_arabic import CERTIFICATION as MEDIA_ARABIC_CERT
from .islamic_studies_arabic import CERTIFICATION as ISLAMIC_STUDIES_CERT

CERTIFICATIONS = [
    # Modern Comprehensive Arabic Certifications
    MSA_PROFICIENCY_CERT,
    BUSINESS_ARABIC_CERT,
    QURANIC_ARABIC_CERT,
    MEDIA_ARABIC_CERT,
    ISLAMIC_STUDIES_CERT,

    # Traditional ALPT (Arabic Language Proficiency Test)
    {
        "name": "ALPT Novice",
        "description": "Basic Arabic proficiency for everyday situations",
        "slug": "alpt-novice",
        "level": "A1",
        "duration": 90,
        "questions_count": 60,
        "category_slug": "arabic"
    },
    {
        "name": "ALPT Elementary",
        "description": "Elementary Arabic for simple conversations",
        "slug": "alpt-elementary",
        "level": "A2",
        "duration": 110,
        "questions_count": 70,
        "category_slug": "arabic"
    },
    {
        "name": "ALPT Intermediate",
        "description": "Intermediate Arabic for workplace and social contexts",
        "slug": "alpt-intermediate",
        "level": "B1",
        "duration": 140,
        "questions_count": 80,
        "category_slug": "arabic"
    },
    {
        "name": "ALPT Advanced",
        "description": "Advanced Arabic for academic and professional use",
        "slug": "alpt-advanced",
        "level": "B2-C1",
        "duration": 160,
        "questions_count": 90,
        "category_slug": "arabic"
    },

    # ACTFL Arabic Proficiency Tests
    {
        "name": "ACTFL Arabic OPI",
        "description": "Arabic Oral Proficiency Interview by ACTFL",
        "slug": "actfl-arabic-opi",
        "level": "A1-C2",
        "duration": 30,
        "questions_count": 15,
        "category_slug": "arabic"
    },
    {
        "name": "ACTFL Arabic WPT",
        "description": "Arabic Writing Proficiency Test by ACTFL",
        "slug": "actfl-arabic-wpt",
        "level": "A1-C2",
        "duration": 80,
        "questions_count": 4,
        "category_slug": "arabic"
    },
    {
        "name": "ACTFL Arabic RPT",
        "description": "Arabic Reading Proficiency Test by ACTFL",
        "slug": "actfl-arabic-rpt",
        "level": "A1-C2",
        "duration": 60,
        "questions_count": 40,
        "category_slug": "arabic"
    },
    {
        "name": "ACTFL Arabic LPT",
        "description": "Arabic Listening Proficiency Test by ACTFL",
        "slug": "actfl-arabic-lpt",
        "level": "A1-C2",
        "duration": 60,
        "questions_count": 35,
        "category_slug": "arabic"
    },

    # CIMA (Certificate in Modern Standard Arabic)
    {
        "name": "CIMA Foundation",
        "description": "Foundation Certificate in Modern Standard Arabic",
        "slug": "cima-foundation",
        "level": "A1-A2",
        "duration": 120,
        "questions_count": 75,
        "category_slug": "arabic"
    },
    {
        "name": "CIMA Intermediate",
        "description": "Intermediate Certificate in Modern Standard Arabic",
        "slug": "cima-intermediate",
        "level": "B1-B2",
        "duration": 150,
        "questions_count": 85,
        "category_slug": "arabic"
    },
    {
        "name": "CIMA Advanced",
        "description": "Advanced Certificate in Modern Standard Arabic",
        "slug": "cima-advanced",
        "level": "C1-C2",
        "duration": 180,
        "questions_count": 95,
        "category_slug": "arabic"
    },

    # DLPT (Defense Language Proficiency Test) Arabic
    {
        "name": "DLPT Arabic Level 1",
        "description": "Defense Language Proficiency Test Arabic - Level 1",
        "slug": "dlpt-arabic-1",
        "level": "A2",
        "duration": 180,
        "questions_count": 100,
        "category_slug": "arabic"
    },
    {
        "name": "DLPT Arabic Level 2",
        "description": "Defense Language Proficiency Test Arabic - Level 2",
        "slug": "dlpt-arabic-2",
        "level": "B1",
        "duration": 180,
        "questions_count": 100,
        "category_slug": "arabic"
    },
    {
        "name": "DLPT Arabic Level 3",
        "description": "Defense Language Proficiency Test Arabic - Level 3",
        "slug": "dlpt-arabic-3",
        "level": "B2-C1",
        "duration": 180,
        "questions_count": 100,
        "category_slug": "arabic"
    },

    # CASA (Center for Arabic Study Abroad) Proficiency Test
    {
        "name": "CASA Proficiency Test",
        "description": "Arabic proficiency assessment by CASA",
        "slug": "casa-proficiency",
        "level": "B1-C2",
        "duration": 120,
        "questions_count": 60,
        "category_slug": "arabic"
    }
]