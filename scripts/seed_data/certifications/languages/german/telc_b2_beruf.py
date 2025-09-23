"""telc Deutsch B2+ Beruf Certification"""

CERTIFICATION = {
    "name": "telc Deutsch B2+ Beruf",
    "description": "Professional German certificate for upper-intermediate workplace skills",
    "slug": "telc-b2-beruf",
    "level": "B2",
    "duration": 180,
    "questions_count": 55,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does 'Beruf' mean in this certification?",
        "explanation": "Beruf means profession/occupation, indicating this test focuses on workplace German skills.",
        "reference": "telc B2+ Beruf Professional German",
        "points": 1,
        "answers": [
            {"text": "Academic", "is_correct": False},
            {"text": "Profession/workplace", "is_correct": True},
            {"text": "Tourism", "is_correct": False},
            {"text": "General conversation", "is_correct": False},
        ],
    }
]