"""PTE Academic Certification"""

CERTIFICATION = {
    "name": "PTE Academic",
    "description": "Pearson Test of English Academic - computer-based English test for study abroad",
    "slug": "pte-academic",
    "level": "B1-C2",
    "duration": 120,
    "questions_count": 70,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What makes PTE Academic unique compared to other English tests?",
        "explanation": "PTE Academic is a fully computer-based test that uses AI scoring, providing results within 48 hours and testing all four language skills in an integrated way.",
        "reference": "PTE Academic Features",
        "points": 1,
        "answers": [
            {"text": "It's only on paper", "is_correct": False},
            {"text": "It's fully computer-based with AI scoring", "is_correct": True},
            {"text": "It only tests reading", "is_correct": False},
            {"text": "It takes a week for results", "is_correct": False},
        ],
    },
    {
        "text": "How is PTE Academic scored?",
        "explanation": "PTE Academic uses a scale from 10-90, with scores aligned to the Global Scale of English and mapped to CEFR levels.",
        "reference": "PTE Academic Scoring",
        "points": 1,
        "answers": [
            {"text": "0-100 scale", "is_correct": False},
            {"text": "10-90 scale", "is_correct": True},
            {"text": "1-9 scale", "is_correct": False},
            {"text": "A-F scale", "is_correct": False},
        ],
    }
]