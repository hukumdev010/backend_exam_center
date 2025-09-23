"""IELTS General Training Certification"""

CERTIFICATION = {
    "name": "IELTS General Training",
    "description": "IELTS for work experience and training programs, or for migration purposes",
    "slug": "ielts-general",
    "level": "A1-C2",
    "duration": 165,
    "questions_count": 120,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the main difference between IELTS Academic and IELTS General Training?",
        "explanation": "IELTS General Training is designed for people who want to migrate to an English-speaking country or apply for training programs and work experience.",
        "reference": "IELTS General Training Overview",
        "points": 1,
        "answers": [
            {"text": "General Training is easier", "is_correct": False},
            {"text": "General Training focuses on workplace and social contexts", "is_correct": True},
            {"text": "General Training has more questions", "is_correct": False},
            {"text": "General Training is only for beginners", "is_correct": False},
        ],
    },
    {
        "text": "In IELTS General Training Writing Task 1, what are you typically asked to write?",
        "explanation": "IELTS General Training Writing Task 1 requires you to write a letter (formal, semi-formal, or informal) in response to a given situation.",
        "reference": "IELTS General Training Writing Task 1",
        "points": 1,
        "answers": [
            {"text": "A formal essay", "is_correct": False},
            {"text": "A letter", "is_correct": True},
            {"text": "A report", "is_correct": False},
            {"text": "A summary", "is_correct": False},
        ],
    },
    {
        "text": "How many sections are in the IELTS General Training Reading test?",
        "explanation": "The IELTS General Training Reading test has three sections with increasing difficulty, containing texts from everyday contexts.",
        "reference": "IELTS General Training Reading Structure",
        "points": 1,
        "answers": [
            {"text": "Two sections", "is_correct": False},
            {"text": "Three sections", "is_correct": True},
            {"text": "Four sections", "is_correct": False},
            {"text": "Five sections", "is_correct": False},
        ],
    }
]