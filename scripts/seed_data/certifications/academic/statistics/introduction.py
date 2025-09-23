"""Statistics Introduction Certification"""

CERTIFICATION = {
    "name": "Statistics Introduction",
    "description": "Basic statistics, probability, and data analysis",
    "slug": "statistics-introduction",
    "level": "Introduction",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "statistics",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the mean of the numbers 2, 4, 6, 8, 10?",
        "explanation": (
            "The mean (average) is calculated by adding all numbers "
            "and dividing by the count: (2+4+6+8+10)/5 = 6."
        ),
        "reference": "Descriptive Statistics",
        "points": 1,
        "answers": [
            {"text": "5", "is_correct": False},
            {"text": "6", "is_correct": True},
            {"text": "7", "is_correct": False},
            {"text": "8", "is_correct": False}
        ]
    },
    {
        "text": "What is the median of the numbers 1, 3, 5, 7, 9?",
        "explanation": (
            "The median is the middle value when numbers are arranged "
            "in order. In this case, 5 is the middle value."
        ),
        "reference": "Central Tendency",
        "points": 1,
        "answers": [
            {"text": "3", "is_correct": False},
            {"text": "5", "is_correct": True},
            {"text": "6", "is_correct": False},
            {"text": "7", "is_correct": False}
        ]
    },
    {
        "text": "What is probability?",
        "explanation": (
            "Probability is a measure of the likelihood of an event "
            "occurring, expressed as a number between 0 and 1."
        ),
        "reference": "Probability",
        "points": 1,
        "answers": [
            {"text": "Always equals 1", "is_correct": False},
            {"text": "Likelihood of an event (0 to 1)", "is_correct": True},
            {"text": "Number of outcomes", "is_correct": False},
            {"text": "Always equals 0.5", "is_correct": False}
        ]
    },
    {
        "text": "What is a sample in statistics?",
        "explanation": (
            "A sample is a subset of a population that is used to "
            "represent and make inferences about the entire population."
        ),
        "reference": "Sampling",
        "points": 1,
        "answers": [
            {"text": "The entire population", "is_correct": False},
            {"text": "Subset representing the population", "is_correct": True},
            {"text": "A single data point", "is_correct": False},
            {"text": "The average value", "is_correct": False}
        ]
    },
    {
        "text": "What is standard deviation?",
        "explanation": (
            "Standard deviation measures how spread out data points "
            "are from the mean (average) of the dataset."
        ),
        "reference": "Variability",
        "points": 1,
        "answers": [
            {"text": "The highest value", "is_correct": False},
            {"text": "Measure of data spread from mean", "is_correct": True},
            {"text": "The most common value", "is_correct": False},
            {"text": "The middle value", "is_correct": False}
        ]
    }
]