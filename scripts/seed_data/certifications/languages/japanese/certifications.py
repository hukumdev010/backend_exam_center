"""Japanese Language Certifications Data"""

# JLPT (Japanese Language Proficiency Test)
from .jlpt_n5 import CERTIFICATION as JLPT_N5_CERT
from .jlpt_n4 import CERTIFICATION as JLPT_N4_CERT
from .jlpt_n3 import CERTIFICATION as JLPT_N3_CERT
from .jlpt_n2 import CERTIFICATION as JLPT_N2_CERT
from .jlpt_n1 import CERTIFICATION as JLPT_N1_CERT

# NAT-TEST (Nihongo Ability Test)
from .nat_test_5q import CERTIFICATION as NAT_TEST_5Q_CERT
from .nat_test_4q import CERTIFICATION as NAT_TEST_4Q_CERT
from .nat_test_3q import CERTIFICATION as NAT_TEST_3Q_CERT
from .nat_test_2q import CERTIFICATION as NAT_TEST_2Q_CERT
from .nat_test_1q import CERTIFICATION as NAT_TEST_1Q_CERT

# J.TEST (Test of Practical Japanese)
from .j_test_g_f import CERTIFICATION as J_TEST_G_F_CERT
from .j_test_e_d import CERTIFICATION as J_TEST_E_D_CERT
from .j_test_c_b import CERTIFICATION as J_TEST_C_B_CERT
from .j_test_a import CERTIFICATION as J_TEST_A_CERT

# BJT (Business Japanese Proficiency Test)
from .bjt import CERTIFICATION as BJT_CERT

# EJU (Examination for Japanese University Admission)
from .eju_japanese import CERTIFICATION as EJU_JAPANESE_CERT

# Kanji Kentei (Japanese Kanji Proficiency Test)
from .kanji_kentei_10 import CERTIFICATION as KANJI_KENTEI_10_CERT
from .kanji_kentei_9 import CERTIFICATION as KANJI_KENTEI_9_CERT
from .kanji_kentei_8 import CERTIFICATION as KANJI_KENTEI_8_CERT
from .kanji_kentei_7 import CERTIFICATION as KANJI_KENTEI_7_CERT
from .kanji_kentei_6 import CERTIFICATION as KANJI_KENTEI_6_CERT
from .kanji_kentei_5 import CERTIFICATION as KANJI_KENTEI_5_CERT

CERTIFICATIONS = [
    # JLPT (Japanese Language Proficiency Test)
    JLPT_N5_CERT,
    JLPT_N4_CERT,
    JLPT_N3_CERT,
    JLPT_N2_CERT,
    JLPT_N1_CERT,
    
    # NAT-TEST (Nihongo Ability Test)
    NAT_TEST_5Q_CERT,
    NAT_TEST_4Q_CERT,
    NAT_TEST_3Q_CERT,
    NAT_TEST_2Q_CERT,
    NAT_TEST_1Q_CERT,
    
    # J.TEST (Test of Practical Japanese)
    J_TEST_G_F_CERT,
    J_TEST_E_D_CERT,
    J_TEST_C_B_CERT,
    J_TEST_A_CERT,
    
    # BJT (Business Japanese Proficiency Test)
    BJT_CERT,
    
    # EJU (Examination for Japanese University Admission)
    EJU_JAPANESE_CERT,
    
    # Kanji Kentei (Japanese Kanji Proficiency Test)
    KANJI_KENTEI_10_CERT,
    KANJI_KENTEI_9_CERT,
    KANJI_KENTEI_8_CERT,
    KANJI_KENTEI_7_CERT,
    KANJI_KENTEI_6_CERT,
    KANJI_KENTEI_5_CERT,
]