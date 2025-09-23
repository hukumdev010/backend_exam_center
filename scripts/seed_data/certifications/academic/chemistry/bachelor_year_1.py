"""Chemistry Bachelor Year 1 Certification"""

CERTIFICATION = {
    "name": "Chemistry Bachelor Year 1",
    "description": "Fundamental chemistry for first-year bachelor students",
    "slug": "chemistry-bachelor-year-1",
    "level": "Bachelor Year 1",
    "duration": 90,
    "questions_count": 40,
    "category_slug": "chemistry",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is Avogadro's number?",
        "explanation": (
            "Avogadro's number is 6.022 × 10²³, representing the number "
            "of particles in one mole."
        ),
        "reference": "Atomic Theory",
        "points": 1,
        "answers": [
            {"text": "6.022 × 10²³", "is_correct": True},
            {"text": "6.022 × 10²²", "is_correct": False},
            {"text": "6.022 × 10²⁴", "is_correct": False},
            {"text": "3.14 × 10²³", "is_correct": False}
        ]
    },
    {
        "text": "Which quantum number describes electron spin?",
        "explanation": (
            "The spin quantum number (ms) describes the intrinsic "
            "angular momentum of electrons."
        ),
        "reference": "Quantum Chemistry",
        "points": 1,
        "answers": [
            {"text": "n", "is_correct": False},
            {"text": "l", "is_correct": False},
            {"text": "ml", "is_correct": False},
            {"text": "ms", "is_correct": True}
        ]
    },
    {
        "text": "What is the molecular geometry of SF6?",
        "explanation": (
            "SF6 has 6 bonding pairs and no lone pairs, "
            "resulting in octahedral geometry."
        ),
        "reference": "Molecular Geometry",
        "points": 1,
        "answers": [
            {"text": "Tetrahedral", "is_correct": False},
            {"text": "Octahedral", "is_correct": True},
            {"text": "Trigonal bipyramidal", "is_correct": False},
            {"text": "Square planar", "is_correct": False}
        ]
    },
    {
        "text": "What is the standard state of enthalpy formation for O2(g)?",
        "explanation": (
            "The standard enthalpy of formation for elements "
            "in their standard state is zero."
        ),
        "reference": "Thermodynamics",
        "points": 1,
        "answers": [
            {"text": "0 kJ/mol", "is_correct": True},
            {"text": "285 kJ/mol", "is_correct": False},
            {"text": "-285 kJ/mol", "is_correct": False},
            {"text": "498 kJ/mol", "is_correct": False}
        ]
    },
    {
        "text": "Which type of isomerism is shown by [Co(NH3)4Cl2]+?",
        "explanation": (
            "This complex can have cis and trans arrangements "
            "of chloride ligands, showing geometrical isomerism."
        ),
        "reference": "Coordination Chemistry",
        "points": 1,
        "answers": [
            {"text": "Optical isomerism", "is_correct": False},
            {"text": "Geometrical isomerism", "is_correct": True},
            {"text": "Linkage isomerism", "is_correct": False},
            {"text": "Ionization isomerism", "is_correct": False}
        ]
    }
]