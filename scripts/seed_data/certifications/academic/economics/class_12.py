"""Economics Class 12 Certification"""

CERTIFICATION = {
    "name": "Economics Class 12",
    "description": "Advanced economic concepts for 12th grade students",
    "slug": "economics-class-12",
    "level": "Class 12",
    "duration": 75,
    "questions_count": 30,
    "category_slug": "economics",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is macroeconomics?",
        "explanation": (
            "Macroeconomics studies the economy as a whole, including "
            "national income, inflation, unemployment, and growth."
        ),
        "reference": "Macroeconomics",
        "points": 1,
        "answers": [
            {"text": "Study of individual firms", "is_correct": False},
            {"text": "Study of the whole economy", "is_correct": True},
            {"text": "Study of market prices", "is_correct": False},
            {"text": "Study of consumer behavior", "is_correct": False}
        ]
    },
    {
        "text": "What causes inflation?",
        "explanation": (
            "Inflation occurs when there is too much money chasing "
            "too few goods, leading to a general rise in prices."
        ),
        "reference": "Inflation",
        "points": 1,
        "answers": [
            {"text": "Decrease in money supply", "is_correct": False},
            {"text": "Increase in production", "is_correct": False},
            {"text": "Excess money supply", "is_correct": True},
            {"text": "Lower demand", "is_correct": False}
        ]
    },
    {
        "text": "What is fiscal policy?",
        "explanation": (
            "Fiscal policy refers to government spending and taxation "
            "policies used to influence the economy."
        ),
        "reference": "Government Policy",
        "points": 1,
        "answers": [
            {"text": "Central bank policies", "is_correct": False},
            {"text": "Government spending and taxation", "is_correct": True},
            {"text": "Trade regulations", "is_correct": False},
            {"text": "Price controls", "is_correct": False}
        ]
    },
    {
        "text": "What is the multiplier effect?",
        "explanation": (
            "The multiplier effect occurs when initial spending "
            "leads to increased economic activity beyond the original amount."
        ),
        "reference": "Keynesian Economics",
        "points": 1,
        "answers": [
            {"text": "Prices multiply over time", "is_correct": False},
            {"text": "Initial spending creates more activity", "is_correct": True},
            {"text": "Population growth", "is_correct": False},
            {"text": "Interest rate changes", "is_correct": False}
        ]
    },
    {
        "text": "What is perfect competition?",
        "explanation": (
            "Perfect competition is a market structure with many "
            "sellers offering identical products with no barriers to entry."
        ),
        "reference": "Market Structures",
        "points": 1,
        "answers": [
            {"text": "One seller dominates", "is_correct": False},
            {"text": "Few large sellers", "is_correct": False},
            {"text": "Many sellers, identical products", "is_correct": True},
            {"text": "Government controls prices", "is_correct": False}
        ]
    }
]