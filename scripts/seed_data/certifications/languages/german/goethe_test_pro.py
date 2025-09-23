"""Goethe-Test PRO Deutsch Certification"""

CERTIFICATION = {
    "name": "Goethe-Test PRO Deutsch",
    "description": "German proficiency test for professional and business contexts",
    "slug": "goethe-test-pro",
    "level": "A1-C2",
    "duration": 90,
    "questions_count": 60,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is Goethe-Test PRO designed for?",
        "explanation": "Goethe-Test PRO is designed for professional and business German language assessment.",
        "reference": "Goethe-Test PRO Business German",
        "points": 1,
        "answers": [
            {"text": "Academic studies", "is_correct": False},
            {"text": "Professional and business contexts", "is_correct": True},
            {"text": "Tourism purposes", "is_correct": False},
            {"text": "Creative writing", "is_correct": False},
        ],
    }
]