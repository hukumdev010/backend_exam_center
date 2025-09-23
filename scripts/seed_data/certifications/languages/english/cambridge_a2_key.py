"""Cambridge A2 Key (KET) Certification"""

CERTIFICATION = {
    "name": "Cambridge A2 Key (KET)",
    "description": "Cambridge English Key - basic level English qualification for everyday situations",
    "slug": "cambridge-a2-key",
    "level": "A2",
    "duration": 120,
    "questions_count": 80,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What level of English does Cambridge A2 Key test?",
        "explanation": "Cambridge A2 Key tests basic English skills at A2 level, demonstrating that you can use English to communicate in simple situations.",
        "reference": "Cambridge A2 Key Overview",
        "points": 1,
        "answers": [
            {"text": "A1 level", "is_correct": False},
            {"text": "A2 level", "is_correct": True},
            {"text": "B1 level", "is_correct": False},
            {"text": "B2 level", "is_correct": False},
        ],
    },
    {
        "text": "How many papers are there in the Cambridge A2 Key exam?",
        "explanation": "Cambridge A2 Key consists of three papers: Reading and Writing (combined paper), Listening, and Speaking.",
        "reference": "Cambridge A2 Key Exam Format",
        "points": 1,
        "answers": [
            {"text": "Two papers", "is_correct": False},
            {"text": "Three papers", "is_correct": True},
            {"text": "Four papers", "is_correct": False},
            {"text": "Five papers", "is_correct": False},
        ],
    }
]