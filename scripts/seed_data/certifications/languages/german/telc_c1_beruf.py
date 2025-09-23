"""telc Deutsch C1 Beruf Certification"""

CERTIFICATION = {
    "name": "telc Deutsch C1 Beruf",
    "description": "Advanced professional German certificate for workplace proficiency",
    "slug": "telc-c1-beruf",
    "level": "C1",
    "duration": 210,
    "questions_count": 65,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What level is telc C1 Beruf?",
        "explanation": "telc C1 Beruf is advanced level professional German for workplace proficiency.",
        "reference": "telc C1 Beruf Advanced Professional",
        "points": 1,
        "answers": [
            {"text": "B2 level", "is_correct": False},
            {"text": "C1 level", "is_correct": True},
            {"text": "C2 level", "is_correct": False},
            {"text": "B1 level", "is_correct": False},
        ],
    }
]