"""Cambridge B1 Business Preliminary Certification"""

CERTIFICATION = {
    "name": "Cambridge B1 Business Preliminary",
    "description": "Cambridge English Business Preliminary - intermediate business English skills",
    "slug": "cambridge-business-preliminary",
    "level": "B1",
    "duration": 140,
    "questions_count": 85,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the focus of Cambridge Business Preliminary?",
        "explanation": "Cambridge Business Preliminary focuses on intermediate level business English skills for workplace communication.",
        "reference": "Cambridge Business Preliminary Overview",
        "points": 1,
        "answers": [
            {"text": "Academic English", "is_correct": False},
            {"text": "Business English", "is_correct": True},
            {"text": "General conversation", "is_correct": False},
            {"text": "Technical English", "is_correct": False},
        ],
    }
]