"""Computer Science Advanced Certification"""

CERTIFICATION = {
    "name": "Computer Science Advanced",
    "description": "Advanced programming and data structures concepts",
    "slug": "computer-science-advanced",
    "level": "Advanced",
    "duration": 75,
    "questions_count": 30,
    "category_slug": "computer_science",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the time complexity of binary search?",
        "explanation": (
            "Binary search has O(log n) time complexity because it "
            "eliminates half of the search space in each iteration."
        ),
        "reference": "Algorithms",
        "points": 1,
        "answers": [
            {"text": "O(n)", "is_correct": False},
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(n²)", "is_correct": False},
            {"text": "O(1)", "is_correct": False}
        ]
    },
    {
        "text": "What is a stack data structure?",
        "explanation": (
            "A stack is a Last-In-First-Out (LIFO) data structure "
            "where elements are added and removed from the same end."
        ),
        "reference": "Data Structures",
        "points": 1,
        "answers": [
            {"text": "First-In-First-Out structure", "is_correct": False},
            {"text": "Last-In-First-Out structure", "is_correct": True},
            {"text": "Random access structure", "is_correct": False},
            {"text": "Sorted data structure", "is_correct": False}
        ]
    },
    {
        "text": "What is object-oriented programming?",
        "explanation": (
            "OOP is a programming paradigm based on objects that "
            "contain data (attributes) and code (methods)."
        ),
        "reference": "Programming Paradigms",
        "points": 1,
        "answers": [
            {"text": "Sequential programming", "is_correct": False},
            {"text": "Programming with objects", "is_correct": True},
            {"text": "Database programming", "is_correct": False},
            {"text": "Web programming", "is_correct": False}
        ]
    },
    {
        "text": "What is recursion?",
        "explanation": (
            "Recursion is a programming technique where a function "
            "calls itself to solve smaller instances of the same problem."
        ),
        "reference": "Programming Concepts",
        "points": 1,
        "answers": [
            {"text": "Repeating loops", "is_correct": False},
            {"text": "Function calling itself", "is_correct": True},
            {"text": "Error handling", "is_correct": False},
            {"text": "Memory management", "is_correct": False}
        ]
    },
    {
        "text": "What is a database?",
        "explanation": (
            "A database is an organized collection of structured "
            "information or data stored electronically."
        ),
        "reference": "Database Systems",
        "points": 1,
        "answers": [
            {"text": "A programming language", "is_correct": False},
            {"text": "Organized collection of data", "is_correct": True},
            {"text": "A web server", "is_correct": False},
            {"text": "A computer network", "is_correct": False}
        ]
    }
]