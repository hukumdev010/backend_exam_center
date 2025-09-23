"""French Language Certifications Data"""

from .delf_a1 import CERTIFICATION as DELF_A1_CERT
from .delf_a2 import CERTIFICATION as DELF_A2_CERT
from .delf_b1 import CERTIFICATION as DELF_B1_CERT
from .delf_b2 import CERTIFICATION as DELF_B2_CERT
from .dalf_c1 import CERTIFICATION as DALF_C1_CERT
from .dalf_c2 import CERTIFICATION as DALF_C2_CERT
from .tcf_tp import CERTIFICATION as TCF_TP_CERT
from .tcf_canada import CERTIFICATION as TCF_CANADA_CERT
from .tcf_anf import CERTIFICATION as TCF_ANF_CERT
from .tcf_dap import CERTIFICATION as TCF_DAP_CERT
from .tef import CERTIFICATION as TEF_CERT
from .tef_canada import CERTIFICATION as TEF_CANADA_CERT
from .tefaq import CERTIFICATION as TEFAQ_CERT
from .dfp_affaires_b1 import CERTIFICATION as DFP_AFFAIRES_B1_CERT
from .dfp_affaires_b2 import CERTIFICATION as DFP_AFFAIRES_B2_CERT
from .dfp_affaires_c1 import CERTIFICATION as DFP_AFFAIRES_C1_CERT
from .bright_french import CERTIFICATION as BRIGHT_FRENCH_CERT
from .dcl_fle import CERTIFICATION as DCL_FLE_CERT

CERTIFICATIONS = [
    # DELF (Diplôme d'études en langue française) Series
    DELF_A1_CERT,
    DELF_A2_CERT,
    DELF_B1_CERT,
    DELF_B2_CERT,
    
    # DALF (Diplôme approfondi de langue française) Series
    DALF_C1_CERT,
    DALF_C2_CERT,
    
    # TCF (Test de connaissance du français) Series
    TCF_TP_CERT,
    TCF_CANADA_CERT,
    TCF_ANF_CERT,
    TCF_DAP_CERT,
    
    # TEF (Test d'évaluation de français) Series
    TEF_CERT,
    TEF_CANADA_CERT,
    TEFAQ_CERT,
    
    # DFP (Diplôme de français professionnel) Series
    DFP_AFFAIRES_B1_CERT,
    DFP_AFFAIRES_B2_CERT,
    DFP_AFFAIRES_C1_CERT,
    # Other French Certifications
    BRIGHT_FRENCH_CERT,
    DCL_FLE_CERT,

    # Additional certifications can be added here as needed
]
