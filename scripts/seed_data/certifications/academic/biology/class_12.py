"""Biology Class 12 Certification"""

CERTIFICATION = {
    "name": "Biology Class 12",
    "description": "Advanced biology concepts for 12th grade students",
    "slug": "biology-class-12",
    "level": "Class 12",
    "duration": 75,
    "questions_count": 30,
    "category_slug": "biology",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the process of cell division that produces gametes?",
        "explanation": (
            "Meiosis is the type of cell division that produces "
            "reproductive cells (gametes) with half the chromosome number."
        ),
        "reference": "Reproduction",
        "points": 1,
        "answers": [
            {"text": "Mitosis", "is_correct": False},
            {"text": "Meiosis", "is_correct": True},
            {"text": "Binary fission", "is_correct": False},
            {"text": "Budding", "is_correct": False}
        ]
    },
    {
        "text": "Which blood group is considered the universal donor?",
        "explanation": (
            "O negative blood lacks A, B, and Rh antigens, "
            "making it compatible with all blood types."
        ),
        "reference": "Human Physiology",
        "points": 1,
        "answers": [
            {"text": "A positive", "is_correct": False},
            {"text": "B negative", "is_correct": False},
            {"text": "AB positive", "is_correct": False},
            {"text": "O negative", "is_correct": True}
        ]
    },
    {
        "text": "What is the role of insulin in the body?",
        "explanation": (
            "Insulin regulates blood glucose levels by facilitating "
            "glucose uptake into cells."
        ),
        "reference": "Endocrine System",
        "points": 1,
        "answers": [
            {"text": "Regulates blood pressure", "is_correct": False},
            {"text": "Controls blood sugar", "is_correct": True},
            {"text": "Produces antibodies", "is_correct": False},
            {"text": "Breaks down proteins", "is_correct": False}
        ]
    },
    {
        "text": "Which law explains the independent assortment of genes?",
        "explanation": (
            "Mendel's second law states that genes for different "
            "traits are inherited independently."
        ),
        "reference": "Genetics",
        "points": 1,
        "answers": [
            {"text": "Law of Dominance", "is_correct": False},
            {"text": "Law of Segregation", "is_correct": False},
            {"text": "Law of Independent Assortment", "is_correct": True},
            {"text": "Hardy-Weinberg Law", "is_correct": False}
        ]
    },
    {
        "text": "What is the function of the nephron in kidneys?",
        "explanation": (
            "Nephrons filter blood, reabsorb useful substances, "
            "and produce urine for waste elimination."
        ),
        "reference": "Excretory System",
        "points": 1,
        "answers": [
            {"text": "Oxygen transport", "is_correct": False},
            {"text": "Blood filtering", "is_correct": True},
            {"text": "Hormone production", "is_correct": False},
            {"text": "Digestion", "is_correct": False}
        ]
    }
]