"""Chinese Language Certifications Data"""

from .hsk_level_1 import CERTIFICATION as HSK_LEVEL_1_CERT
from .hsk_level_2 import CERTIFICATION as HSK_LEVEL_2_CERT
from .hsk_level_3 import CERTIFICATION as HSK_LEVEL_3_CERT
from .hsk_level_4 import CERTIFICATION as HSK_LEVEL_4_CERT
from .hsk_level_5 import CERTIFICATION as HSK_LEVEL_5_CERT
from .hsk_level_6 import CERTIFICATION as HSK_LEVEL_6_CERT
from .hskk_elementary import CERTIFICATION as HSKK_ELEMENTARY_CERT
from .hskk_intermediate import CERTIFICATION as HSKK_INTERMEDIATE_CERT
from .hskk_advanced import CERTIFICATION as HSKK_ADVANCED_CERT
from .bct_a import CERTIFICATION as BCT_A_CERT
from .bct_b import CERTIFICATION as BCT_B_CERT
from .yct_level_1 import CERTIFICATION as YCT_LEVEL_1_CERT
from .tocfl_band_a_level_1 import CERTIFICATION as TOCFL_BAND_A_LEVEL_1_CERT

CERTIFICATIONS = [
    # Modern Comprehensive Chinese Certifications with Questions
    HSK_LEVEL_1_CERT,
    HSK_LEVEL_2_CERT,
    HSK_LEVEL_3_CERT,
    HSK_LEVEL_4_CERT,
    HSK_LEVEL_5_CERT,
    HSK_LEVEL_6_CERT,
    HSKK_ELEMENTARY_CERT,
    HSKK_INTERMEDIATE_CERT,
    HSKK_ADVANCED_CERT,
    BCT_A_CERT,
    BCT_B_CERT,
    YCT_LEVEL_1_CERT,
    TOCFL_BAND_A_LEVEL_1_CERT,

    # Additional YCT Levels (Traditional Format)
    {
        "name": "YCT Level 2",
        "description": "Youth Chinese Test for young learners - Elementary level",
        "slug": "yct-level-2",
        "level": "A2",
        "duration": 50,
        "questions_count": 50,
        "category_slug": "chinese"
    },

    # YCT (Youth Chinese Test) - Additional levels
    {
        "name": "YCT Level 2",
        "description": "Youth Chinese Test for young learners - Elementary level",
        "slug": "yct-level-2",
        "level": "A2",
        "duration": 50,
        "questions_count": 50,
        "category_slug": "chinese"
    },
    {
        "name": "YCT Level 3",
        "description": "Youth Chinese Test for young learners - Intermediate level",
        "slug": "yct-level-3",
        "level": "B1",
        "duration": 60,
        "questions_count": 60,
        "category_slug": "chinese"
    },
    {
        "name": "YCT Level 4",
        "description": "Youth Chinese Test for young learners - Upper-intermediate",
        "slug": "yct-level-4",
        "level": "B2",
        "duration": 85,
        "questions_count": 80,
        "category_slug": "chinese"
    },

    # TOCFL (Test of Chinese as a Foreign Language - Taiwan)
    {
        "name": "TOCFL Band A Level 1",
        "description": "Taiwan Chinese proficiency test - Novice level",
        "slug": "tocfl-band-a-level-1",
        "level": "A1",
        "duration": 60,
        "questions_count": 50,
        "category_slug": "chinese"
    },
    {
        "name": "TOCFL Band A Level 2",
        "description": "Taiwan Chinese proficiency test - Basic level",
        "slug": "tocfl-band-a-level-2",
        "level": "A2",
        "duration": 70,
        "questions_count": 60,
        "category_slug": "chinese"
    },
    {
        "name": "TOCFL Band B Level 3",
        "description": "Taiwan Chinese proficiency test - Intermediate level",
        "slug": "tocfl-band-b-level-3",
        "level": "B1",
        "duration": 110,
        "questions_count": 80,
        "category_slug": "chinese"
    },
    {
        "name": "TOCFL Band B Level 4",
        "description": "Taiwan Chinese proficiency test - High-intermediate level",
        "slug": "tocfl-band-b-level-4",
        "level": "B2",
        "duration": 110,
        "questions_count": 80,
        "category_slug": "chinese"
    },
    {
        "name": "TOCFL Band C Level 5",
        "description": "Taiwan Chinese proficiency test - Advanced level",
        "slug": "tocfl-band-c-level-5",
        "level": "C1",
        "duration": 120,
        "questions_count": 70,
        "category_slug": "chinese"
    }
]