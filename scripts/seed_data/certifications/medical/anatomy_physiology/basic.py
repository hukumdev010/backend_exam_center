"""Anatomy & Physiology Basic Certification"""

CERTIFICATION = {
    "name": "Anatomy & Physiology Basic",
    "description": "Basic human anatomy and physiological processes",
    "slug": "anatomy-physiology-basic",
    "level": "Basic",
    "duration": 75,
    "questions_count": 30,
    "category_slug": "anatomy_physiology",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "How many bones are in the adult human body?",
        "explanation": (
            "The adult human body has 206 bones. Babies are born "
            "with about 270 bones, but many fuse as they grow."
        ),
        "reference": "Skeletal System",
        "points": 1,
        "answers": [
            {"text": "195", "is_correct": False},
            {"text": "206", "is_correct": True},
            {"text": "220", "is_correct": False},
            {"text": "180", "is_correct": False}
        ]
    },
    {
        "text": "What is the largest organ in the human body?",
        "explanation": (
            "The skin is the largest organ in the human body, "
            "covering the entire surface and protecting internal organs."
        ),
        "reference": "Integumentary System",
        "points": 1,
        "answers": [
            {"text": "Liver", "is_correct": False},
            {"text": "Lungs", "is_correct": False},
            {"text": "Skin", "is_correct": True},
            {"text": "Brain", "is_correct": False}
        ]
    },
    {
        "text": "Which chamber of the heart pumps blood to the lungs?",
        "explanation": (
            "The right ventricle pumps deoxygenated blood to the "
            "lungs through the pulmonary artery for oxygenation."
        ),
        "reference": "Cardiovascular System",
        "points": 1,
        "answers": [
            {"text": "Left atrium", "is_correct": False},
            {"text": "Right atrium", "is_correct": False},
            {"text": "Left ventricle", "is_correct": False},
            {"text": "Right ventricle", "is_correct": True}
        ]
    },
    {
        "text": "What is the function of red blood cells?",
        "explanation": (
            "Red blood cells (erythrocytes) carry oxygen from the "
            "lungs to body tissues and carbon dioxide back to the lungs."
        ),
        "reference": "Blood System",
        "points": 1,
        "answers": [
            {"text": "Fight infections", "is_correct": False},
            {"text": "Carry oxygen and carbon dioxide", "is_correct": True},
            {"text": "Clot blood", "is_correct": False},
            {"text": "Produce hormones", "is_correct": False}
        ]
    },
    {
        "text": "Which part of the brain controls balance and coordination?",
        "explanation": (
            "The cerebellum is responsible for balance, coordination, "
            "and fine motor control."
        ),
        "reference": "Nervous System",
        "points": 1,
        "answers": [
            {"text": "Cerebrum", "is_correct": False},
            {"text": "Cerebellum", "is_correct": True},
            {"text": "Brain stem", "is_correct": False},
            {"text": "Medulla", "is_correct": False}
        ]
    }
]