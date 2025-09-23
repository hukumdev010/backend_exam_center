"""TOEIC Listening & Reading Certification"""

CERTIFICATION = {
    "name": "TOEIC Listening & Reading",
    "description": "Test of English for International Communication - workplace English proficiency",
    "slug": "toeic-listening-reading",
    "level": "A1-C1",
    "duration": 120,
    "questions_count": 200,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the main focus of the TOEIC test?",
        "explanation": "TOEIC focuses on workplace English communication skills, measuring how well people can communicate in English in professional settings.",
        "reference": "TOEIC Test Overview",
        "points": 1,
        "answers": [
            {"text": "Academic English", "is_correct": False},
            {"text": "Workplace English", "is_correct": True},
            {"text": "Conversational English", "is_correct": False},
            {"text": "Literary English", "is_correct": False},
        ],
    },
    {
        "text": "How many questions are in the TOEIC Listening & Reading test?",
        "explanation": "The TOEIC Listening & Reading test contains 200 questions: 100 listening questions and 100 reading questions.",
        "reference": "TOEIC Test Format",
        "points": 1,
        "answers": [
            {"text": "150 questions", "is_correct": False},
            {"text": "200 questions", "is_correct": True},
            {"text": "250 questions", "is_correct": False},
            {"text": "300 questions", "is_correct": False},
        ],
    }
]