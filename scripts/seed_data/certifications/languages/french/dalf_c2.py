"""DALF C2 Certification"""

CERTIFICATION = {
    "name": "DALF C2",
    "description": "Proficient French with ease of understanding everything heard or read",
    "slug": "dalf-c2",
    "level": "C2",
    "duration": 210,
    "questions_count": 65,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the highest level of French proficiency?",
        "explanation": "DALF C2 represents mastery level, with ease of understanding everything heard or read and ability to summarize information from different sources.",
        "reference": "DALF C2 Mastery Level",
        "points": 1,
        "answers": [
            {"text": "DELF B2", "is_correct": False},
            {"text": "DALF C1", "is_correct": False},
            {"text": "DALF C2", "is_correct": True},
            {"text": "DELF B1", "is_correct": False},
        ],
    }
]