"""Art & Design Fundamentals Certification"""

CERTIFICATION = {
    "name": "Art & Design Fundamentals",
    "description": "Basic art history and design principles",
    "slug": "art-design-fundamentals",
    "level": "Fundamentals",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "art_design",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What are the primary colors?",
        "explanation": (
            "The primary colors are red, blue, and yellow. These colors "
            "cannot be created by mixing other colors."
        ),
        "reference": "Color Theory",
        "points": 1,
        "answers": [
            {"text": "Red, green, blue", "is_correct": False},
            {"text": "Red, blue, yellow", "is_correct": True},
            {"text": "Blue, yellow, orange", "is_correct": False},
            {"text": "Red, purple, green", "is_correct": False}
        ]
    },
    {
        "text": "Who painted the Mona Lisa?",
        "explanation": (
            "Leonardo da Vinci painted the Mona Lisa during the "
            "Italian Renaissance (1503-1519)."
        ),
        "reference": "Art History",
        "points": 1,
        "answers": [
            {"text": "Michelangelo", "is_correct": False},
            {"text": "Leonardo da Vinci", "is_correct": True},
            {"text": "Raphael", "is_correct": False},
            {"text": "Picasso", "is_correct": False}
        ]
    },
    {
        "text": "What is perspective in art?",
        "explanation": (
            "Perspective is a technique used to create the illusion "
            "of depth and three-dimensional space on a flat surface."
        ),
        "reference": "Art Techniques",
        "points": 1,
        "answers": [
            {"text": "Use of bright colors", "is_correct": False},
            {"text": "Creating illusion of depth", "is_correct": True},
            {"text": "Painting outdoors", "is_correct": False},
            {"text": "Abstract representation", "is_correct": False}
        ]
    },
    {
        "text": "What is the rule of thirds in composition?",
        "explanation": (
            "The rule of thirds divides an image into nine equal parts "
            "with two horizontal and two vertical lines for better composition."
        ),
        "reference": "Design Principles",
        "points": 1,
        "answers": [
            {"text": "Dividing image into 3 parts", "is_correct": False},
            {"text": "Grid of 9 equal sections", "is_correct": True},
            {"text": "Using 3 colors only", "is_correct": False},
            {"text": "Three main subjects", "is_correct": False}
        ]
    },
    {
        "text": "What is a still life painting?",
        "explanation": (
            "A still life is a painting or drawing of inanimate objects "
            "like fruits, flowers, or everyday items."
        ),
        "reference": "Art Genres",
        "points": 1,
        "answers": [
            {"text": "Painting of people", "is_correct": False},
            {"text": "Painting of landscapes", "is_correct": False},
            {"text": "Painting of inanimate objects", "is_correct": True},
            {"text": "Painting of animals", "is_correct": False}
        ]
    }
]