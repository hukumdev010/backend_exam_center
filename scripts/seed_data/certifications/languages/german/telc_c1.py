"""telc Deutsch C1 Certification"""

CERTIFICATION = {
    "name": "telc Deutsch C1",
    "description": "Advanced German certificate for effective operational proficiency",
    "slug": "telc-c1",
    "level": "C1",
    "duration": 220,
    "questions_count": 60,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does telc C1 demonstrate?",
        "explanation": "telc C1 demonstrates advanced German with effective operational proficiency.",
        "reference": "telc C1 Advanced Level",
        "points": 1,
        "answers": [
            {"text": "Basic skills", "is_correct": False},
            {"text": "Advanced operational proficiency", "is_correct": True},
            {"text": "Elementary communication", "is_correct": False},
            {"text": "Intermediate skills", "is_correct": False},
        ],
    }
]