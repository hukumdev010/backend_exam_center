"""
Python Institute PCPP-2 (Python Certified Professional Programmer Level 2) Certification
Advanced Enterprise Python Programming
"""

PYTHON_PCPP2 = {
    "title": "Python Institute PCPP-2 (Python Certified Professional Programmer Level 2)",
    "description": "Advanced Enterprise Python Programming certification covering design patterns, advanced OOP, GUI programming, network programming, and software architecture.",
    "category": "Programming",
    "subcategory": "Python",
    "difficulty": "Expert",
    "duration_hours": 3,
    "passing_score": 75,
    "total_questions": 50,
    "syllabus": """
    Module 1: Advanced Object-Oriented Programming
    - Design patterns (Singleton, Factory, Observer, Strategy, Command)
    - Abstract base classes and metaclasses
    - Descriptors and properties
    - Method resolution order (MRO)
    - Multiple inheritance and mixins

    Module 2: GUI Programming
    - tkinter advanced widgets and layouts
    - Event handling and binding
    - Canvas and drawing operations
    - Custom widgets and themes
    - GUI application architecture

    Module 3: Network Programming
    - Socket programming (TCP/UDP)
    - HTTP client/server programming
    - RESTful API development
    - WebSocket programming
    - Network protocols and security

    Module 4: Advanced File and Data Processing
    - Binary file operations
    - Serialization (pickle, JSON, XML)
    - Database connectivity (sqlite3, ORM)
    - Data validation and parsing
    - File system monitoring

    Module 5: Software Architecture and Testing
    - Software design principles (SOLID)
    - Code organization and packaging
    - Unit testing and mocking
    - Performance optimization
    - Documentation and deployment
    """,
    "questions": [
        {
            "question": "Which design pattern ensures that a class has only one instance and provides a global point of access to it?",
            "options": [
                "Factory Pattern",
                "Singleton Pattern", 
                "Observer Pattern",
                "Strategy Pattern"
            ],
            "correct_answer": "Singleton Pattern",
            "explanation": "The Singleton pattern restricts a class to a single instance and provides a global point of access to that instance."
        },
        {
            "question": "What is the primary purpose of metaclasses in Python?",
            "options": [
                "To create instances of classes",
                "To define how classes are created",
                "To handle method calls",
                "To manage memory allocation"
            ],
            "correct_answer": "To define how classes are created",
            "explanation": "Metaclasses are classes whose instances are classes themselves. They define how classes are constructed."
        },
        {
            "question": "In tkinter, which method is used to handle window close events?",
            "options": [
                "on_closing()",
                "protocol('WM_DELETE_WINDOW', handler)",
                "bind('<Destroy>', handler)",
                "close_handler()"
            ],
            "correct_answer": "protocol('WM_DELETE_WINDOW', handler)",
            "explanation": "The protocol() method with 'WM_DELETE_WINDOW' is used to handle window close events in tkinter."
        },
        {
            "question": "Which socket method is used to accept incoming connections on a server socket?",
            "options": [
                "connect()",
                "listen()",
                "accept()",
                "bind()"
            ],
            "correct_answer": "accept()",
            "explanation": "The accept() method is used by server sockets to accept incoming client connections."
        },
        {
            "question": "What does the __enter__ method define in a context manager?",
            "options": [
                "Cleanup operations when exiting the context",
                "Setup operations when entering the context",
                "Error handling within the context",
                "The context manager's return value"
            ],
            "correct_answer": "Setup operations when entering the context",
            "explanation": "__enter__ defines what happens when entering a 'with' block and can return a value to be used in the context."
        },
        {
            "question": "Which principle states that software entities should be open for extension but closed for modification?",
            "options": [
                "Single Responsibility Principle",
                "Open/Closed Principle",
                "Liskov Substitution Principle",
                "Interface Segregation Principle"
            ],
            "correct_answer": "Open/Closed Principle",
            "explanation": "The Open/Closed Principle states that classes should be open for extension but closed for modification."
        },
        {
            "question": "What is the purpose of the pickle module in Python?",
            "options": [
                "Text file processing",
                "Object serialization and deserialization",
                "Network communication",
                "Database operations"
            ],
            "correct_answer": "Object serialization and deserialization",
            "explanation": "The pickle module is used for serializing and deserializing Python objects to/from binary format."
        },
        {
            "question": "In the Observer pattern, what is the role of the Subject?",
            "options": [
                "To observe changes in other objects",
                "To notify observers when its state changes",
                "To process notifications from observers",
                "To create observer instances"
            ],
            "correct_answer": "To notify observers when its state changes",
            "explanation": "The Subject maintains a list of observers and notifies them when its state changes."
        },
        {
            "question": "Which HTTP status code indicates that a resource was successfully created?",
            "options": [
                "200 OK",
                "201 Created",
                "202 Accepted",
                "204 No Content"
            ],
            "correct_answer": "201 Created",
            "explanation": "HTTP status code 201 indicates that a request has been fulfilled and resulted in a new resource being created."
        },
        {
            "question": "What is the main advantage of using abstract base classes (ABC) in Python?",
            "options": [
                "Improved performance",
                "Enforcing interface contracts",
                "Memory optimization",
                "Simplified syntax"
            ],
            "correct_answer": "Enforcing interface contracts",
            "explanation": "Abstract base classes enforce that derived classes implement specific methods, ensuring interface contracts."
        },
        {
            "question": "In tkinter Canvas, which method is used to create a rectangle?",
            "options": [
                "draw_rectangle()",
                "create_rect()",
                "create_rectangle()",
                "rectangle()"
            ],
            "correct_answer": "create_rectangle()",
            "explanation": "The create_rectangle() method is used to draw rectangles on a tkinter Canvas widget."
        },
        {
            "question": "What is the primary purpose of the unittest.mock module?",
            "options": [
                "Creating test databases",
                "Mocking objects and functions for testing",
                "Generating test data",
                "Performance testing"
            ],
            "correct_answer": "Mocking objects and functions for testing",
            "explanation": "The unittest.mock module provides tools for creating mock objects to replace real objects during testing."
        },
        {
            "question": "Which method resolution order (MRO) algorithm does Python use?",
            "options": [
                "Depth-First Search",
                "Breadth-First Search",
                "C3 Linearization",
                "Random Selection"
            ],
            "correct_answer": "C3 Linearization",
            "explanation": "Python uses the C3 linearization algorithm to determine the method resolution order in multiple inheritance."
        },
        {
            "question": "What is the purpose of the __slots__ attribute in a Python class?",
            "options": [
                "To define method signatures",
                "To restrict instance attributes and save memory",
                "To create class methods",
                "To handle inheritance"
            ],
            "correct_answer": "To restrict instance attributes and save memory",
            "explanation": "__slots__ restricts the attributes that instances can have and can reduce memory usage."
        },
        {
            "question": "In socket programming, what does the SO_REUSEADDR option do?",
            "options": [
                "Allows multiple connections",
                "Enables address reuse for quick restart",
                "Sets socket timeout",
                "Configures buffer size"
            ],
            "correct_answer": "Enables address reuse for quick restart",
            "explanation": "SO_REUSEADDR allows a socket to reuse an address that is in TIME_WAIT state, enabling quick server restart."
        },
        {
            "question": "What is the Factory Method pattern used for?",
            "options": [
                "Creating objects without specifying exact classes",
                "Managing object lifecycle",
                "Implementing inheritance",
                "Handling exceptions"
            ],
            "correct_answer": "Creating objects without specifying exact classes",
            "explanation": "The Factory Method pattern creates objects without specifying the exact class of object that will be created."
        },
        {
            "question": "Which decorator is used to define a property setter in Python?",
            "options": [
                "@property.setter",
                "@setter",
                "@<property_name>.setter",
                "@set_property"
            ],
            "correct_answer": "@<property_name>.setter",
            "explanation": "The setter decorator uses the property name, like @property_name.setter, to define a setter method."
        },
        {
            "question": "What is the main benefit of using dependency injection?",
            "options": [
                "Faster execution",
                "Reduced coupling and improved testability",
                "Smaller code size",
                "Better error handling"
            ],
            "correct_answer": "Reduced coupling and improved testability",
            "explanation": "Dependency injection reduces coupling between components and makes code more testable and maintainable."
        },
        {
            "question": "In RESTful APIs, which HTTP method is typically used for updating a resource?",
            "options": [
                "GET",
                "POST",
                "PUT",
                "DELETE"
            ],
            "correct_answer": "PUT",
            "explanation": "PUT is typically used for updating an entire resource in RESTful APIs (PATCH for partial updates)."
        },
        {
            "question": "What is the purpose of the Strategy pattern?",
            "options": [
                "To define a family of algorithms and make them interchangeable",
                "To create complex objects step by step",
                "To provide a simplified interface to a complex system",
                "To ensure a class has only one instance"
            ],
            "correct_answer": "To define a family of algorithms and make them interchangeable",
            "explanation": "The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable."
        }
    ]
}