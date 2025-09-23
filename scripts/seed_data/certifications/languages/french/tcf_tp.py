"""TCF TP (Tout Public) Certification"""

CERTIFICATION = {
    "name": "TCF TP (Tout Public)",
    "description": "General French proficiency test for personal, academic or professional use",
    "slug": "tcf-tp",
    "level": "A1-C2",
    "duration": 90,
    "questions_count": 91,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does TCF TP stand for?",
        "explanation": "TCF TP stands for Test de connaissance du français Tout Public, a general French proficiency test for all audiences.",
        "reference": "TCF TP Overview",
        "points": 1,
        "answers": [
            {"text": "Test de Culture Française", "is_correct": False},
            {"text": "Test de connaissance du français Tout Public", "is_correct": True},
            {"text": "Test de Compétence Française", "is_correct": False},
            {"text": "Test de Communication Française", "is_correct": False},
        ],
    }
]