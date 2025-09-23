"""DSH-1 Certification"""

CERTIFICATION = {
    "name": "DSH-1",
    "description": "University entrance German language test - basic level",
    "slug": "dsh-1",
    "level": "B2",
    "duration": 240,
    "questions_count": 60,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does DSH stand for?",
        "explanation": "DSH stands for Deutsche Sprachprüfung für den Hochschulzugang - German language test for university entrance.",
        "reference": "DSH Overview",
        "points": 1,
        "answers": [
            {"text": "Deutsche Sprachprüfung für den Hochschulzugang", "is_correct": True},
            {"text": "Deutsche Sprach Hochschule", "is_correct": False},
            {"text": "Deutsches Sprach Handel", "is_correct": False},
            {"text": "Deutsche Sprach Historie", "is_correct": False},
        ],
    }
]