"""Russian Language Certifications Data"""

from .torfl_elementary import CERTIFICATION as TORFL_ELEMENTARY
from .torfl_basic import CERTIFICATION as TORFL_BASIC
from .torfl_first_level import CERTIFICATION as TORFL_FIRST_LEVEL
from .torfl_second_level import CERTIFICATION as TORFL_SECOND_LEVEL
from .torfl_third_level import CERTIFICATION as TORFL_THIRD_LEVEL
from .torfl_fourth_level import CERTIFICATION as TORFL_FOURTH_LEVEL
from .actfl_russian_opi import CERTIFICATION as ACTFL_RUSSIAN_OPI
from .actfl_russian_wpt import CERTIFICATION as ACTFL_RUSSIAN_WPT
from .actfl_russian_rpt import CERTIFICATION as ACTFL_RUSSIAN_RPT
from .actfl_russian_lpt import CERTIFICATION as ACTFL_RUSSIAN_LPT
from .dlpt_russian_1 import CERTIFICATION as DLPT_RUSSIAN_1
from .dlpt_russian_2 import CERTIFICATION as DLPT_RUSSIAN_2
from .dlpt_russian_3 import CERTIFICATION as DLPT_RUSSIAN_3
from .business_russian_elementary import CERTIFICATION as BUSINESS_RUSSIAN_ELEMENTARY
from .business_russian_intermediate import CERTIFICATION as BUSINESS_RUSSIAN_INTERMEDIATE
from .business_russian_advanced import CERTIFICATION as BUSINESS_RUSSIAN_ADVANCED
from .russian_olympiad_regional import CERTIFICATION as RUSSIAN_OLYMPIAD_REGIONAL
from .russian_olympiad_national import CERTIFICATION as RUSSIAN_OLYMPIAD_NATIONAL
from .academic_russian_b2 import CERTIFICATION as ACADEMIC_RUSSIAN_B2
from .academic_russian_c1 import CERTIFICATION as ACADEMIC_RUSSIAN_C1
from .russian_literature import CERTIFICATION as RUSSIAN_LITERATURE

CERTIFICATIONS = [
    TORFL_ELEMENTARY,
    TORFL_BASIC,
    TORFL_FIRST_LEVEL,
    TORFL_SECOND_LEVEL,
    TORFL_THIRD_LEVEL,
    TORFL_FOURTH_LEVEL,
    ACTFL_RUSSIAN_OPI,
    ACTFL_RUSSIAN_WPT,
    ACTFL_RUSSIAN_RPT,
    ACTFL_RUSSIAN_LPT,
    DLPT_RUSSIAN_1,
    DLPT_RUSSIAN_2,
    DLPT_RUSSIAN_3,
    BUSINESS_RUSSIAN_ELEMENTARY,
    BUSINESS_RUSSIAN_INTERMEDIATE,
    BUSINESS_RUSSIAN_ADVANCED,
    RUSSIAN_OLYMPIAD_REGIONAL,
    RUSSIAN_OLYMPIAD_NATIONAL,
    ACADEMIC_RUSSIAN_B2,
    ACADEMIC_RUSSIAN_C1,
    RUSSIAN_LITERATURE,
]