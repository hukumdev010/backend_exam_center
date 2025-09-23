"""Physics Bachelor Year 2 Certification"""

CERTIFICATION = {
    "name": "Physics Bachelor Year 2",
    "description": "Second year university physics",
    "slug": "physics-bachelor-year-2",
    "level": "Bachelor Year 2",
    "duration": 180,
    "questions_count": 75,
    "category_slug": "physics",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is Schrödinger's equation?",
        "explanation": "Schrödinger's equation is a fundamental equation in quantum mechanics that describes how the quantum state of a physical system changes with time.",
        "reference": "Quantum Mechanics",
        "points": 1,
        "answers": [
            {"text": "iℏ∂ψ/∂t = Ĥψ", "is_correct": True},
            {"text": "E = mc²", "is_correct": False},
            {"text": "F = ma", "is_correct": False},
            {"text": "pV = nRT", "is_correct": False}
        ]
    },
    {
        "text": "What is the uncertainty principle?",
        "explanation": "Heisenberg's uncertainty principle states that the position and momentum of a particle cannot be simultaneously measured with absolute precision.",
        "reference": "Quantum Mechanics",
        "points": 1,
        "answers": [
            {"text": "ΔxΔp ≥ ℏ/2", "is_correct": True},
            {"text": "ΔE = mc²", "is_correct": False},
            {"text": "Δx = 0", "is_correct": False},
            {"text": "Δp = 0", "is_correct": False}
        ]
    },
    {
        "text": "What is Maxwell's displacement current?",
        "explanation": "Maxwell's displacement current is a quantity proportional to the rate of change of electric field, introduced to make Ampere's law consistent.",
        "reference": "Electromagnetic Theory",
        "points": 1,
        "answers": [
            {"text": "ε₀∂E/∂t", "is_correct": True},
            {"text": "μ₀∂B/∂t", "is_correct": False},
            {"text": "∇×E", "is_correct": False},
            {"text": "∇⋅B", "is_correct": False}
        ]
    }
]