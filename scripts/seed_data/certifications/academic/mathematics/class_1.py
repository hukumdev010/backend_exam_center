"""Mathematics Class 1 Certification"""

CERTIFICATION = {
    "name": "Mathematics Class 1",
    "description": "Basic mathematics for 1st grade students",
    "slug": "mathematics-class-1",
    "level": "Class 1",
    "duration": 45,
    "questions_count": 20,
    "category_slug": "mathematics",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What comes after 5?",
        "explanation": (
            "Numbers follow a sequence: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10..."
        ),
        "reference": "Number Sequence",
        "points": 1,
        "answers": [
            {"text": "4", "is_correct": False},
            {"text": "6", "is_correct": True},
            {"text": "7", "is_correct": False},
            {"text": "3", "is_correct": False}
        ]
    },
    {
        "text": "How many fingers do you have on one hand?",
        "explanation": (
            "Each hand has 5 fingers: thumb, index, middle, ring, "
            "and little finger."
        ),
        "reference": "Counting",
        "points": 1,
        "answers": [
            {"text": "4", "is_correct": False},
            {"text": "5", "is_correct": True},
            {"text": "6", "is_correct": False},
            {"text": "10", "is_correct": False}
        ]
    },
    {
        "text": "What is 2 + 1?",
        "explanation": "Addition means putting things together. 2 + 1 = 3.",
        "reference": "Basic Addition",
        "points": 1,
        "answers": [
            {"text": "1", "is_correct": False},
            {"text": "2", "is_correct": False},
            {"text": "3", "is_correct": True},
            {"text": "4", "is_correct": False}
        ]
    }
]