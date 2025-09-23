"""Mathematics Class 2 Certification"""

CERTIFICATION = {
    "name": "Mathematics Class 2",
    "description": "Elementary mathematics for 2nd grade students",
    "slug": "mathematics-class-2",
    "level": "Class 2",
    "duration": 50,
    "questions_count": 25,
    "category_slug": "mathematics",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is 5 + 3?",
        "explanation": "When we add 5 and 3, we get 8.",
        "reference": "Addition",
        "points": 1,
        "answers": [
            {"text": "7", "is_correct": False},
            {"text": "8", "is_correct": True},
            {"text": "9", "is_correct": False},
            {"text": "6", "is_correct": False}
        ]
    },
    {
        "text": "What is 10 - 4?",
        "explanation": "Subtraction means taking away. 10 - 4 = 6.",
        "reference": "Basic Subtraction",
        "points": 1,
        "answers": [
            {"text": "5", "is_correct": False},
            {"text": "6", "is_correct": True},
            {"text": "7", "is_correct": False},
            {"text": "14", "is_correct": False}
        ]
    },
    {
        "text": "How many sides does a triangle have?",
        "explanation": "A triangle is a shape with 3 sides and 3 corners.",
        "reference": "Basic Geometry",
        "points": 1,
        "answers": [
            {"text": "2", "is_correct": False},
            {"text": "3", "is_correct": True},
            {"text": "4", "is_correct": False},
            {"text": "5", "is_correct": False}
        ]
    }
]