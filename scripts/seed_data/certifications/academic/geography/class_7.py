"""Geography Class 7 Certification"""

CERTIFICATION = {
    "name": "Geography Class 7",
    "description": "Physical and world geography for 7th grade students",
    "slug": "geography-class-7",
    "level": "Class 7",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "geography",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the largest continent on Earth?",
        "explanation": (
            "Asia is the largest continent, covering about 30% "
            "of Earth's land area."
        ),
        "reference": "World Geography",
        "points": 1,
        "answers": [
            {"text": "Africa", "is_correct": False},
            {"text": "Asia", "is_correct": True},
            {"text": "North America", "is_correct": False},
            {"text": "Europe", "is_correct": False}
        ]
    },
    {
        "text": "Which river is the longest in the world?",
        "explanation": (
            "The Nile River in Africa is the longest river in the world, "
            "flowing over 6,600 kilometers."
        ),
        "reference": "Physical Geography",
        "points": 1,
        "answers": [
            {"text": "Amazon River", "is_correct": False},
            {"text": "Nile River", "is_correct": True},
            {"text": "Mississippi River", "is_correct": False},
            {"text": "Yangtze River", "is_correct": False}
        ]
    },
    {
        "text": "What is the capital of Australia?",
        "explanation": (
            "Canberra is the capital city of Australia, though "
            "Sydney and Melbourne are larger cities."
        ),
        "reference": "World Capitals",
        "points": 1,
        "answers": [
            {"text": "Sydney", "is_correct": False},
            {"text": "Melbourne", "is_correct": False},
            {"text": "Canberra", "is_correct": True},
            {"text": "Perth", "is_correct": False}
        ]
    },
    {
        "text": "Which mountain range contains Mount Everest?",
        "explanation": (
            "Mount Everest, the world's highest peak, "
            "is located in the Himalayas."
        ),
        "reference": "Physical Geography",
        "points": 1,
        "answers": [
            {"text": "Rocky Mountains", "is_correct": False},
            {"text": "Andes Mountains", "is_correct": False},
            {"text": "Himalayas", "is_correct": True},
            {"text": "Alps", "is_correct": False}
        ]
    },
    {
        "text": "What causes the seasons on Earth?",
        "explanation": (
            "Earth's tilted axis causes different parts to receive "
            "varying amounts of sunlight throughout the year."
        ),
        "reference": "Earth Science",
        "points": 1,
        "answers": [
            {"text": "Distance from the sun", "is_correct": False},
            {"text": "Earth's tilted axis", "is_correct": True},
            {"text": "Moon's gravity", "is_correct": False},
            {"text": "Solar flares", "is_correct": False}
        ]
    }
]