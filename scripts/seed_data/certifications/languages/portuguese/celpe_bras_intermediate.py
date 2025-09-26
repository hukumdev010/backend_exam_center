"""CELPE-Bras Intermediate - Brazilian Portuguese proficiency certificate"""

CERTIFICATION = {
    "name": "CELPE-Bras Intermediate",
    "description": "Brazilian Portuguese proficiency certificate - "
                   "Intermediate level",
    "slug": "celpe-bras-intermediate",
    "level": "B1-B2",
    "duration": 180,
    "questions_count": 45,
    "category_slug": "portuguese",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "Qual é a forma correta do verbo 'estar' na primeira "
                    "pessoa do singular no presente?",
        "options": ["estou", "está", "estamos", "estão"],
        "correct_answer": 0,
        "explanation": "'Estou' é a conjugação correta do verbo 'estar' "
                       "na primeira pessoa do singular do presente do "
                       "indicativo."
    },
    {
        "question": "Complete a frase: 'Eu ___ brasileiro.'",
        "options": ["sou", "estou", "tenho", "vou"],
        "correct_answer": 0,
        "explanation": "Para nacionalidade, usamos o verbo 'ser'. 'Sou' é "
                       "a primeira pessoa do singular do presente do "
                       "indicativo."
    },
    {
        "question": "Qual preposição deve ser usada na frase: "
                    "'Vou ___ escola'?",
        "options": ["para", "na", "à", "pela"],
        "correct_answer": 2,
        "explanation": "Usamos 'à' (preposição 'a' + artigo 'a') quando há "
                       "movimento em direção a um lugar feminino específico."
    }
]