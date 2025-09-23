"""CELI 1 - Basic Italian proficiency certificate for elementary level"""

CERTIFICATION = {
    "name": "CELI 1",
    "description": "Basic Italian proficiency certificate for elementary level",
    "slug": "celi-1",
    "level": "A2",
    "duration": 120,
    "questions_count": 42,
    "category_slug": "italian",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "Che cosa hai fatto ieri sera?",
        "options": ["Ho guardato la televisione", "Sono alto", "Mi piace il blu", "È mercoledì"],
        "correct_answer": 0,
        "explanation": "The question asks what you did last night. The correct answer is 'Ho guardato la televisione' (I watched television)."
    },
    {
        "question": "Con chi abiti?",
        "options": ["Ho fame", "Abito con i miei genitori", "È caldo", "Mi piace cucinare"],
        "correct_answer": 1,
        "explanation": "'Con chi abiti?' means 'Who do you live with?' The correct answer is 'Abito con i miei genitori' (I live with my parents)."
    },
    {
        "question": "Dove lavori?",
        "options": ["Lavoro in un ufficio", "Ho vent'anni", "Mi piace la musica", "È difficile"],
        "correct_answer": 0,
        "explanation": "'Dove lavori?' means 'Where do you work?' The correct answer is 'Lavoro in un ufficio' (I work in an office)."
    }
]