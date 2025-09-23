"""IELTS Academic Certification"""

CERTIFICATION = {
    "name": "IELTS Academic",
    "description": "International English Language Testing System for academic purposes - university admissions and professional registration",
    "slug": "ielts-academic",
    "level": "B1-C2",
    "duration": 165,
    "questions_count": 120,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "In IELTS Academic Writing Task 1, what type of visual information might you be asked to describe?",
        "explanation": "IELTS Academic Writing Task 1 requires you to describe visual information such as graphs, charts, tables, or diagrams in at least 150 words.",
        "reference": "IELTS Academic Writing Task 1 Format",
        "points": 1,
        "answers": [
            {"text": "Personal opinions and experiences", "is_correct": False},
            {"text": "Charts, graphs, tables, or diagrams", "is_correct": True},
            {"text": "Creative stories and narratives", "is_correct": False},
            {"text": "Business correspondence", "is_correct": False},
        ],
    },
    {
        "text": "How long should your response be for IELTS Academic Writing Task 2?",
        "explanation": "IELTS Academic Writing Task 2 requires you to write at least 250 words in response to a point of view, argument, or problem.",
        "reference": "IELTS Academic Writing Task 2 Requirements",
        "points": 1,
        "answers": [
            {"text": "At least 150 words", "is_correct": False},
            {"text": "At least 250 words", "is_correct": True},
            {"text": "At least 300 words", "is_correct": False},
            {"text": "At least 200 words", "is_correct": False},
        ],
    },
    {
        "text": "In IELTS Academic Reading, how many passages are there?",
        "explanation": "IELTS Academic Reading contains three long passages with a variety of questions, totaling 40 questions to be completed in 60 minutes.",
        "reference": "IELTS Academic Reading Format",
        "points": 1,
        "answers": [
            {"text": "Two passages", "is_correct": False},
            {"text": "Three passages", "is_correct": True},
            {"text": "Four passages", "is_correct": False},
            {"text": "Five passages", "is_correct": False},
        ],
    },
    {
        "text": "Which of the following is a typical question type in IELTS Academic Listening?",
        "explanation": "IELTS Academic Listening includes various question types such as multiple choice, matching, plan/map/diagram labeling, form completion, note completion, table completion, flow-chart completion, and summary completion.",
        "reference": "IELTS Academic Listening Question Types",
        "points": 1,
        "answers": [
            {"text": "Multiple choice questions", "is_correct": True},
            {"text": "Essay writing", "is_correct": False},
            {"text": "Translation exercises", "is_correct": False},
            {"text": "Grammar correction", "is_correct": False},
        ],
    },
    {
        "text": "How many parts are there in the IELTS Academic Speaking test?",
        "explanation": "The IELTS Academic Speaking test consists of three parts: Part 1 (Introduction and interview), Part 2 (Long turn), and Part 3 (Two-way discussion).",
        "reference": "IELTS Academic Speaking Test Structure",
        "points": 1,
        "answers": [
            {"text": "Two parts", "is_correct": False},
            {"text": "Three parts", "is_correct": True},
            {"text": "Four parts", "is_correct": False},
            {"text": "Five parts", "is_correct": False},
        ],
    }
]