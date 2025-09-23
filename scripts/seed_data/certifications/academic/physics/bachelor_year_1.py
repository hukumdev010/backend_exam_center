"""Physics Bachelor Year 1 Certification"""

CERTIFICATION = {
    "name": "Physics Bachelor Year 1",
    "description": "First year university physics fundamentals",
    "slug": "physics-bachelor-year-1",
    "level": "Bachelor Year 1",
    "duration": 180,
    "questions_count": 70,
    "category_slug": "physics",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the principle of superposition?",
        "explanation": (
            "The principle of superposition states that when two or more waves overlap, "
            "the resultant displacement is the algebraic sum of individual displacements."
        ),
        "reference": "Wave Physics",
        "points": 1,
        "answers": [
            {"text": "Waves cancel each other", "is_correct": False},
            {"text": "Waves add algebraically", "is_correct": True},
            {"text": "Waves multiply", "is_correct": False},
            {"text": "Waves remain unchanged", "is_correct": False}
        ]
    },
    {
        "text": "What is Gauss's law in electrostatics?",
        "explanation": "Gauss's law states that the electric flux through a closed surface is proportional to the charge enclosed by that surface.",
        "reference": "Electrostatics",
        "points": 1,
        "answers": [
            {"text": "∮E⋅dA = Q/ε₀", "is_correct": True},
            {"text": "∮B⋅dl = μ₀I", "is_correct": False},
            {"text": "∇×E = -∂B/∂t", "is_correct": False},
            {"text": "F = qE", "is_correct": False}
        ]
    },
    {
        "text": "What is the Stefan-Boltzmann law?",
        "explanation": "The Stefan-Boltzmann law states that the total energy radiated per unit surface area of a black body is proportional to the fourth power of its temperature.",
        "reference": "Thermal Physics",
        "points": 1,
        "answers": [
            {"text": "Energy ∝ T⁴", "is_correct": True},
            {"text": "Energy ∝ T²", "is_correct": False},
            {"text": "Energy ∝ T", "is_correct": False},
            {"text": "Energy ∝ 1/T", "is_correct": False}
        ]
    }
]