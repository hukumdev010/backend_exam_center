"""Python Institute PCAP Certification"""

CERTIFICATION = {
    "name": "Python Institute PCAP",
    "description": "Python Certified Associate Programmer",
    "slug": "python-pcap",
    "level": "Associate",
    "duration": 65,
    "questions_count": 40,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": """## Code Analysis Question

**What is the output of the following code?**

```python
class A:
    def __init__(self):
        self.x = 1

obj = A()
print(obj.x)
```

*Choose the correct output:*""",
        "explanation": """# Object-Oriented Programming - Classes and Objects

> **Key Concept**: Classes are blueprints for creating objects. The `__init__` method is the constructor that initializes new instances.

## Code Breakdown:

1. **Class Definition**: `class A:` defines a new class named A
2. **Constructor Method**: `__init__(self)` is called when creating new instances
3. **Instance Variable**: `self.x = 1` sets an instance attribute
4. **Object Creation**: `obj = A()` creates a new instance
5. **Attribute Access**: `print(obj.x)` accesses the instance variable

## Example Output:
```python
class A:
    def __init__(self):
        self.x = 1

obj = A()
print(obj.x)  # Output: 1
```

### 📝 **Important Notes:**
- The `__init__` method initializes instance variables when an object is created
- Instance variables belong to specific object instances
- The `self` parameter refers to the instance being created

### 🔗 **Related Concepts:**
- Instance vs Class variables
- Object instantiation
- Constructor methods""",
        "reference": "https://docs.python.org/3/tutorial/classes.html",
        "points": 1,
        "answers": [
            {"text": "**1**", "is_correct": True},
            {"text": "**None**", "is_correct": False},
            {"text": "**Error**", "is_correct": False},
            {"text": "**0**", "is_correct": False},
        ],
    },
    {
        "text": "Which method is used to handle exceptions in Python?",
        "explanation": """# Exception Handling in Python

Use `try-except` blocks to handle exceptions and prevent program crashes.

## Basic Syntax:
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid value!")
finally:
    print("This always executes")
```

## Common Exception Types:
- `ValueError` - Invalid value for operation
- `TypeError` - Wrong data type  
- `IndexError` - List index out of range
- `KeyError` - Dictionary key not found
- `ZeroDivisionError` - Division by zero

Always catch specific exceptions before general ones.""",
        "reference": "https://docs.python.org/3/tutorial/errors.html",
        "points": 1,
        "answers": [
            {"text": "try-except", "is_correct": True},
            {"text": "catch-throw", "is_correct": False},
            {"text": "handle-error", "is_correct": False},
            {"text": "exception-catch", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between a list and a tuple?",
        "explanation": """# Lists vs Tuples

Lists are mutable (can be changed), tuples are immutable (cannot be changed).

## Example:
```python
# List - mutable
my_list = [1, 2, 3]
my_list[0] = 10  # Works: [10, 2, 3]

# Tuple - immutable
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Error: cannot modify
```

## Key Differences:
- **Mutability**: Lists can be modified, tuples cannot
- **Performance**: Tuples are faster for accessing data
- **Memory**: Tuples use less memory
- **Use cases**: Lists for dynamic data, tuples for fixed data

Use tuples for coordinates, database records, or any fixed data.
Use lists for shopping carts, user inputs, or dynamic collections.""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html",
        "points": 1,
        "answers": [
            {"text": "Lists are mutable, tuples are immutable", "is_correct": True},
            {"text": "Lists are faster than tuples", "is_correct": False},
            {"text": "Tuples can store more data", "is_correct": False},
            {"text": "No difference", "is_correct": False},
        ],
    },
    {
        "text": "What does the 'super()' function do in Python?",
        "explanation": """# Inheritance and super() Function

`super()` calls methods from the parent class in inheritance.

## Example:
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed
    
    def speak(self):
        return super().speak() + " - Woof!"
```

Allows code reuse and method extension in inheritance.""",
        "reference": "https://docs.python.org/3/library/functions.html#super",
        "points": 1,
        "answers": [
            {"text": "Calls parent class methods", "is_correct": True},
            {"text": "Creates a new class", "is_correct": False},
            {"text": "Deletes the current object", "is_correct": False},
            {"text": "Imports modules", "is_correct": False},
        ],
    },
    {
        "text": "What is a lambda function in Python?",
        "explanation": """# Lambda Functions (Anonymous Functions)

Lambda functions are small, anonymous functions that can have any number of arguments but only one expression.

## Example:
```python
# Regular function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

# Usage in higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
# Result: [1, 4, 9, 16, 25]
```

Useful for short, one-line functions and functional programming.""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions",
        "points": 1,
        "answers": [
            {"text": "A small anonymous function", "is_correct": True},
            {"text": "A type of variable", "is_correct": False},
            {"text": "A loop statement", "is_correct": False},
            {"text": "A class method", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of '__init__.py' file?",
        "explanation": """# Package Initialization with __init__.py

The `__init__.py` file makes a directory a Python package and controls what gets imported.

## Example:
```python
# mypackage/__init__.py
from .module1 import function1
from .module2 import Class2

__all__ = ['function1', 'Class2']

# Now you can import directly:
# from mypackage import function1, Class2
```

Can be empty or contain package initialization code.""",
        "reference": "https://docs.python.org/3/tutorial/modules.html#packages",
        "points": 1,
        "answers": [
            {"text": "Makes directory a Python package", "is_correct": True},
            {"text": "Initializes variables", "is_correct": False},
            {"text": "Contains main function", "is_correct": False},
            {"text": "Stores configuration", "is_correct": False},
        ],
    },
    {
        "text": """## Code Output Question

**What is the output of the following code?**

```python
list(map(lambda x: x*2, [1, 2, 3]))
```

*Choose the correct result:*""",
        "explanation": """# Map Function with Lambda

`map()` applies a function to every item in an iterable and returns an iterator.

## Example:
```python
numbers = [1, 2, 3]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)  # [2, 4, 6]

# Equivalent to:
doubled = [x*2 for x in numbers]
```

Common functional programming pattern for transforming data.""",
        "reference": "https://docs.python.org/3/library/functions.html#map",
        "points": 1,
        "answers": [
            {"text": "[2, 4, 6]", "is_correct": True},
            {"text": "[1, 2, 3]", "is_correct": False},
            {"text": "[1, 4, 9]", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": "What is a decorator in Python?",
        "explanation": """# Decorators in Python

Decorators are functions that modify or extend the behavior of other functions.

## Example:
```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output: Before function call
#         Hello!
#         After function call
```

Used for logging, timing, authentication, etc.""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
        "points": 1,
        "answers": [
            {"text": "A function that modifies other functions", "is_correct": True},
            {"text": "A type of variable", "is_correct": False},
            {"text": "A design pattern", "is_correct": False},
            {"text": "A data structure", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between '==' and 'is' operators?",
        "explanation": """# Equality vs Identity Operators

`==` compares values, `is` compares object identity (memory location).

## Example:
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True - same values
print(a is b)  # False - different objects
print(a is c)  # True - same object

# For small integers and strings:
x = 5
y = 5
print(x is y)  # True - Python optimizes small integers
```

Use `==` for value comparison, `is` for identity checks (especially with None).""",
        "reference": "https://docs.python.org/3/reference/expressions.html#comparisons",
        "points": 1,
        "answers": [
            {"text": "== compares values, is compares identity", "is_correct": True},
            {"text": "Both do the same thing", "is_correct": False},
            {"text": "is compares values, == compares identity", "is_correct": False},
            {"text": "== is faster than is", "is_correct": False},
        ],
    },
    {
        "text": "What does the 'yield' keyword do in Python?",
        "explanation": """# Generators and yield Keyword

`yield` creates a generator function that returns an iterator, pausing execution and resuming where it left off.

## Example:
```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

counter = count_up_to(3)
for num in counter:
    print(num)  # 1, 2, 3

# Memory efficient for large sequences
```

Generators produce values on-demand, saving memory for large datasets.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html#generators",
        "points": 1,
        "answers": [
            {"text": "Creates a generator function", "is_correct": True},
            {"text": "Returns a value and exits", "is_correct": False},
            {"text": "Imports a module", "is_correct": False},
            {"text": "Defines a class", "is_correct": False},
        ],
    },
    {
        "text": """## File Handling Code Question

**What is the output of the following code?**

```python
with open('file.txt', 'w') as f:
    f.write('Hello')
print('File closed?', f.closed)
```

*Choose the correct output:*""",
        "explanation": """# Context Managers and 'with' Statement

The `with` statement ensures proper resource management by automatically closing files.

## Example:
```python
with open('file.txt', 'w') as f:
    f.write('Hello')
print('File closed?', f.closed)  # True

# Equivalent to:
f = open('file.txt', 'w')
try:
    f.write('Hello')
finally:
    f.close()
```

Context managers guarantee cleanup even if exceptions occur.""",
        "reference": "https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files",
        "points": 1,
        "answers": [
            {"text": "File closed? True", "is_correct": True},
            {"text": "File closed? False", "is_correct": False},
            {"text": "Error", "is_correct": False},
            {"text": "File closed? None", "is_correct": False},
        ],
    },
    {
        "text": "What is list comprehension in Python?",
        "explanation": """# List Comprehensions

List comprehensions provide a concise way to create lists using a single line of code.

## Example:
```python
# Traditional approach
squares = []
for x in range(5):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

More readable and efficient than traditional loops for simple transformations.""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions",
        "points": 1,
        "answers": [
            {"text": "A concise way to create lists", "is_correct": True},
            {"text": "A type of loop", "is_correct": False},
            {"text": "A function argument", "is_correct": False},
            {"text": "A data type", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between args and kwargs?",
        "explanation": """# Variable Arguments: *args and **kwargs

`*args` collects positional arguments, `**kwargs` collects keyword arguments.

## Example:
```python
def my_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

my_function(1, 2, 3, name="Alice", age=25)
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 25}

# Unpacking
numbers = [1, 2, 3]
data = {'x': 10, 'y': 20}
my_function(*numbers, **data)
```

Useful for flexible function signatures and function decorators.""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions",
        "points": 1,
        "answers": [
            {"text": "*args for positional, **kwargs for keyword arguments", "is_correct": True},
            {"text": "Both do the same thing", "is_correct": False},
            {"text": "*args for keywords, **kwargs for positional", "is_correct": False},
            {"text": "They are data types", "is_correct": False},
        ],
    },
    {
        "text": "What is multiple inheritance in Python?",
        "explanation": """# Multiple Inheritance

A class can inherit from multiple parent classes, gaining features from all of them.

## Example:
```python
class Animal:
    def eat(self):
        return "Eating"

class Flyable:
    def fly(self):
        return "Flying"

class Bird(Animal, Flyable):  # Multiple inheritance
    def chirp(self):
        return "Chirping"

bird = Bird()
print(bird.eat())   # From Animal
print(bird.fly())   # From Flyable
print(bird.chirp()) # Own method
```

Method Resolution Order (MRO) determines which method is called when there are conflicts.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html#multiple-inheritance",
        "points": 1,
        "answers": [
            {"text": "A class inheriting from multiple parent classes", "is_correct": True},
            {"text": "Creating multiple objects", "is_correct": False},
            {"text": "Having multiple methods", "is_correct": False},
            {"text": "Using multiple variables", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of __str__ and __repr__ methods?",
        "explanation": """# String Representation Methods

`__str__` defines user-friendly string representation, `__repr__` defines developer-friendly representation.

## Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 25)
print(str(p))   # Alice, 25 years old
print(repr(p))  # Person('Alice', 25)
```

`__str__` for end users, `__repr__` for debugging and development.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html#object.__str__",
        "points": 1,
        "answers": [
            {"text": "__str__ for user display, __repr__ for debugging", "is_correct": True},
            {"text": "Both do the same thing", "is_correct": False},
            {"text": "__repr__ for users, __str__ for debugging", "is_correct": False},
            {"text": "They convert objects to integers", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between shallow copy and deep copy?",
        "explanation": """# Shallow vs Deep Copy

Shallow copy creates new object but references to nested objects remain. Deep copy creates completely independent copy.

## Example:
```python
import copy

original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow = copy.copy(original)
shallow[0][0] = 'X'
print(original)  # [['X', 2, 3], [4, 5, 6]] - original affected!

# Deep copy
original = [[1, 2, 3], [4, 5, 6]]
deep = copy.deepcopy(original)
deep[0][0] = 'X'
print(original)  # [[1, 2, 3], [4, 5, 6]] - original unchanged
```

Use deepcopy for nested mutable objects to avoid unintended modifications.""",
        "reference": "https://docs.python.org/3/library/copy.html",
        "points": 1,
        "answers": [
            {"text": "Shallow copies references, deep copy creates independent copy", "is_correct": True},
            {"text": "Both do the same thing", "is_correct": False},
            {"text": "Deep copy is faster", "is_correct": False},
            {"text": "Shallow copy creates independent copy", "is_correct": False},
        ],
    },
    {
        "text": "What are property decorators used for?",
        "explanation": """# Property Decorators

Property decorators allow methods to be accessed like attributes while maintaining control over getting/setting values.

## Example:
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.radius)  # 5 (calls getter)
c.radius = 10    # calls setter
print(c.area)    # computed property
```

Provides clean interface while controlling access and validation.""",
        "reference": "https://docs.python.org/3/library/functions.html#property",
        "points": 1,
        "answers": [
            {"text": "Control access to attributes", "is_correct": True},
            {"text": "Create new classes", "is_correct": False},
            {"text": "Handle exceptions", "is_correct": False},
            {"text": "Import modules", "is_correct": False},
        ],
    },
    {
        "text": "What is the Global Interpreter Lock (GIL) in Python?",
        "explanation": """# Global Interpreter Lock (GIL)

The GIL prevents multiple threads from executing Python code simultaneously, affecting multi-threaded performance.

## Example:
```python
import threading
import time

def cpu_intensive_task():
    # This won't run in parallel due to GIL
    total = 0
    for i in range(10000000):
        total += i
    return total

# Multiple threads, but not truly parallel
threads = []
for i in range(4):
    t = threading.Thread(target=cpu_intensive_task)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

For CPU-bound tasks, use multiprocessing instead of threading.""",
        "reference": "https://docs.python.org/3/glossary.html#term-global-interpreter-lock",
        "points": 1,
        "answers": [
            {"text": "Prevents true parallel execution of Python threads", "is_correct": True},
            {"text": "Speeds up thread execution", "is_correct": False},
            {"text": "Manages memory allocation", "is_correct": False},
            {"text": "Handles file operations", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the __name__ == '__main__' check?",
        "explanation": """# Module Execution Check

`if __name__ == '__main__':` ensures code runs only when script is executed directly, not when imported.

## Example:
```python
# mymodule.py
def hello():
    print("Hello from module")

if __name__ == '__main__':
    print("Running as main script")
    hello()

# When run directly: prints both messages
# When imported: only function is available, no automatic execution
```

Essential for creating reusable modules with optional standalone functionality.""",
        "reference": "https://docs.python.org/3/library/__main__.html",
        "points": 1,
        "answers": [
            {"text": "Run code only when script is executed directly", "is_correct": True},
            {"text": "Check if module is imported", "is_correct": False},
            {"text": "Define the main function", "is_correct": False},
            {"text": "Handle exceptions", "is_correct": False},
        ],
    },
    {
        "text": "What is a metaclass in Python?",
        "explanation": """# Metaclasses

A metaclass is a class whose instances are classes. It controls class creation and behavior.

## Example:
```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Connected"

db1 = Database()
db2 = Database()
print(db1 is db2)  # True - same instance
```

Advanced feature for controlling class creation and behavior.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html#metaclasses",
        "points": 1,
        "answers": [
            {"text": "A class that creates other classes", "is_correct": True},
            {"text": "A parent class", "is_correct": False},
            {"text": "A data structure", "is_correct": False},
            {"text": "A function decorator", "is_correct": False},
        ],
    },
]
