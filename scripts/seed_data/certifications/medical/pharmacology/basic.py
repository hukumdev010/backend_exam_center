"""Pharmacology Basics Certification"""

CERTIFICATION = {
    "name": "Pharmacology Basics",
    "description": "Fundamental principles of drug action and therapy",
    "slug": "pharmacology-basics",
    "level": "Beginner",
    "duration": 45,
    "questions_count": 20,
    "category_slug": "pharmacology",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is pharmacokinetics?",
        "explanation": (
            "Pharmacokinetics studies what the body does to a drug: "
            "absorption, distribution, metabolism, and excretion (ADME)."
        ),
        "reference": "Basic Pharmacology",
        "points": 1,
        "answers": [
            {"text": "What drugs do to the body", "is_correct": False},
            {"text": "What the body does to drugs", "is_correct": True},
            {"text": "Drug manufacturing process", "is_correct": False},
            {"text": "Drug side effects", "is_correct": False}
        ]
    },
    {
        "text": "What is the half-life of a drug?",
        "explanation": (
            "Half-life is the time required for the plasma concentration "
            "of a drug to decrease by 50%."
        ),
        "reference": "Pharmacokinetics",
        "points": 1,
        "answers": [
            {"text": "Time for drug to reach maximum effect", "is_correct": False},
            {"text": "Time for 50% drug elimination", "is_correct": True},
            {"text": "Duration of drug action", "is_correct": False},
            {"text": "Time to reach steady state", "is_correct": False}
        ]
    },
    {
        "text": "What is bioavailability?",
        "explanation": (
            "Bioavailability is the fraction of administered drug "
            "that reaches the systemic circulation unchanged."
        ),
        "reference": "Drug Absorption",
        "points": 1,
        "answers": [
            {"text": "Drug potency", "is_correct": False},
            {"text": "Drug efficacy", "is_correct": False},
            {"text": "Fraction reaching systemic circulation", "is_correct": True},
            {"text": "Drug metabolism rate", "is_correct": False}
        ]
    },
    {
        "text": "Which route has 100% bioavailability?",
        "explanation": (
            "Intravenous administration bypasses absorption barriers "
            "and delivers 100% of the drug to systemic circulation."
        ),
        "reference": "Drug Administration",
        "points": 1,
        "answers": [
            {"text": "Oral", "is_correct": False},
            {"text": "Intramuscular", "is_correct": False},
            {"text": "Intravenous", "is_correct": True},
            {"text": "Sublingual", "is_correct": False}
        ]
    },
    {
        "text": "What is an agonist?",
        "explanation": (
            "An agonist is a drug that binds to and activates "
            "a receptor to produce a biological response."
        ),
        "reference": "Receptor Pharmacology",
        "points": 1,
        "answers": [
            {"text": "Blocks receptor activation", "is_correct": False},
            {"text": "Activates receptors", "is_correct": True},
            {"text": "Destroys receptors", "is_correct": False},
            {"text": "Modifies receptor structure", "is_correct": False}
        ]
    }
]