"""Accounting Fundamentals Certification"""

CERTIFICATION = {
    "name": "Accounting Fundamentals",
    "description": "Basic accounting principles and financial management",
    "slug": "accounting-fundamentals",
    "level": "Fundamentals",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "accounting",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the accounting equation?",
        "explanation": (
            "The basic accounting equation is Assets = Liabilities + "
            "Owner's Equity, which must always balance."
        ),
        "reference": "Accounting Principles",
        "points": 1,
        "answers": [
            {"text": "Revenue - Expenses = Profit", "is_correct": False},
            {"text": "Assets = Liabilities + Equity", "is_correct": True},
            {"text": "Income = Assets - Liabilities", "is_correct": False},
            {"text": "Profit = Revenue + Expenses", "is_correct": False}
        ]
    },
    {
        "text": "What is a debit in accounting?",
        "explanation": (
            "A debit is an entry on the left side of an account that "
            "increases assets and expenses, or decreases liabilities and equity."
        ),
        "reference": "Double-Entry Bookkeeping",
        "points": 1,
        "answers": [
            {"text": "Money owed to others", "is_correct": False},
            {"text": "Left-side entry that increases assets", "is_correct": True},
            {"text": "Right-side entry", "is_correct": False},
            {"text": "Bank withdrawal", "is_correct": False}
        ]
    },
    {
        "text": "What is depreciation?",
        "explanation": (
            "Depreciation is the allocation of the cost of an asset "
            "over its useful life as it loses value over time."
        ),
        "reference": "Asset Management",
        "points": 1,
        "answers": [
            {"text": "Increase in asset value", "is_correct": False},
            {"text": "Allocation of asset cost over time", "is_correct": True},
            {"text": "Purchase of new assets", "is_correct": False},
            {"text": "Sale of old assets", "is_correct": False}
        ]
    },
    {
        "text": "What is accounts receivable?",
        "explanation": (
            "Accounts receivable represents money owed to a company "
            "by customers for goods or services sold on credit."
        ),
        "reference": "Financial Statements",
        "points": 1,
        "answers": [
            {"text": "Money the company owes", "is_correct": False},
            {"text": "Money owed to the company", "is_correct": True},
            {"text": "Cash in bank", "is_correct": False},
            {"text": "Company expenses", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of a balance sheet?",
        "explanation": (
            "A balance sheet shows a company's financial position at "
            "a specific point in time, listing assets, liabilities, and equity."
        ),
        "reference": "Financial Statements",
        "points": 1,
        "answers": [
            {"text": "Show profit and loss", "is_correct": False},
            {"text": "Show financial position at a point in time", "is_correct": True},
            {"text": "Track daily transactions", "is_correct": False},
            {"text": "Calculate taxes owed", "is_correct": False}
        ]
    }
]