"""BRIGHT Deutsch Certification"""

CERTIFICATION = {
    "name": "BRIGHT Deutsch",
    "description": "Professional German language assessment for workplace skills",
    "slug": "bright-deutsch",
    "level": "A1-C2",
    "duration": 60,
    "questions_count": 120,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is BRIGHT Deutsch used for?",
        "explanation": "BRIGHT Deutsch is used for professional German language assessment in workplace contexts.",
        "reference": "BRIGHT Deutsch Workplace Assessment",
        "points": 1,
        "answers": [
            {"text": "University admission", "is_correct": False},
            {"text": "Workplace skills assessment", "is_correct": True},
            {"text": "Tourism certification", "is_correct": False},
            {"text": "Academic research", "is_correct": False},
        ],
    }
]