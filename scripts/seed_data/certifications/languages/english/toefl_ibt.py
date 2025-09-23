"""TOEFL iBT Certification"""

CERTIFICATION = {
    "name": "TOEFL iBT",
    "description": "Test of English as a Foreign Language Internet-Based Test for academic English proficiency",
    "slug": "toefl-ibt",
    "level": "B1-C2",
    "duration": 180,
    "questions_count": 140,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "How many sections are there in the TOEFL iBT test?",
        "explanation": "The TOEFL iBT test consists of four sections: Reading, Listening, Speaking, and Writing, all completed in one sitting.",
        "reference": "TOEFL iBT Test Structure",
        "points": 1,
        "answers": [
            {"text": "Three sections", "is_correct": False},
            {"text": "Four sections", "is_correct": True},
            {"text": "Five sections", "is_correct": False},
            {"text": "Six sections", "is_correct": False},
        ],
    },
    {
        "text": "What is the maximum score you can achieve on the TOEFL iBT?",
        "explanation": "The TOEFL iBT is scored on a scale of 0-120, with each of the four sections (Reading, Listening, Speaking, Writing) worth 0-30 points.",
        "reference": "TOEFL iBT Scoring",
        "points": 1,
        "answers": [
            {"text": "100 points", "is_correct": False},
            {"text": "120 points", "is_correct": True},
            {"text": "150 points", "is_correct": False},
            {"text": "200 points", "is_correct": False},
        ],
    },
    {
        "text": "In the TOEFL iBT Speaking section, how many tasks do you complete?",
        "explanation": "The TOEFL iBT Speaking section contains 4 tasks: 1 independent task and 3 integrated tasks that combine speaking with reading and/or listening.",
        "reference": "TOEFL iBT Speaking Tasks",
        "points": 1,
        "answers": [
            {"text": "3 tasks", "is_correct": False},
            {"text": "4 tasks", "is_correct": True},
            {"text": "5 tasks", "is_correct": False},
            {"text": "6 tasks", "is_correct": False},
        ],
    }
]