"""telc Deutsch B1 Certification"""

CERTIFICATION = {
    "name": "telc Deutsch B1",
    "description": "Intermediate German certificate for independent language use",
    "slug": "telc-b1",
    "level": "B1",
    "duration": 150,
    "questions_count": 45,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does telc B1 demonstrate?",
        "explanation": "telc B1 demonstrates independent use of German in familiar situations and topics.",
        "reference": "telc B1 Independent Use",
        "points": 1,
        "answers": [
            {"text": "Basic communication", "is_correct": False},
            {"text": "Independent language use", "is_correct": True},
            {"text": "Advanced proficiency", "is_correct": False},
            {"text": "Native-like fluency", "is_correct": False},
        ],
    }
]