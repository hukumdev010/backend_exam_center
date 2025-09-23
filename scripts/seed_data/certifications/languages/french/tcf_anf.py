"""TCF ANF Certification"""

CERTIFICATION = {
    "name": "TCF ANF",
    "description": "Test for acquiring French nationality through naturalization",
    "slug": "tcf-anf",
    "level": "A1-B1",
    "duration": 90,
    "questions_count": 60,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the purpose of TCF ANF?",
        "explanation": "TCF ANF is used for acquiring French nationality through naturalization process.",
        "reference": "TCF ANF Purpose",
        "points": 1,
        "answers": [
            {"text": "University admission", "is_correct": False},
            {"text": "French nationality acquisition", "is_correct": True},
            {"text": "Job applications", "is_correct": False},
            {"text": "Tourism purposes", "is_correct": False},
        ],
    }
]