"""TestDaF Certification"""

CERTIFICATION = {
    "name": "TestDaF",
    "description": "German test for university admission and academic purposes",
    "slug": "testdaf",
    "level": "B2-C1",
    "duration": 185,
    "questions_count": 70,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does TestDaF stand for?",
        "explanation": "TestDaF stands for Test Deutsch als Fremdsprache, the German language test for university admission.",
        "reference": "TestDaF Overview",
        "points": 1,
        "answers": [
            {"text": "Test Deutsch als Fremdsprache", "is_correct": True},
            {"text": "Test Deutsche Akademie", "is_correct": False},
            {"text": "Test Deutsch für Ausländer", "is_correct": False},
            {"text": "Test Deutsche Fakultät", "is_correct": False},
        ],
    },
    {
        "text": "What is TestDaF primarily used for?",
        "explanation": "TestDaF is primarily used for university admission in Germany, proving German language skills for academic study.",
        "reference": "TestDaF University Admission",
        "points": 1,
        "answers": [
            {"text": "Business certification", "is_correct": False},
            {"text": "University admission", "is_correct": True},
            {"text": "Tourism purposes", "is_correct": False},
            {"text": "Immigration only", "is_correct": False},
        ],
    }
]