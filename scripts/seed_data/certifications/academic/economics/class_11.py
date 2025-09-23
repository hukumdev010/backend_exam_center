"""Economics Class 11 Certification"""

CERTIFICATION = {
    "name": "Economics Class 11",
    "description": "Basic economic principles for 11th grade students",
    "slug": "economics-class-11",
    "level": "Class 11",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "economics",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the basic economic problem?",
        "explanation": (
            "Scarcity is the fundamental economic problem where "
            "resources are limited but wants are unlimited."
        ),
        "reference": "Basic Economics",
        "points": 1,
        "answers": [
            {"text": "Inflation", "is_correct": False},
            {"text": "Unemployment", "is_correct": False},
            {"text": "Scarcity", "is_correct": True},
            {"text": "Recession", "is_correct": False}
        ]
    },
    {
        "text": "What does GDP stand for?",
        "explanation": (
            "GDP stands for Gross Domestic Product, which measures "
            "the total value of goods and services produced in a country."
        ),
        "reference": "National Income",
        "points": 1,
        "answers": [
            {"text": "Gross Development Product", "is_correct": False},
            {"text": "Gross Domestic Product", "is_correct": True},
            {"text": "General Development Plan", "is_correct": False},
            {"text": "Global Domestic Product", "is_correct": False}
        ]
    },
    {
        "text": "What is demand in economics?",
        "explanation": (
            "Demand is the quantity of a good or service that "
            "consumers are willing and able to buy at a given price."
        ),
        "reference": "Demand and Supply",
        "points": 1,
        "answers": [
            {"text": "Quantity available for sale", "is_correct": False},
            {"text": "Willingness and ability to buy", "is_correct": True},
            {"text": "Price of goods", "is_correct": False},
            {"text": "Production capacity", "is_correct": False}
        ]
    },
    {
        "text": "What happens to demand when price increases?",
        "explanation": (
            "According to the law of demand, when price increases, "
            "quantity demanded generally decreases."
        ),
        "reference": "Law of Demand",
        "points": 1,
        "answers": [
            {"text": "Demand increases", "is_correct": False},
            {"text": "Demand decreases", "is_correct": True},
            {"text": "Demand remains same", "is_correct": False},
            {"text": "Supply increases", "is_correct": False}
        ]
    },
    {
        "text": "What is opportunity cost?",
        "explanation": (
            "Opportunity cost is the value of the best alternative "
            "that must be given up when making a choice."
        ),
        "reference": "Economic Concepts",
        "points": 1,
        "answers": [
            {"text": "Cost of production", "is_correct": False},
            {"text": "Value of best alternative forgone", "is_correct": True},
            {"text": "Market price", "is_correct": False},
            {"text": "Fixed costs", "is_correct": False}
        ]
    }
]