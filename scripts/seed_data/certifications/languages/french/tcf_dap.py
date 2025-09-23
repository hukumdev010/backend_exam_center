"""TCF DAP Certification"""

CERTIFICATION = {
    "name": "TCF DAP",
    "description": "French test for university admission procedures in France",
    "slug": "tcf-dap",
    "level": "B2-C2",
    "duration": 180,
    "questions_count": 110,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does DAP stand for in TCF DAP?",
        "explanation": "DAP stands for Demande d'Admission Préalable, the preliminary admission request for French universities.",
        "reference": "TCF DAP University Admission",
        "points": 1,
        "answers": [
            {"text": "Diplôme d'Aptitude Professionnelle", "is_correct": False},
            {"text": "Demande d'Admission Préalable", "is_correct": True},
            {"text": "Diplôme d'Accès Professionnel", "is_correct": False},
            {"text": "Document d'Apprentissage Pratique", "is_correct": False},
        ],
    }
]