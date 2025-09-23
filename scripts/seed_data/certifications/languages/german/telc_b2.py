"""telc Deutsch B2 Certification"""

CERTIFICATION = {
    "name": "telc Deutsch B2",
    "description": "Upper-intermediate German for complex communication situations",
    "slug": "telc-b2",
    "level": "B2",
    "duration": 170,
    "questions_count": 50,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What level is telc Deutsch B2?",
        "explanation": "telc B2 is upper-intermediate level for complex communication in German.",
        "reference": "telc B2 Level",
        "points": 1,
        "answers": [
            {"text": "B1 level", "is_correct": False},
            {"text": "B2 level", "is_correct": True},
            {"text": "C1 level", "is_correct": False},
            {"text": "A2 level", "is_correct": False},
        ],
    }
]