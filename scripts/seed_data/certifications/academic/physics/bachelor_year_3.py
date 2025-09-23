"""Physics Bachelor Year 3 Certification"""

CERTIFICATION = {
    "name": "Physics Bachelor Year 3",
    "description": "Third year advanced university physics",
    "slug": "physics-bachelor-year-3",
    "level": "Bachelor Year 3",
    "duration": 200,
    "questions_count": 80,
    "category_slug": "physics",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the Pauli exclusion principle?",
        "explanation": "The Pauli exclusion principle states that no two fermions can occupy the same quantum state simultaneously.",
        "reference": "Advanced Quantum Mechanics",
        "points": 1,
        "answers": [
            {"text": "No two fermions in same state", "is_correct": True},
            {"text": "No two bosons in same state", "is_correct": False},
            {"text": "All particles in same state", "is_correct": False},
            {"text": "Energy is conserved", "is_correct": False}
        ]
    },
    {
        "text": "What is renormalization in quantum field theory?",
        "explanation": "Renormalization is a technique to deal with infinities that arise in quantum field theory calculations by redefining parameters.",
        "reference": "Quantum Field Theory",
        "points": 1,
        "answers": [
            {"text": "Removing infinities", "is_correct": True},
            {"text": "Adding infinities", "is_correct": False},
            {"text": "Normalizing waves", "is_correct": False},
            {"text": "Quantizing fields", "is_correct": False}
        ]
    },
    {
        "text": "What is the standard model of particle physics?",
        "explanation": "The standard model describes the fundamental particles and three of the four fundamental forces of nature (excluding gravity).",
        "reference": "Particle Physics",
        "points": 1,
        "answers": [
            {"text": "Theory of fundamental particles and forces", "is_correct": True},
            {"text": "Theory of gravity only", "is_correct": False},
            {"text": "Theory of atoms only", "is_correct": False},
            {"text": "Theory of nuclei only", "is_correct": False}
        ]
    }
]