"""Oxford Test of English Certification"""

CERTIFICATION = {
    "name": "Oxford Test of English",
    "description": "Oxford University Press English proficiency test for study and work",
    "slug": "oxford-test-english",
    "level": "A2-C1",
    "duration": 120,
    "questions_count": 80,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What organization created the Oxford Test of English?",
        "explanation": "The Oxford Test of English is created by Oxford University Press, focusing on practical English skills for study and work.",
        "reference": "Oxford Test of English Overview",
        "points": 1,
        "answers": [
            {"text": "Cambridge University", "is_correct": False},
            {"text": "Oxford University Press", "is_correct": True},
            {"text": "ETS", "is_correct": False},
            {"text": "Pearson", "is_correct": False},
        ],
    }
]