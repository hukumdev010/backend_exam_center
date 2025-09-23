"""DELF B1 Certification"""

CERTIFICATION = {
    "name": "DELF B1",
    "description": "Intermediate French for main points of clear input on familiar matters",
    "slug": "delf-b1",
    "level": "B1",
    "duration": 105,
    "questions_count": 45,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What characterizes the B1 level in French?",
        "explanation": "B1 level allows you to understand main points of clear standard input on familiar matters and deal with most situations while traveling.",
        "reference": "DELF B1 Competency Framework",
        "points": 1,
        "answers": [
            {"text": "Only basic conversations", "is_correct": False},
            {"text": "Main points of familiar matters", "is_correct": True},
            {"text": "Complex academic texts", "is_correct": False},
            {"text": "Professional negotiations", "is_correct": False},
        ],
    }
]