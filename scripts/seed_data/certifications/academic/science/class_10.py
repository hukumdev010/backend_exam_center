"""Science Class 10 Certification"""

CERTIFICATION = {
    "name": "Science Class 10",
    "description": "Comprehensive high school science",
    "slug": "science-class-10",
    "level": "Class 10",
    "duration": 120,
    "questions_count": 60,
    "category_slug": "science",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the process of cell division called?",
        "explanation": "Mitosis is the process by which a single cell divides to form two identical daughter cells.",
        "reference": "Cell Division",
        "points": 1,
        "answers": [
            {"text": "Mitosis", "is_correct": True},
            {"text": "Meiosis", "is_correct": False},
            {"text": "Photosynthesis", "is_correct": False},
            {"text": "Respiration", "is_correct": False}
        ]
    },
    {
        "text": "Which acid is present in our stomach?",
        "explanation": "Hydrochloric acid (HCl) is produced by the stomach to help digest food.",
        "reference": "Human Digestive System",
        "points": 1,
        "answers": [
            {"text": "Sulfuric acid", "is_correct": False},
            {"text": "Nitric acid", "is_correct": False},
            {"text": "Hydrochloric acid", "is_correct": True},
            {"text": "Acetic acid", "is_correct": False}
        ]
    },
    {
        "text": "What is the unit of electric current?",
        "explanation": "The ampere (A) is the SI unit for measuring electric current.",
        "reference": "Electrical Units",
        "points": 1,
        "answers": [
            {"text": "Volt", "is_correct": False},
            {"text": "Watt", "is_correct": False},
            {"text": "Ampere", "is_correct": True},
            {"text": "Ohm", "is_correct": False}
        ]
    }
]