"""DELF B2 Certification"""

CERTIFICATION = {
    "name": "DELF B2",
    "description": "Upper-intermediate French for complex texts and abstract topics",
    "slug": "delf-b2",
    "level": "B2",
    "duration": 150,
    "questions_count": 50,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What can you achieve at DELF B2 level?",
        "explanation": "B2 level enables understanding of complex texts on concrete and abstract topics and interaction with native speakers with spontaneity.",
        "reference": "DELF B2 Capabilities",
        "points": 1,
        "answers": [
            {"text": "Only simple conversations", "is_correct": False},
            {"text": "Complex texts and abstract topics", "is_correct": True},
            {"text": "Basic greetings only", "is_correct": False},
            {"text": "Elementary vocabulary", "is_correct": False},
        ],
    }
]