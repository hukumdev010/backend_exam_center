"""Radiology Basics Certification"""

CERTIFICATION = {
    "name": "Radiology Basics",
    "description": "Fundamentals of medical imaging and radiation safety",
    "slug": "radiology-basics",
    "level": "Beginner",
    "duration": 45,
    "questions_count": 20,
    "category_slug": "radiology",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does X-ray imaging primarily show?",
        "explanation": (
            "X-rays primarily show dense structures like bones "
            "and can detect fractures, dislocations, and bone diseases."
        ),
        "reference": "X-ray Imaging",
        "points": 1,
        "answers": [
            {"text": "Soft tissues only", "is_correct": False},
            {"text": "Bones and dense structures", "is_correct": True},
            {"text": "Blood flow", "is_correct": False},
            {"text": "Brain activity", "is_correct": False}
        ]
    },
    {
        "text": "What does CT stand for?",
        "explanation": (
            "CT stands for Computed Tomography, which uses "
            "X-rays to create cross-sectional images of the body."
        ),
        "reference": "CT Imaging",
        "points": 1,
        "answers": [
            {"text": "Cardiac Testing", "is_correct": False},
            {"text": "Computed Tomography", "is_correct": True},
            {"text": "Cerebral Tracking", "is_correct": False},
            {"text": "Clinical Trial", "is_correct": False}
        ]
    },
    {
        "text": "What is MRI best used for?",
        "explanation": (
            "MRI (Magnetic Resonance Imaging) is best for imaging "
            "soft tissues like brain, muscles, and organs."
        ),
        "reference": "MRI Imaging",
        "points": 1,
        "answers": [
            {"text": "Bone fractures only", "is_correct": False},
            {"text": "Soft tissue imaging", "is_correct": True},
            {"text": "Lung diseases only", "is_correct": False},
            {"text": "Blood pressure measurement", "is_correct": False}
        ]
    },
    {
        "text": "What is contrast material used for?",
        "explanation": (
            "Contrast material enhances visibility of specific "
            "structures or abnormalities in medical imaging."
        ),
        "reference": "Contrast Imaging",
        "points": 1,
        "answers": [
            {"text": "Pain relief during scans", "is_correct": False},
            {"text": "Enhance image visibility", "is_correct": True},
            {"text": "Reduce radiation exposure", "is_correct": False},
            {"text": "Speed up scanning process", "is_correct": False}
        ]
    },
    {
        "text": "What is the ALARA principle?",
        "explanation": (
            "ALARA stands for 'As Low As Reasonably Achievable', "
            "the principle of minimizing radiation exposure."
        ),
        "reference": "Radiation Safety",
        "points": 1,
        "answers": [
            {"text": "Always use maximum radiation", "is_correct": False},
            {"text": "Minimize radiation exposure", "is_correct": True},
            {"text": "Avoid all radiation", "is_correct": False},
            {"text": "Use radiation for all patients", "is_correct": False}
        ]
    }
]