"""Cambridge C1 Business Higher Certification"""

CERTIFICATION = {
    "name": "Cambridge C1 Business Higher",
    "description": "Cambridge English Business Higher - advanced business English for international business",
    "slug": "cambridge-business-higher",
    "level": "C1",
    "duration": 180,
    "questions_count": 105,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What level is Cambridge Business Higher?",
        "explanation": "Cambridge Business Higher is an advanced (C1) level business English qualification for international business.",
        "reference": "Cambridge Business Higher Overview",
        "points": 1,
        "answers": [
            {"text": "B2 level", "is_correct": False},
            {"text": "C1 level", "is_correct": True},
            {"text": "C2 level", "is_correct": False},
            {"text": "B1 level", "is_correct": False},
        ],
    }
]