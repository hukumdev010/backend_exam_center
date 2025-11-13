"""Python Institute PCPP-1 Certification"""

CERTIFICATION = {
    "name": "Python Institute PCPP-1",
    "description": "Python Certified Professional Programmer Level 1",
    "slug": "python-pcpp1",
    "level": "Professional",
    "duration": 65,
    "questions_count": 20,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": """What is the output of the following code?

```python
class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['class_name'] = name
        return super().__new__(cls, name, bases, attrs)

class Person(metaclass=Meta):
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.class_name)
```""",
        "explanation": """Metaclasses control class creation. 
The Meta metaclass adds a 'class_name' attribute to any class 
that uses it. The output is 'Person'.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html",
        "points": 1,
        "answers": [
            {"text": "Person", "is_correct": True},
            {"text": "Alice", "is_correct": False},
            {"text": "Meta", "is_correct": False},
            {"text": "AttributeError", "is_correct": False},
        ],
    },
    {
        "text": """What is the purpose of the __exit__ method in context managers?""",
        "explanation": """The __exit__ method handles cleanup and resource 
management when exiting a context. It's called even if exceptions occur.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html",
        "points": 1,
        "answers": [
            {"text": "Initialize the context", "is_correct": False},
            {"text": "Handle cleanup and resource management", "is_correct": True},
            {"text": "Return the managed resource", "is_correct": False},
            {"text": "Create the context object", "is_correct": False},
        ],
    },
    {
        "text": """What is the output of this decorator code?

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
    return f"Greeted {name}"

result = greet("Alice")
print(result)
```""",
        "explanation": """This parameterized decorator executes the function 
3 times but only returns the last result. It prints 3 greetings.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html",
        "points": 1,
        "answers": [
            {"text": "Hello, Alice!\nGreeted Alice", "is_correct": False},
            {"text": "Hello, Alice!\nHello, Alice!\nHello, Alice!\n"
                     "Greeted Alice", "is_correct": True},
            {"text": "Greeted Alice", "is_correct": False},
            {"text": "Hello, Alice!", "is_correct": False},
        ],
    },
    {
        "text": """What is the difference between generator expressions and list comprehensions?""",
        "explanation": """Generator expressions use lazy evaluation and 
consume less memory, while list comprehensions create complete lists 
in memory immediately.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html",
        "points": 1,
        "answers": [
            {"text": "No difference, just syntax", "is_correct": False},
            {"text": "Generators are faster in all cases", "is_correct": False},
            {"text": "Generators use lazy evaluation and less memory", 
             "is_correct": True},
            {"text": "List comprehensions return iterators", "is_correct": False},
        ],
    },
    {
        "text": """What is the output of this function parameter code?

```python
def func(a, b, /, c, d, *, e, f):
    return f"{a}-{b}-{c}-{d}-{e}-{f}"

result = func(1, 2, c=3, d=4, e=5, f=6)
print(result)
```""",
        "explanation": """This demonstrates Python 3.8+ parameter types:
- a, b are positional-only (/)
- c, d can be positional or keyword
- e, f are keyword-only (*)""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html",
        "points": 1,
        "answers": [
            {"text": "1-2-3-4-5-6", "is_correct": True},
            {"text": "TypeError", "is_correct": False},
            {"text": "6-5-4-3-2-1", "is_correct": False},
            {"text": "1234-56", "is_correct": False},
        ],
    },
    {
        "text": """What is the time complexity of accessing an element in a Python dictionary?""",
        "explanation": """Python dictionaries use hash tables, providing 
O(1) average case access time through direct hash lookup.""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html",
        "points": 1,
        "answers": [
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(1) average case", "is_correct": True},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False},
        ],
    },
    {
        "text": """What happens when you use __slots__ in a Python class?""",
        "explanation": """__slots__ restricts instance attributes to only 
those specified and reduces memory usage by eliminating __dict__.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html",
        "points": 1,
        "answers": [
            {"text": "Increases memory usage", "is_correct": False},
            {"text": "Restricts attributes and reduces memory usage", 
             "is_correct": True},
            {"text": "Only affects method calls", "is_correct": False},
            {"text": "Enables multiple inheritance", "is_correct": False},
        ],
    },
    {
        "text": """What is the output of this iterator code?

```python
class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        self.start += 1
        return self.start - 1

counter = Counter(1, 4)
for i in counter:
    print(i, end=" ")
print("\\nSecond iteration:")
for i in counter:
    print(i, end=" ")
```""",
        "explanation": """After the first iteration, the iterator's state 
is exhausted (start=4). The second iteration finds start >= end 
immediately and yields nothing.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html",
        "points": 1,
        "answers": [
            {"text": "1 2 3 \\nSecond iteration:\\n1 2 3", "is_correct": False},
            {"text": "1 2 3 \\nSecond iteration:\\n", "is_correct": True},
            {"text": "1 2 3 4 \\nSecond iteration:\\n1 2 3 4", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """What is the purpose of the descriptor protocol in Python?""",
        "explanation": """Descriptors customize attribute access behavior 
through __get__, __set__, and __delete__ methods. Used by properties, 
methods, and static/class methods.""",
        "reference": "https://docs.python.org/3/howto/descriptor.html",
        "points": 1,
        "answers": [
            {"text": "Create new classes", "is_correct": False},
            {"text": "Customize attribute access behavior", "is_correct": True},
            {"text": "Handle exceptions", "is_correct": False},
            {"text": "Manage memory allocation", "is_correct": False},
        ],
    },
    {
        "text": """What is the difference between asyncio.gather() and asyncio.wait()?""",
        "explanation": """gather() preserves order and returns results, 
while wait() returns (done, pending) sets with more control options 
over completion behavior.""",
        "reference": "https://docs.python.org/3/library/asyncio-task.html",
        "points": 1,
        "answers": [
            {"text": "No difference, just aliases", "is_correct": False},
            {"text": "gather() preserves order, wait() gives more control", 
             "is_correct": True},
            {"text": "wait() is faster than gather()", "is_correct": False},
            {"text": "gather() only works with coroutines", "is_correct": False},
        ],
    },
    {
        "text": """What is the output of this property code?

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
    
    @area.setter
    def area(self, value):
        self._radius = (value / 3.14159) ** 0.5

c = Circle(5)
print(f"{c.area:.2f}")
c.area = 50
print(f"{c._radius:.2f}")
```""",
        "explanation": """Properties allow computed attributes. The getter 
calculates area from radius. The setter calculates radius from area.""",
        "reference": "https://docs.python.org/3/library/functions.html#property",
        "points": 1,
        "answers": [
            {"text": "78.54\\n3.99", "is_correct": True},
            {"text": "25.00\\n5.00", "is_correct": False},
            {"text": "78.54\\n5.00", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """What is method resolution order (MRO) in Python?""",
        "explanation": """MRO determines the order in which base classes 
are searched when executing a method. Python uses C3 linearization 
algorithm for MRO.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html",
        "points": 1,
        "answers": [
            {"text": "Random order of method calls", "is_correct": False},
            {"text": "Order of method definition", "is_correct": False},
            {"text": "Order of base class search for methods", "is_correct": True},
            {"text": "Alphabetical order of methods", "is_correct": False},
        ],
    },
    {
        "text": """What is the purpose of __new__ vs __init__ in Python classes?""",
        "explanation": """__new__ creates and returns the instance object, 
while __init__ initializes the already created instance. __new__ is 
called first.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html",
        "points": 1,
        "answers": [
            {"text": "__new__ initializes, __init__ creates", "is_correct": False},
            {"text": "__new__ creates instance, __init__ initializes it", 
             "is_correct": True},
            {"text": "They do the same thing", "is_correct": False},
            {"text": "__init__ is called first", "is_correct": False},
        ],
    },
    {
        "text": """What is a closure in Python?""",
        "explanation": """A closure is a function that captures and retains 
access to variables from its enclosing scope, even after the outer 
function returns.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html",
        "points": 1,
        "answers": [
            {"text": "A function inside another function", "is_correct": False},
            {"text": "A function that captures outer scope variables", 
             "is_correct": True},
            {"text": "A recursive function", "is_correct": False},
            {"text": "A function with no parameters", "is_correct": False},
        ],
    },
    {
        "text": """What is the difference between @staticmethod and @classmethod?""",
        "explanation": """@staticmethod doesn't receive any automatic 
arguments. @classmethod receives the class as first argument (cls). 
Both don't require instances.""",
        "reference": "https://docs.python.org/3/library/functions.html",
        "points": 1,
        "answers": [
            {"text": "No difference", "is_correct": False},
            {"text": "staticmethod has no automatic args, classmethod gets cls", 
             "is_correct": True},
            {"text": "staticmethod gets cls, classmethod gets self", 
             "is_correct": False},
            {"text": "Only staticmethod can be inherited", "is_correct": False},
        ],
    },
    {
        "text": """What is the Global Interpreter Lock (GIL) in Python?""",
        "explanation": """The GIL is a mutex that prevents multiple native 
threads from executing Python bytecode simultaneously, limiting 
true parallelism in CPU-bound tasks.""",
        "reference": "https://docs.python.org/3/glossary.html#term-GIL",
        "points": 1,
        "answers": [
            {"text": "A security feature", "is_correct": False},
            {"text": "A lock limiting thread parallelism", "is_correct": True},
            {"text": "A memory management tool", "is_correct": False},
            {"text": "A debugging feature", "is_correct": False},
        ],
    },
    {
        "text": """What is the difference between shallow copy and deep copy?""",
        "explanation": """Shallow copy creates a new object but inserts 
references to objects in the original. Deep copy creates new objects 
recursively.""",
        "reference": "https://docs.python.org/3/library/copy.html",
        "points": 1,
        "answers": [
            {"text": "No difference", "is_correct": False},
            {"text": "Shallow copies references, deep copies recursively", 
             "is_correct": True},
            {"text": "Deep copy is faster", "is_correct": False},
            {"text": "Shallow copy creates new nested objects", "is_correct": False},
        ],
    },
    {
        "text": """What is monkey patching in Python?""",
        "explanation": """Monkey patching is dynamically modifying a class 
or module at runtime by adding, modifying, or deleting attributes 
or methods.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html",
        "points": 1,
        "answers": [
            {"text": "A testing technique", "is_correct": False},
            {"text": "Dynamically modifying classes/modules at runtime", 
             "is_correct": True},
            {"text": "A debugging method", "is_correct": False},
            {"text": "Error handling mechanism", "is_correct": False},
        ],
    },
    {
        "text": """What is the purpose of __call__ method in Python classes?""",
        "explanation": """__call__ makes instances of a class callable 
like functions. When you call obj(), Python calls obj.__call__().""",
        "reference": "https://docs.python.org/3/reference/datamodel.html",
        "points": 1,
        "answers": [
            {"text": "Initialize the object", "is_correct": False},
            {"text": "Make instances callable like functions", "is_correct": True},
            {"text": "Handle method calls", "is_correct": False},
            {"text": "Create new instances", "is_correct": False},
        ],
    },
    {
        "text": """What is the difference between *args and **kwargs?""",
        "explanation": """*args collects extra positional arguments into 
a tuple. **kwargs collects extra keyword arguments into a dictionary.""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html",
        "points": 1,
        "answers": [
            {"text": "*args for keywords, **kwargs for positional", 
             "is_correct": False},
            {"text": "*args for positional, **kwargs for keywords", 
             "is_correct": True},
            {"text": "They do the same thing", "is_correct": False},
            {"text": "**kwargs is for classes only", "is_correct": False},
        ],
    },
]