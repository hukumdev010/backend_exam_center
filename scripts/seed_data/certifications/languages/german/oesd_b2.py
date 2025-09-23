"""ÖSD B2 Certification"""

CERTIFICATION = {
    "name": "ÖSD (Österreichisches Sprachdiplom) B2",
    "description": "Austrian German language diploma - upper-intermediate level",
    "slug": "oesd-b2",
    "level": "B2",
    "duration": 165,
    "questions_count": 55,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What level is ÖSD B2?",
        "explanation": "ÖSD B2 is upper-intermediate level Austrian German language certification.",
        "reference": "ÖSD B2 Upper-Intermediate",
        "points": 1,
        "answers": [
            {"text": "B1 level", "is_correct": False},
            {"text": "B2 level", "is_correct": True},
            {"text": "C1 level", "is_correct": False},
            {"text": "A2 level", "is_correct": False},
        ],
    }
]