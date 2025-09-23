"""Computer Science Introduction Certification"""

CERTIFICATION = {
    "name": "Computer Science Introduction",
    "description": "Basic computer science concepts and programming",
    "slug": "computer-science-introduction",
    "level": "Introduction",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "computer_science",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is an algorithm?",
        "explanation": (
            "An algorithm is a step-by-step procedure or set of "
            "instructions for solving a problem or completing a task."
        ),
        "reference": "Algorithms",
        "points": 1,
        "answers": [
            {"text": "A programming language", "is_correct": False},
            {"text": "Step-by-step instructions", "is_correct": True},
            {"text": "A computer program", "is_correct": False},
            {"text": "A data structure", "is_correct": False}
        ]
    },
    {
        "text": "What does CPU stand for?",
        "explanation": (
            "CPU stands for Central Processing Unit, which is the "
            "main component that executes instructions in a computer."
        ),
        "reference": "Computer Hardware",
        "points": 1,
        "answers": [
            {"text": "Computer Processing Unit", "is_correct": False},
            {"text": "Central Processing Unit", "is_correct": True},
            {"text": "Core Processing Unit", "is_correct": False},
            {"text": "Central Program Unit", "is_correct": False}
        ]
    },
    {
        "text": "What is binary code?",
        "explanation": (
            "Binary code is a system that uses only two digits, "
            "0 and 1, to represent information in computers."
        ),
        "reference": "Number Systems",
        "points": 1,
        "answers": [
            {"text": "Code with 10 digits", "is_correct": False},
            {"text": "Code with 0s and 1s only", "is_correct": True},
            {"text": "Programming language", "is_correct": False},
            {"text": "Encryption method", "is_correct": False}
        ]
    },
    {
        "text": "What is a variable in programming?",
        "explanation": (
            "A variable is a storage location with a name that "
            "can hold different values during program execution."
        ),
        "reference": "Programming Basics",
        "points": 1,
        "answers": [
            {"text": "A fixed number", "is_correct": False},
            {"text": "Storage location for data", "is_correct": True},
            {"text": "A function", "is_correct": False},
            {"text": "A command", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of loops in programming?",
        "explanation": (
            "Loops allow you to repeat a block of code multiple times "
            "until a certain condition is met."
        ),
        "reference": "Control Structures",
        "points": 1,
        "answers": [
            {"text": "Store data", "is_correct": False},
            {"text": "Repeat code execution", "is_correct": True},
            {"text": "Make decisions", "is_correct": False},
            {"text": "Connect to internet", "is_correct": False}
        ]
    }
]