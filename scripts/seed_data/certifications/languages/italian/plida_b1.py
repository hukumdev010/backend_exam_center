"""PLIDA B1 - Intermediate Italian certificate for independent users"""

CERTIFICATION = {
    "name": "PLIDA B1",
    "description": "Intermediate Italian certificate for independent users",
    "slug": "plida-b1",
    "level": "B1",
    "duration": 170,
    "questions_count": 45,
    "category_slug": "italian",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "Se dovessi consigliare la tua città a un turista, cosa diresti?",
        "options": ["È bella", "Direi che offre storia, arte e ottima cucina", "Mi piace", "È grande"],
        "correct_answer": 1,
        "explanation": "This conditional question requires giving advice about your city to tourists."
    },
    {
        "question": "Cosa pensi dell'importanza di imparare le lingue straniere?",
        "options": ["Penso che sia fondamentale per aprire nuove opportunità", "È difficile", "Mi piace studiare", "È utile"],
        "correct_answer": 0,
        "explanation": "This question asks for an opinion about the importance of learning foreign languages."
    },
    {
        "question": "Come descriveresti la cucina italiana rispetto ad altre cucine?",
        "options": ["È buona", "È caratterizzata da ingredienti freschi e tradizioni regionali", "Mi piace cucinare", "È famosa"],
        "correct_answer": 1,
        "explanation": "This question requires comparing Italian cuisine with others."
    }
]