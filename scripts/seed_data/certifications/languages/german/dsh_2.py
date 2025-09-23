"""DSH-2 Certification"""

CERTIFICATION = {
    "name": "DSH-2",
    "description": "University entrance German language test - intermediate level",
    "slug": "dsh-2",
    "level": "C1",
    "duration": 240,
    "questions_count": 65,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What level does DSH-2 correspond to?",
        "explanation": "DSH-2 corresponds to C1 level German proficiency for university entrance requirements.",
        "reference": "DSH-2 Level Requirements",
        "points": 1,
        "answers": [
            {"text": "B2 level", "is_correct": False},
            {"text": "C1 level", "is_correct": True},
            {"text": "C2 level", "is_correct": False},
            {"text": "B1 level", "is_correct": False},
        ],
    }
]