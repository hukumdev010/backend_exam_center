"""telc Deutsch C2 Certification"""

CERTIFICATION = {
    "name": "telc Deutsch C2",
    "description": "Proficient German certificate for mastery of the language",
    "slug": "telc-c2",
    "level": "C2",
    "duration": 250,
    "questions_count": 65,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the highest telc German level?",
        "explanation": "telc C2 is the highest level, demonstrating mastery of German language.",
        "reference": "telc C2 Mastery Level",
        "points": 1,
        "answers": [
            {"text": "telc C1", "is_correct": False},
            {"text": "telc C2", "is_correct": True},
            {"text": "telc B2", "is_correct": False},
            {"text": "telc C3", "is_correct": False},
        ],
    }
]