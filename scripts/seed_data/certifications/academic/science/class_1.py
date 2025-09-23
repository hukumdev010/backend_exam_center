"""Science Class 1 Certification"""

CERTIFICATION = {
    "name": "Science Class 1",
    "description": "Basic science concepts for 1st grade students",
    "slug": "science-class-1",
    "level": "Class 1",
    "duration": 45,
    "questions_count": 20,
    "category_slug": "science",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What do plants need to grow?",
        "explanation": (
            "Plants need water, sunlight, and air (carbon dioxide) "
            "to grow through photosynthesis."
        ),
        "reference": "Basic Plant Biology",
        "points": 1,
        "answers": [
            {"text": "Only water", "is_correct": False},
            {"text": "Water, sunlight, and air", "is_correct": True},
            {"text": "Only sunlight", "is_correct": False},
            {"text": "Only soil", "is_correct": False}
        ]
    },
    {
        "text": "Which of these is a living thing?",
        "explanation": (
            "A tree is a living organism that grows, breathes, "
            "and reproduces."
        ),
        "reference": "Living vs Non-living Things",
        "points": 1,
        "answers": [
            {"text": "Rock", "is_correct": False},
            {"text": "Tree", "is_correct": True},
            {"text": "Chair", "is_correct": False},
            {"text": "Car", "is_correct": False}
        ]
    },
    {
        "text": "What makes the day bright?",
        "explanation": (
            "The Sun provides light and heat during the day, "
            "making it bright."
        ),
        "reference": "Solar System Basics",
        "points": 1,
        "answers": [
            {"text": "Moon", "is_correct": False},
            {"text": "Stars", "is_correct": False},
            {"text": "Sun", "is_correct": True},
            {"text": "Clouds", "is_correct": False}
        ]
    }
]