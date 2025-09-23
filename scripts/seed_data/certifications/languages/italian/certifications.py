"""Italian Language Certifications Data"""

# CILS (Certificazione di Italiano come Lingua Straniera)
from .cils_a1 import CERTIFICATION as CILS_A1_CERT
from .cils_a2 import CERTIFICATION as CILS_A2_CERT
from .cils_b1 import CERTIFICATION as CILS_B1_CERT
from .cils_b2 import CERTIFICATION as CILS_B2_CERT
from .cils_c1 import CERTIFICATION as CILS_C1_CERT
from .cils_c2 import CERTIFICATION as CILS_C2_CERT

# CELI (Certificato di Conoscenza della Lingua Italiana)
from .celi_1 import CERTIFICATION as CELI_1_CERT
from .celi_2 import CERTIFICATION as CELI_2_CERT
from .celi_3 import CERTIFICATION as CELI_3_CERT
from .celi_4 import CERTIFICATION as CELI_4_CERT
from .celi_5 import CERTIFICATION as CELI_5_CERT

# PLIDA (Progetto Lingua Italiana Dante Alighieri)
from .plida_a1 import CERTIFICATION as PLIDA_A1_CERT
from .plida_a2 import CERTIFICATION as PLIDA_A2_CERT
from .plida_b1 import CERTIFICATION as PLIDA_B1_CERT
from .plida_b2 import CERTIFICATION as PLIDA_B2_CERT
from .plida_c1 import CERTIFICATION as PLIDA_C1_CERT
from .plida_c2 import CERTIFICATION as PLIDA_C2_CERT

# AIL (Accademia Italiana di Lingua)
from .ail_dili_a2 import CERTIFICATION as AIL_DILI_A2_CERT
from .ail_dili_b1 import CERTIFICATION as AIL_DILI_B1_CERT
from .ail_dilc_b2 import CERTIFICATION as AIL_DILC_B2_CERT
from .ail_dali_c1 import CERTIFICATION as AIL_DALI_C1_CERT
from .ail_dalc_c1 import CERTIFICATION as AIL_DALC_C1_CERT

CERTIFICATIONS = [
    # CILS (Certificazione di Italiano come Lingua Straniera)
    CILS_A1_CERT,
    CILS_A2_CERT,
    CILS_B1_CERT,
    CILS_B2_CERT,
    CILS_C1_CERT,
    CILS_C2_CERT,
    
    # CELI (Certificato di Conoscenza della Lingua Italiana)
    CELI_1_CERT,
    CELI_2_CERT,
    CELI_3_CERT,
    CELI_4_CERT,
    CELI_5_CERT,
    
    # PLIDA (Progetto Lingua Italiana Dante Alighieri)
    PLIDA_A1_CERT,
    PLIDA_A2_CERT,
    PLIDA_B1_CERT,
    PLIDA_B2_CERT,
    PLIDA_C1_CERT,
    PLIDA_C2_CERT,
    
    # AIL (Accademia Italiana di Lingua)
    AIL_DILI_A2_CERT,
    AIL_DILI_B1_CERT,
    AIL_DILC_B2_CERT,
    AIL_DALI_C1_CERT,
    AIL_DALC_C1_CERT,
]