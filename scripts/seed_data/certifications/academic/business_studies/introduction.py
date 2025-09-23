"""Business Studies Introduction Certification"""

CERTIFICATION = {
    "name": "Business Studies Introduction",
    "description": "Basic business concepts and entrepreneurship",
    "slug": "business-studies-introduction",
    "level": "Introduction",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "business_studies",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is entrepreneurship?",
        "explanation": (
            "Entrepreneurship is the process of starting and running "
            "a business venture, taking financial risks for profit."
        ),
        "reference": "Entrepreneurship",
        "points": 1,
        "answers": [
            {"text": "Working for a company", "is_correct": False},
            {"text": "Starting and running a business", "is_correct": True},
            {"text": "Investing in stocks", "is_correct": False},
            {"text": "Managing employees", "is_correct": False}
        ]
    },
    {
        "text": "What is marketing?",
        "explanation": (
            "Marketing is the process of promoting, selling, and "
            "distributing products or services to customers."
        ),
        "reference": "Marketing",
        "points": 1,
        "answers": [
            {"text": "Only advertising products", "is_correct": False},
            {"text": "Promoting and selling products", "is_correct": True},
            {"text": "Manufacturing products", "is_correct": False},
            {"text": "Managing finances", "is_correct": False}
        ]
    },
    {
        "text": "What is supply and demand?",
        "explanation": (
            "Supply and demand is an economic model where the price "
            "of goods is determined by availability and consumer desire."
        ),
        "reference": "Economic Principles",
        "points": 1,
        "answers": [
            {"text": "Company policies", "is_correct": False},
            {"text": "Price determination by availability and desire", "is_correct": True},
            {"text": "Employee management", "is_correct": False},
            {"text": "Production methods", "is_correct": False}
        ]
    },
    {
        "text": "What is a business plan?",
        "explanation": (
            "A business plan is a document that outlines business goals, "
            "strategies, and financial projections for a company."
        ),
        "reference": "Business Planning",
        "points": 1,
        "answers": [
            {"text": "Employee schedule", "is_correct": False},
            {"text": "Document outlining business goals and strategies", "is_correct": True},
            {"text": "Financial statement", "is_correct": False},
            {"text": "Marketing campaign", "is_correct": False}
        ]
    },
    {
        "text": "What is profit?",
        "explanation": (
            "Profit is the financial gain obtained when revenue "
            "from business operations exceeds expenses and costs."
        ),
        "reference": "Financial Concepts",
        "points": 1,
        "answers": [
            {"text": "Total sales", "is_correct": False},
            {"text": "Revenue minus expenses", "is_correct": True},
            {"text": "Number of customers", "is_correct": False},
            {"text": "Business investment", "is_correct": False}
        ]
    }
]