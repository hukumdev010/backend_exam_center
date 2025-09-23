"""Political Science Civics Certification"""

CERTIFICATION = {
    "name": "Political Science Civics",
    "description": "Government systems and political theory basics",
    "slug": "political-science-civics",
    "level": "Civics",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "political_science",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is democracy?",
        "explanation": (
            "Democracy is a system of government where power is held "
            "by the people, either directly or through elected representatives."
        ),
        "reference": "Forms of Government",
        "points": 1,
        "answers": [
            {"text": "Rule by one person", "is_correct": False},
            {"text": "Rule by the people", "is_correct": True},
            {"text": "Rule by the wealthy", "is_correct": False},
            {"text": "Rule by the military", "is_correct": False}
        ]
    },
    {
        "text": "What are the three branches of government in the US?",
        "explanation": (
            "The three branches are legislative (makes laws), "
            "executive (enforces laws), and judicial (interprets laws)."
        ),
        "reference": "Separation of Powers",
        "points": 1,
        "answers": [
            {"text": "Federal, state, local", "is_correct": False},
            {"text": "Legislative, executive, judicial", "is_correct": True},
            {"text": "Senate, House, Court", "is_correct": False},
            {"text": "President, Congress, Military", "is_correct": False}
        ]
    },
    {
        "text": "What is the Constitution?",
        "explanation": (
            "The Constitution is the supreme law that establishes "
            "the framework of government and guarantees basic rights."
        ),
        "reference": "Constitutional Government",
        "points": 1,
        "answers": [
            {"text": "A treaty with other nations", "is_correct": False},
            {"text": "The supreme law of the land", "is_correct": True},
            {"text": "A political party platform", "is_correct": False},
            {"text": "A court decision", "is_correct": False}
        ]
    },
    {
        "text": "What is federalism?",
        "explanation": (
            "Federalism is the division of power between national "
            "and state governments in a federal system."
        ),
        "reference": "Federal System",
        "points": 1,
        "answers": [
            {"text": "Rule by federal judges", "is_correct": False},
            {"text": "Division of power between levels", "is_correct": True},
            {"text": "Single central government", "is_correct": False},
            {"text": "International cooperation", "is_correct": False}
        ]
    },
    {
        "text": "What is a civil right?",
        "explanation": (
            "Civil rights are fundamental rights guaranteed to all "
            "citizens, such as freedom of speech and equal protection."
        ),
        "reference": "Civil Rights and Liberties",
        "points": 1,
        "answers": [
            {"text": "Right to vote only", "is_correct": False},
            {"text": "Fundamental rights of all citizens", "is_correct": True},
            {"text": "Property ownership rights", "is_correct": False},
            {"text": "Criminal justice rights", "is_correct": False}
        ]
    }
]