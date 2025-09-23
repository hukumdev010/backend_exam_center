"""DSH-3 Certification"""

CERTIFICATION = {
    "name": "DSH-3",
    "description": "University entrance German language test - advanced level",
    "slug": "dsh-3",
    "level": "C2",
    "duration": 240,
    "questions_count": 70,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the highest DSH level?",
        "explanation": "DSH-3 is the highest level, corresponding to C2 proficiency for advanced university studies.",
        "reference": "DSH-3 Advanced Level",
        "points": 1,
        "answers": [
            {"text": "DSH-1", "is_correct": False},
            {"text": "DSH-2", "is_correct": False},
            {"text": "DSH-3", "is_correct": True},
            {"text": "DSH-4", "is_correct": False},
        ],
    }
]