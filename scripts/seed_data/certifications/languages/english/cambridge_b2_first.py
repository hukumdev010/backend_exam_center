"""Cambridge B2 First (FCE) Certification"""

CERTIFICATION = {
    "name": "Cambridge B2 First (FCE)",
    "description": "Cambridge English First - upper-intermediate level English for work and study purposes",
    "slug": "cambridge-b2-first",
    "level": "B2",
    "duration": 210,
    "questions_count": 110,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What level of English proficiency does Cambridge B2 First demonstrate?",
        "explanation": "Cambridge B2 First demonstrates upper-intermediate (B2) level English skills, showing you can communicate effectively in English in work and study environments.",
        "reference": "Cambridge B2 First Overview",
        "points": 1,
        "answers": [
            {"text": "B1 level", "is_correct": False},
            {"text": "B2 level", "is_correct": True},
            {"text": "C1 level", "is_correct": False},
            {"text": "C2 level", "is_correct": False},
        ],
    },
    {
        "text": "How many parts are there in the Cambridge B2 First exam?",
        "explanation": "Cambridge B2 First consists of four papers: Reading and Use of English, Writing, Listening, and Speaking.",
        "reference": "Cambridge B2 First Exam Structure",
        "points": 1,
        "answers": [
            {"text": "Three parts", "is_correct": False},
            {"text": "Four parts", "is_correct": True},
            {"text": "Five parts", "is_correct": False},
            {"text": "Six parts", "is_correct": False},
        ],
    }
]