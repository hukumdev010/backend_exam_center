"""BRIGHT French Certification"""

CERTIFICATION = {
    "name": "BRIGHT French",
    "description": "Professional French language assessment for workplace skills",
    "slug": "bright-french",
    "level": "A1-C2",
    "duration": 60,
    "questions_count": 120,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is BRIGHT French designed for?",
        "explanation": "BRIGHT French is designed for professional assessment of French language skills in workplace contexts.",
        "reference": "BRIGHT French Workplace Assessment",
        "points": 1,
        "answers": [
            {"text": "Academic studies", "is_correct": False},
            {"text": "Workplace skills assessment", "is_correct": True},
            {"text": "Tourism purposes", "is_correct": False},
            {"text": "Immigration", "is_correct": False},
        ],
    }
]