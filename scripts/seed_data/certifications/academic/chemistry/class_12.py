"""Chemistry Class 12 Certification"""

CERTIFICATION = {
    "name": "Chemistry Class 12",
    "description": "Advanced chemistry concepts for 12th grade students",
    "slug": "chemistry-class-12",
    "level": "Class 12",
    "duration": 75,
    "questions_count": 30,
    "category_slug": "chemistry",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the hybridization of carbon in methane (CH4)?",
        "explanation": (
            "In methane, carbon forms 4 single bonds, "
            "resulting in sp3 hybridization."
        ),
        "reference": "Chemical Bonding",
        "points": 1,
        "answers": [
            {"text": "sp", "is_correct": False},
            {"text": "sp2", "is_correct": False},
            {"text": "sp3", "is_correct": True},
            {"text": "sp3d", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following is an aldehyde?",
        "explanation": (
            "Formaldehyde (HCHO) has a carbonyl group at the end of "
            "the carbon chain, making it an aldehyde."
        ),
        "reference": "Organic Chemistry",
        "points": 1,
        "answers": [
            {"text": "CH3COCH3", "is_correct": False},
            {"text": "HCHO", "is_correct": True},
            {"text": "CH3OH", "is_correct": False},
            {"text": "CH3COOH", "is_correct": False}
        ]
    },
    {
        "text": "What is the IUPAC name of CH3CH2OH?",
        "explanation": (
            "This is a 2-carbon alcohol, so its IUPAC name is ethanol."
        ),
        "reference": "Organic Nomenclature",
        "points": 1,
        "answers": [
            {"text": "Methanol", "is_correct": False},
            {"text": "Ethanol", "is_correct": True},
            {"text": "Propanol", "is_correct": False},
            {"text": "Butanol", "is_correct": False}
        ]
    },
    {
        "text": "What is the order of reaction if rate = k[A]²[B]?",
        "explanation": (
            "The overall order is the sum of individual orders: 2 + 1 = 3."
        ),
        "reference": "Chemical Kinetics",
        "points": 1,
        "answers": [
            {"text": "1", "is_correct": False},
            {"text": "2", "is_correct": False},
            {"text": "3", "is_correct": True},
            {"text": "4", "is_correct": False}
        ]
    },
    {
        "text": "Which metal is extracted by electrolysis of molten ore?",
        "explanation": (
            "Aluminum is extracted by electrolysis of molten alumina."
        ),
        "reference": "Metallurgy",
        "points": 1,
        "answers": [
            {"text": "Iron", "is_correct": False},
            {"text": "Copper", "is_correct": False},
            {"text": "Aluminum", "is_correct": True},
            {"text": "Zinc", "is_correct": False}
        ]
    }
]