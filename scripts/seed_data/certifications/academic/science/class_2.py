"""Science Class 2 Certification"""

CERTIFICATION = {
    "name": "Science Class 2",
    "description": "Elementary science for 2nd grade students",
    "slug": "science-class-2",
    "level": "Class 2",
    "duration": 50,
    "questions_count": 25,
    "category_slug": "science",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What are the three states of matter?",
        "explanation": "Matter exists in three main states: solid, liquid, and gas.",
        "reference": "States of Matter",
        "points": 1,
        "answers": [
            {"text": "Solid, liquid, gas", "is_correct": True},
            {"text": "Hot, cold, warm", "is_correct": False},
            {"text": "Big, medium, small", "is_correct": False},
            {"text": "Heavy, light, medium", "is_correct": False}
        ]
    },
    {
        "text": "Which animal lays eggs?",
        "explanation": "Birds, reptiles, and some other animals lay eggs to reproduce.",
        "reference": "Animal Reproduction",
        "points": 1,
        "answers": [
            {"text": "Dog", "is_correct": False},
            {"text": "Cat", "is_correct": False},
            {"text": "Bird", "is_correct": True},
            {"text": "Horse", "is_correct": False}
        ]
    },
    {
        "text": "What do we use to see things that are far away?",
        "explanation": "A telescope is used to see distant objects clearly.",
        "reference": "Scientific Instruments",
        "points": 1,
        "answers": [
            {"text": "Microscope", "is_correct": False},
            {"text": "Telescope", "is_correct": True},
            {"text": "Mirror", "is_correct": False},
            {"text": "Glasses", "is_correct": False}
        ]
    }
]