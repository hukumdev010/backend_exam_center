"""OPI Spanish - Spanish oral proficiency assessment for speaking skills evaluation"""

CERTIFICATION = {
    "name": "OPI Spanish (Oral Proficiency Interview)",
    "description": "Spanish oral proficiency assessment for speaking skills evaluation",
    "slug": "opi-spanish",
    "level": "A1-C2",
    "duration": 30,
    "questions_count": 1,
    "category_slug": "spanish",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "Describa su rutina diaria y sus actividades favoritas.",
        "options": ["Excelente fluidez", "Buena comunicación", "Comunicación básica", "Dificultades comunicativas"],
        "correct_answer": 0,
        "explanation": "La respuesta debe demostrar fluidez, precisión y riqueza léxica apropiada al nivel."
    }
]