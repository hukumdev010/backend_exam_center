"""Mathematics Class 10 Certification"""

CERTIFICATION = {
    "name": "Mathematics Class 10",
    "description": "Advanced mathematics for 10th grade students",
    "slug": "mathematics-class-10",
    "level": "Class 10",
    "duration": 120,
    "questions_count": 60,
    "category_slug": "mathematics",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the quadratic formula?",
        "explanation": (
            "The quadratic formula is x = (-b ± √(b²-4ac)) / 2a "
            "for equation ax² + bx + c = 0."
        ),
        "reference": "Quadratic Equations",
        "points": 1,
        "answers": [
            {"text": "x = -b/2a", "is_correct": False},
            {"text": "x = (-b ± √(b²-4ac)) / 2a", "is_correct": True},
            {"text": "x = b/a", "is_correct": False},
            {"text": "x = c/a", "is_correct": False}
        ]
    },
    {
        "text": "What is the value of sin(30°)?",
        "reference": "Trigonometry",
        "points": 1,
        "answers": [
            {"text": "1/2", "is_correct": True},
            {"text": "√3/2", "is_correct": False},
            {"text": "1", "is_correct": False},
            {"text": "√2/2", "is_correct": False}
        ],
        "explanation": (
            "The area of a circle is π × r², "
            "where r is the radius."
        ),
    },
    {
        "text": "What is the area of a circle with radius r?",
        "explanation": (
            "The area of a circle is π × r², where r is the radius."
        ),
        "reference": "Circle Geometry",
        "points": 1,
        "answers": [
            {"text": "2πr", "is_correct": False},
            {"text": "πr²", "is_correct": True},
            {"text": "πr", "is_correct": False},
            {"text": "2πr²", "is_correct": False}
        ]
    }
]