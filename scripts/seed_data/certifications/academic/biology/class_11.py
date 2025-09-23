"""Biology Class 11 Certification"""

CERTIFICATION = {
    "name": "Biology Class 11",
    "description": "Basic biology concepts for 11th grade students",
    "slug": "biology-class-11",
    "level": "Class 11",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "biology",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the basic unit of life?",
        "explanation": (
            "The cell is the smallest structural and functional unit "
            "of all living organisms."
        ),
        "reference": "Cell Biology",
        "points": 1,
        "answers": [
            {"text": "Tissue", "is_correct": False},
            {"text": "Cell", "is_correct": True},
            {"text": "Organ", "is_correct": False},
            {"text": "Organism", "is_correct": False}
        ]
    },
    {
        "text": "Which organelle is known as the powerhouse of the cell?",
        "explanation": (
            "Mitochondria produce ATP through cellular respiration, "
            "providing energy for cellular processes."
        ),
        "reference": "Cell Organelles",
        "points": 1,
        "answers": [
            {"text": "Nucleus", "is_correct": False},
            {"text": "Ribosome", "is_correct": False},
            {"text": "Mitochondria", "is_correct": True},
            {"text": "Endoplasmic reticulum", "is_correct": False}
        ]
    },
    {
        "text": "What is photosynthesis?",
        "explanation": (
            "Photosynthesis is the process by which plants convert "
            "sunlight, carbon dioxide, and water into glucose and oxygen."
        ),
        "reference": "Plant Physiology",
        "points": 1,
        "answers": [
            {"text": "Breaking down glucose", "is_correct": False},
            {"text": "Making food using sunlight", "is_correct": True},
            {"text": "Cell division", "is_correct": False},
            {"text": "Protein synthesis", "is_correct": False}
        ]
    },
    {
        "text": "Which kingdom do bacteria belong to?",
        "explanation": (
            "Bacteria are prokaryotic organisms that belong to "
            "the kingdom Monera."
        ),
        "reference": "Classification",
        "points": 1,
        "answers": [
            {"text": "Plantae", "is_correct": False},
            {"text": "Animalia", "is_correct": False},
            {"text": "Fungi", "is_correct": False},
            {"text": "Monera", "is_correct": True}
        ]
    },
    {
        "text": "What is the function of DNA?",
        "explanation": (
            "DNA stores genetic information and passes it from "
            "one generation to the next."
        ),
        "reference": "Genetics",
        "points": 1,
        "answers": [
            {"text": "Energy production", "is_correct": False},
            {"text": "Storing genetic information", "is_correct": True},
            {"text": "Protein digestion", "is_correct": False},
            {"text": "Water transport", "is_correct": False}
        ]
    }
]