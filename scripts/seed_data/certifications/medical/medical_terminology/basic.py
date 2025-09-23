"""Medical Terminology Basics Certification"""

CERTIFICATION = {
    "name": "Medical Terminology Basics",
    "description": "Fundamental medical vocabulary and word parts",
    "slug": "medical-terminology-basics",
    "level": "Beginner",
    "duration": 45,
    "questions_count": 30,
    "category_slug": "medical_terminology",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does the prefix 'hyper-' mean?",
        "explanation": (
            "The prefix 'hyper-' means excessive, above normal, "
            "or increased, as in hypertension (high blood pressure)."
        ),
        "reference": "Medical Prefixes",
        "points": 1,
        "answers": [
            {"text": "Below normal", "is_correct": False},
            {"text": "Above normal", "is_correct": True},
            {"text": "Around or about", "is_correct": False},
            {"text": "Through or across", "is_correct": False}
        ]
    },
    {
        "text": "What does the suffix '-itis' mean?",
        "explanation": (
            "The suffix '-itis' means inflammation, as in "
            "arthritis (joint inflammation) or bronchitis."
        ),
        "reference": "Medical Suffixes",
        "points": 1,
        "answers": [
            {"text": "Pain", "is_correct": False},
            {"text": "Inflammation", "is_correct": True},
            {"text": "Disease", "is_correct": False},
            {"text": "Enlargement", "is_correct": False}
        ]
    },
    {
        "text": "What does 'cardio-' refer to?",
        "explanation": (
            "The root 'cardio-' refers to the heart, as in "
            "cardiology (study of the heart) or cardiac arrest."
        ),
        "reference": "Medical Roots",
        "points": 1,
        "answers": [
            {"text": "Lungs", "is_correct": False},
            {"text": "Heart", "is_correct": True},
            {"text": "Kidneys", "is_correct": False},
            {"text": "Brain", "is_correct": False}
        ]
    },
    {
        "text": "What does 'bradycardia' mean?",
        "explanation": (
            "Bradycardia means slow heart rate, typically "
            "below 60 beats per minute in adults."
        ),
        "reference": "Cardiovascular Terms",
        "points": 1,
        "answers": [
            {"text": "Fast heart rate", "is_correct": False},
            {"text": "Slow heart rate", "is_correct": True},
            {"text": "Irregular heart rhythm", "is_correct": False},
            {"text": "Heart enlargement", "is_correct": False}
        ]
    },
    {
        "text": "What does the suffix '-ectomy' mean?",
        "explanation": (
            "The suffix '-ectomy' means surgical removal, "
            "as in appendectomy (removal of the appendix)."
        ),
        "reference": "Surgical Terms",
        "points": 1,
        "answers": [
            {"text": "Surgical creation of opening", "is_correct": False},
            {"text": "Surgical removal", "is_correct": True},
            {"text": "Surgical repair", "is_correct": False},
            {"text": "Visual examination", "is_correct": False}
        ]
    }
]