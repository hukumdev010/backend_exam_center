"""Chemistry Class 11 Certification"""

CERTIFICATION = {
    "name": "Chemistry Class 11",
    "description": "Basic chemistry concepts for 11th grade students",
    "slug": "chemistry-class-11",
    "level": "Class 11",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "chemistry",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the atomic number of Carbon?",
        "explanation": "Carbon has 6 protons in its nucleus, so its atomic number is 6.",
        "reference": "Atomic Structure",
        "points": 1,
        "answers": [
            {"text": "4", "is_correct": False},
            {"text": "6", "is_correct": True},
            {"text": "8", "is_correct": False},
            {"text": "12", "is_correct": False}
        ]
    },
    {
        "text": "What is the chemical formula of water?",
        "explanation": "Water consists of 2 hydrogen atoms and 1 oxygen atom, forming H2O.",
        "reference": "Chemical Formulas",
        "points": 1,
        "answers": [
            {"text": "H2O", "is_correct": True},
            {"text": "HO2", "is_correct": False},
            {"text": "H2O2", "is_correct": False},
            {"text": "OH", "is_correct": False}
        ]
    },
    {
        "text": "Which of the following is a noble gas?",
        "explanation": "Noble gases are in Group 18 of the periodic table. Helium is a noble gas.",
        "reference": "Periodic Table",
        "points": 1,
        "answers": [
            {"text": "Oxygen", "is_correct": False},
            {"text": "Nitrogen", "is_correct": False},
            {"text": "Helium", "is_correct": True},
            {"text": "Hydrogen", "is_correct": False}
        ]
    },
    {
        "text": "What type of bond is formed between sodium and chlorine in NaCl?",
        "explanation": "Sodium transfers an electron to chlorine, forming an ionic bond.",
        "reference": "Chemical Bonding",
        "points": 1,
        "answers": [
            {"text": "Covalent bond", "is_correct": False},
            {"text": "Ionic bond", "is_correct": True},
            {"text": "Metallic bond", "is_correct": False},
            {"text": "Hydrogen bond", "is_correct": False}
        ]
    },
    {
        "text": "What is the pH of pure water?",
        "explanation": "Pure water is neutral with a pH of 7.",
        "reference": "Acids and Bases",
        "points": 1,
        "answers": [
            {"text": "0", "is_correct": False},
            {"text": "7", "is_correct": True},
            {"text": "14", "is_correct": False},
            {"text": "1", "is_correct": False}
        ]
    }
]