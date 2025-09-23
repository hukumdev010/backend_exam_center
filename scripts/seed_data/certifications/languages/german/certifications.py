"""German Language Certifications Data"""

from .goethe_a1 import CERTIFICATION as GOETHE_A1_CERT
from .goethe_a2 import CERTIFICATION as GOETHE_A2_CERT
from .goethe_b1 import CERTIFICATION as GOETHE_B1_CERT
from .goethe_b2 import CERTIFICATION as GOETHE_B2_CERT
from .goethe_c1 import CERTIFICATION as GOETHE_C1_CERT
from .goethe_c2 import CERTIFICATION as GOETHE_C2_CERT
from .testdaf import CERTIFICATION as TESTDAF_CERT
from .dsh_1 import CERTIFICATION as DSH_1_CERT
from .dsh_2 import CERTIFICATION as DSH_2_CERT
from .dsh_3 import CERTIFICATION as DSH_3_CERT
from .telc_a1 import CERTIFICATION as TELC_A1_CERT
from .telc_a2 import CERTIFICATION as TELC_A2_CERT
from .telc_b1 import CERTIFICATION as TELC_B1_CERT
from .telc_b2 import CERTIFICATION as TELC_B2_CERT
from .telc_c1 import CERTIFICATION as TELC_C1_CERT
from .telc_c2 import CERTIFICATION as TELC_C2_CERT
from .goethe_test_pro import CERTIFICATION as GOETHE_TEST_PRO_CERT
from .telc_b2_beruf import CERTIFICATION as TELC_B2_BERUF_CERT
from .telc_c1_beruf import CERTIFICATION as TELC_C1_BERUF_CERT
from .bright_deutsch import CERTIFICATION as BRIGHT_DEUTSCH_CERT
from .oesd_b1 import CERTIFICATION as OESD_B1_CERT
from .oesd_b2 import CERTIFICATION as OESD_B2_CERT

CERTIFICATIONS = [
    # Goethe Institute Certifications
    GOETHE_A1_CERT,
    GOETHE_A2_CERT,
    GOETHE_B1_CERT,
    GOETHE_B2_CERT,
    GOETHE_C1_CERT,
    GOETHE_C2_CERT,
    
    # TestDaF (Test Deutsch als Fremdsprache)
    TESTDAF_CERT,
    
    # DSH (Deutsche Sprachprüfung für den Hochschulzugang)
    DSH_1_CERT,
    DSH_2_CERT,
    DSH_3_CERT,
    
    # telc (The European Language Certificates)
    TELC_A1_CERT,
    TELC_A2_CERT,
    TELC_B1_CERT,
    TELC_B2_CERT,
    TELC_C1_CERT,
    TELC_C2_CERT,
    
    # Business German
    GOETHE_TEST_PRO_CERT,
    TELC_B2_BERUF_CERT,
    TELC_C1_BERUF_CERT,
    
    # Other German Certifications
    BRIGHT_DEUTSCH_CERT,
    OESD_B1_CERT,
    OESD_B2_CERT,

]