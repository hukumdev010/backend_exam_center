"""CILS A1 - Basic Italian language skills for elementary communication situations"""

CERTIFICATION = {
    "name": "CILS A1",
    "description": "Basic Italian language skills for elementary communication situations",
    "slug": "cils-a1",
    "level": "A1",
    "duration": 95,
    "questions_count": 35,
    "category_slug": "italian",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "Come ti chiami?",
        "options": ["Mi piace la pizza", "Sono di Roma", "Mi chiamo Marco", "Ho vent'anni"],
        "correct_answer": 2,
        "explanation": "'Come ti chiami?' means 'What is your name?' The correct response is 'Mi chiamo Marco' (My name is Marco)."
    },
    {
        "question": "Dove abiti?",
        "options": ["Abito a Milano", "Sono studente", "Mi piace leggere", "Ho fame"],
        "correct_answer": 0,
        "explanation": "'Dove abiti?' means 'Where do you live?' The correct answer is 'Abito a Milano' (I live in Milan)."
    },
    {
        "question": "Che ore sono?",
        "options": ["Sono le tre", "È martedì", "Fa caldo", "È blu"],
        "correct_answer": 0,
        "explanation": "'Che ore sono?' means 'What time is it?' The correct answer is 'Sono le tre' (It's three o'clock)."
    }
]