"""TOEIC Speaking & Writing Certification"""

CERTIFICATION = {
    "name": "TOEIC Speaking & Writing",
    "description": "TOEIC productive skills test for workplace communication",
    "slug": "toeic-speaking-writing",
    "level": "A1-C1",
    "duration": 80,
    "questions_count": 19,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What skills does TOEIC Speaking & Writing test?",
        "explanation": "TOEIC Speaking & Writing tests productive English skills - speaking and writing - for workplace communication.",
        "reference": "TOEIC Speaking & Writing Overview",
        "points": 1,
        "answers": [
            {"text": "Reading and listening", "is_correct": False},
            {"text": "Speaking and writing", "is_correct": True},
            {"text": "Grammar and vocabulary", "is_correct": False},
            {"text": "Translation skills", "is_correct": False},
        ],
    }
]