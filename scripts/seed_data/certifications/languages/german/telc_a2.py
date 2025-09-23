"""telc Deutsch A2 Certification"""

CERTIFICATION = {
    "name": "telc Deutsch A2",
    "description": "Elementary German certificate for basic communication skills",
    "slug": "telc-a2",
    "level": "A2",
    "duration": 90,
    "questions_count": 40,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What level is telc Deutsch A2?",
        "explanation": "telc Deutsch A2 tests elementary level German for basic communication in familiar situations.",
        "reference": "telc A2 Elementary Level",
        "points": 1,
        "answers": [
            {"text": "A1 level", "is_correct": False},
            {"text": "A2 level", "is_correct": True},
            {"text": "B1 level", "is_correct": False},
            {"text": "B2 level", "is_correct": False},
        ],
    }
]