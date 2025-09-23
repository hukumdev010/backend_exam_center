"""Anatomy & Physiology Advanced Certification"""

CERTIFICATION = {
    "name": "Anatomy & Physiology Advanced",
    "description": "Advanced human anatomy and complex physiological systems",
    "slug": "anatomy-physiology-advanced",
    "level": "Advanced",
    "duration": 90,
    "questions_count": 40,
    "category_slug": "anatomy_physiology",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the glomerular filtration rate?",
        "explanation": (
            "GFR measures how well the kidneys filter blood, "
            "normally about 120-130 mL/min in healthy adults."
        ),
        "reference": "Renal Physiology",
        "points": 1,
        "answers": [
            {"text": "Heart's pumping rate", "is_correct": False},
            {"text": "Kidney's blood filtering rate", "is_correct": True},
            {"text": "Liver's detox rate", "is_correct": False},
            {"text": "Lung's gas exchange rate", "is_correct": False}
        ]
    },
    {
        "text": "Which hormone regulates blood calcium levels?",
        "explanation": (
            "Parathyroid hormone (PTH) increases blood calcium by "
            "stimulating bone resorption and calcium absorption."
        ),
        "reference": "Endocrine System",
        "points": 1,
        "answers": [
            {"text": "Insulin", "is_correct": False},
            {"text": "Cortisol", "is_correct": False},
            {"text": "Parathyroid hormone", "is_correct": True},
            {"text": "Growth hormone", "is_correct": False}
        ]
    },
    {
        "text": "What is the Frank-Starling mechanism?",
        "explanation": (
            "The Frank-Starling mechanism describes how increased "
            "venous return leads to increased cardiac output."
        ),
        "reference": "Cardiac Physiology",
        "points": 1,
        "answers": [
            {"text": "Breathing regulation", "is_correct": False},
            {"text": "Heart's response to filling", "is_correct": True},
            {"text": "Blood pressure control", "is_correct": False},
            {"text": "Nerve conduction", "is_correct": False}
        ]
    },
    {
        "text": "Which cells produce myelin in the central nervous system?",
        "explanation": (
            "Oligodendrocytes produce myelin sheaths around axons "
            "in the central nervous system for faster conduction."
        ),
        "reference": "Neurophysiology",
        "points": 1,
        "answers": [
            {"text": "Neurons", "is_correct": False},
            {"text": "Astrocytes", "is_correct": False},
            {"text": "Oligodendrocytes", "is_correct": True},
            {"text": "Schwann cells", "is_correct": False}
        ]
    },
    {
        "text": "What is the primary buffer system in blood?",
        "explanation": (
            "The bicarbonate buffer system (HCO3-/H2CO3) is the "
            "primary buffer maintaining blood pH around 7.4."
        ),
        "reference": "Acid-Base Balance",
        "points": 1,
        "answers": [
            {"text": "Protein buffer", "is_correct": False},
            {"text": "Bicarbonate buffer", "is_correct": True},
            {"text": "Phosphate buffer", "is_correct": False},
            {"text": "Hemoglobin buffer", "is_correct": False}
        ]
    }
]