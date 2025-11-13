"""JavaScript Fundamentals Certification"""

CERTIFICATION = {
    "name": "JavaScript Fundamentals",
    "description": "JavaScript Certified Entry-level Developer",
    "slug": "javascript-fundamentals",
    "level": "Entry",
    "duration": 45,
    "questions_count": 40,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is JavaScript?",
        "explanation": """# JavaScript Programming Language

**JavaScript** is a high-level, interpreted programming language that was originally created to make web pages interactive.

## Key Features:
- **Interpreted**: Runs directly in browsers or Node.js
- **Dynamic**: Variables can change types at runtime
- **Object-oriented**: Supports objects and classes
- **Functional**: Supports functional programming concepts

## Examples:

### 1. Simple Program
```javascript
console.log("Hello, World!");
// Output: Hello, World!
```

### 2. Variables and Data Types
```javascript
let name = "Alice";         // String
let age = 25;              // Number
let height = 5.6;          // Number (no separate float type)
let isStudent = true;      // Boolean

console.log(`Name: ${name}, Age: ${age}`);
// Output: Name: Alice, Age: 25
```

### 3. Basic Operations
```javascript
// Arithmetic
let x = 10 + 5;    // 15
let y = 20 - 8;    // 12
let z = 4 * 3;     // 12

// String operations
let greeting = "Hello" + " " + "World";
console.log(greeting);  // Hello World
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction",
        "points": 1,
        "answers": [
            {"text": "A programming language for web development", "is_correct": True},
            {"text": "A database management system", "is_correct": False},
            {"text": "An operating system", "is_correct": False},
            {"text": "A web browser", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of console.log(Boolean(0))?",
        "explanation": """# Boolean Values in JavaScript

**Boolean(0)** returns false because 0 is considered a **falsy** value in JavaScript.

## Falsy Values:
- `false`, `0`, `-0`, `0n`
- Empty strings: `""`, `''`
- `null`, `undefined`, `NaN`

## Truthy Values:
- `true`, any non-zero number
- Non-empty strings: `"hello"`, `"false"`
- Objects, arrays (even empty ones)

## Examples:

### 1. Boolean Conversion
```javascript
console.log(Boolean(0));        // false
console.log(Boolean(1));        // true
console.log(Boolean(-5));       // true
console.log(Boolean(""));       // false
console.log(Boolean("hello"));  // true
```

### 2. Implicit Conversion
```javascript
if (0) {
    console.log("This won't run");
} else {
    console.log("0 is falsy");
}

if ("hello") {
    console.log("Strings are truthy");
}
```

### 3. Practical Usage
```javascript
let numbers = [1, 2, 3, 4, 5];

if (numbers.length) {  // Checks if array has items
    console.log("Array has items");
} else {
    console.log("Array is empty");
}
// Output: Array has items
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Glossary/Truthy",
        "points": 1,
        "answers": [
            {"text": "true", "is_correct": False},
            {"text": "false", "is_correct": True},
            {"text": "0", "is_correct": False},
            {"text": "undefined", "is_correct": False},
        ],
    },
    {
        "text": "Which method adds an element to the end of an array?",
        "explanation": """# Array Methods in JavaScript

**push()** method adds one or more elements to the end of an array and returns the new length.

## Common Array Methods:
- `push()` - Add elements to end
- `pop()` - Remove last element
- `unshift()` - Add elements to beginning
- `shift()` - Remove first element

## Examples:

### 1. Using push()
```javascript
let fruits = ["apple", "banana"];
fruits.push("orange");
console.log(fruits);  // ["apple", "banana", "orange"]

// Push multiple elements
let numbers = [1, 2, 3];
numbers.push(4, 5, 6);
console.log(numbers);  // [1, 2, 3, 4, 5, 6]

// Returns new length
let length = fruits.push("grape");
console.log(length);  // 4
```

### 2. Other Array Methods
```javascript
let colors = ["red", "blue"];

// Add to beginning
colors.unshift("green");
console.log(colors);  // ["green", "red", "blue"]

// Remove from end
let lastColor = colors.pop();
console.log(lastColor);  // "blue"
console.log(colors);     // ["green", "red"]

// Remove from beginning
let firstColor = colors.shift();
console.log(firstColor); // "green"
```

### 3. Method Chaining
```javascript
let result = [1, 2, 3]
    .push(4)           // Add 4
    .map(x => x * 2);  // Double each number
// Note: push() returns length, not array, so this won't work
// Better approach:
let arr = [1, 2, 3];
arr.push(4);
result = arr.map(x => x * 2);  // [2, 4, 6, 8]
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push",
        "points": 1,
        "answers": [
            {"text": "add()", "is_correct": False},
            {"text": "push()", "is_correct": True},
            {"text": "append()", "is_correct": False},
            {"text": "insert()", "is_correct": False},
        ],
    },
    {
        "text": "What does the length property return?",
        "explanation": """# Length Property in JavaScript

The **length** property returns the number of elements in an array or characters in a string.

## Works with:
- Arrays, strings, and other array-like objects
- Returns a number representing the count

## Examples:

### 1. String Length
```javascript
let text = "Hello World";
console.log(text.length);  // 11 (includes space)

let name = "JavaScript";
console.log(name.length);  // 10
```

### 2. Array Length
```javascript
let numbers = [1, 2, 3, 4, 5];
console.log(numbers.length);  // 5

let emptyArray = [];
console.log(emptyArray.length);  // 0
```

### 3. Modifying Array Length
```javascript
let arr = [1, 2, 3, 4, 5];
console.log(arr.length);  // 5

// Truncate array
arr.length = 3;
console.log(arr);  // [1, 2, 3]

// Extend array (fills with undefined)
arr.length = 5;
console.log(arr);  // [1, 2, 3, undefined, undefined]
```

### 4. Practical Usage
```javascript
// Check if array is empty
let items = [];
if (items.length === 0) {
    console.log("No items found");
}

// Loop through array
let words = ["hello", "world", "javascript"];
for (let i = 0; i < words.length; i++) {
    console.log(`${i}: ${words[i]}`);
}

// Get last element
let lastItem = words[words.length - 1];
console.log(lastItem);  // "javascript"
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length",
        "points": 1,
        "answers": [
            {"text": "The length of an array or string", "is_correct": True},
            {"text": "The type of an object", "is_correct": False},
            {"text": "The value of an object", "is_correct": False},
            {"text": "The memory address", "is_correct": False},
        ],
    },
    {
        "text": "What is the correct way to create a comment in JavaScript?",
        "explanation": """# Comments in JavaScript

**Comments** in JavaScript can be single-line (`//`) or multi-line (`/* */`).

## Types of Comments:

### 1. Single-line Comments
```javascript
// This is a single-line comment
console.log("Hello World");  // This is also a comment

// You can have multiple single-line comments
// Each line needs its own // symbols
let x = 5;  // Variable declaration
```

### 2. Multi-line Comments
```javascript
/*
This is a multi-line comment
that spans multiple lines
*/

let y = 10; /* This can also be inline */

/*
Multi-line comments are useful for:
- Longer explanations
- Temporarily disabling code blocks
- Documentation headers
*/
```

### 3. JSDoc Comments (Documentation)
```javascript
/**
 * Calculates the area of a rectangle
 * @param {number} width - The width of the rectangle
 * @param {number} height - The height of the rectangle
 * @returns {number} The area of the rectangle
 */
function calculateArea(width, height) {
    return width * height;
}
```

### 4. Commenting Best Practices
```javascript
// Good: Explain WHY, not WHAT
let totalPrice = price * taxRate;  // Apply local tax rate

// Bad: Just repeating what code does
x = x + 1;  // Add 1 to x

// Good: Explain complex logic
// Calculate compound interest using A = P(1+r/n)^(nt)
let amount = principal * Math.pow(1 + rate/frequency, frequency * time);

// Temporary disable code
/*
if (debugMode) {
    console.log("Debug info");
}
*/
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_Types#comments",
        "points": 1,
        "answers": [
            {"text": "<!-- This is a comment -->", "is_correct": False},
            {"text": "# This is a comment", "is_correct": False},
            {"text": "// This is a comment", "is_correct": True},
            {"text": "' This is a comment", "is_correct": False},
        ],
    },
    {
        "text": "Which of the following is a valid JavaScript variable name?",
        "explanation": """# JavaScript Variable Naming Rules

**Valid variable names** in JavaScript must follow specific rules and conventions.

## Rules (Required):
- Must start with letter (a-z, A-Z), underscore (_), or dollar sign ($)
- Can contain letters, numbers, underscores, and dollar signs
- Case-sensitive
- Cannot be JavaScript keywords

## Examples:

### 1. Valid Names
```javascript
let name = "Alice";           // lowercase
let firstName = "Bob";        // camelCase (preferred)
let first_name = "Charlie";   // snake_case (less common)
let _private = "secret";      // starts with underscore
let $element = document;      // starts with dollar sign
let age2 = 25;               // contains numbers
const MAX_SIZE = 100;        // constants (all uppercase)
```

### 2. Invalid Names
```javascript
// These will cause SyntaxError:
// let 2name = "invalid";        // starts with number
// let first-name = "invalid";   // contains hyphen
// let class = "invalid";        // JavaScript keyword
// let first name = "invalid";   // contains space
```

### 3. JavaScript Keywords (Reserved)
```javascript
// Reserved words that cannot be used as variable names:
// break, case, catch, class, const, continue, debugger, default,
// delete, do, else, export, extends, finally, for, function,
// if, import, in, instanceof, let, new, return, super, switch,
// this, throw, try, typeof, var, void, while, with, yield
```

### 4. Naming Conventions
```javascript
// Variables and functions: camelCase
let userAge = 25;
function calculateTotal() {
    return 100;
}

// Constants: ALL_CAPS
const PI = 3.14159;
const MAX_RETRIES = 5;

// Classes: PascalCase
class StudentRecord {
    constructor(name) {
        this.name = name;
    }
}

// Private-like variables: underscore prefix
let _internalValue = 42;
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_Types#variables",
        "points": 1,
        "answers": [
            {"text": "2name", "is_correct": False},
            {"text": "first-name", "is_correct": False},
            {"text": "firstName", "is_correct": True},
            {"text": "class", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of console.log(typeof 3.14)?",
        "explanation": """# Data Types in JavaScript

**typeof** operator returns the data type of a value. `3.14` is a **number** in JavaScript.

## Basic Data Types:

### 1. Primitive Types
```javascript
console.log(typeof 42);        // "number"
console.log(typeof 3.14);      // "number"
console.log(typeof "Hello");   // "string"
console.log(typeof true);      // "boolean"
console.log(typeof undefined); // "undefined"
console.log(typeof null);      // "object" (this is a known quirk!)
console.log(typeof Symbol());  // "symbol"
console.log(typeof BigInt(123)); // "bigint"
```

### 2. Non-Primitive Types
```javascript
console.log(typeof {});        // "object"
console.log(typeof []);        // "object" (arrays are objects)
console.log(typeof function(){}); // "function"
console.log(typeof new Date()); // "object"
console.log(typeof /regex/);   // "object"
```

### 3. Number Type Details
```javascript
// JavaScript has only one number type
console.log(typeof 42);     // "number"
console.log(typeof 3.14);   // "number"
console.log(typeof -17);    // "number"
console.log(typeof Infinity); // "number"
console.log(typeof NaN);    // "number" (Not a Number is still type number!)
```

### 4. Type Checking
```javascript
let x = 3.14;
console.log(typeof x === "number");  // true

// More specific checks
console.log(Number.isInteger(42));   // true
console.log(Number.isInteger(3.14)); // false
console.log(Number.isNaN(NaN));      // true
console.log(Number.isFinite(42));    // true
```

### 5. Type Conversion
```javascript
console.log(typeof String(123));    // "string" - "123"
console.log(typeof Number("456"));  // "number" - 456
console.log(typeof Boolean(1));     // "boolean" - true
console.log(typeof parseInt("78")); // "number" - 78
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof",
        "points": 1,
        "answers": [
            {"text": "\"float\"", "is_correct": False},
            {"text": "\"number\"", "is_correct": True},
            {"text": "\"decimal\"", "is_correct": False},
            {"text": "\"double\"", "is_correct": False},
        ],
    },
    {
        "text": "Which operator is used for string concatenation in JavaScript?",
        "explanation": """# String Concatenation in JavaScript

**+ operator** is used to concatenate (join) strings in JavaScript, along with template literals.

## String Operations:

### 1. Basic Concatenation with +
```javascript
let firstName = "John";
let lastName = "Doe";
let fullName = firstName + " " + lastName;
console.log(fullName);  // John Doe

let greeting = "Hello" + " " + "World";
console.log(greeting);  // Hello World
```

### 2. Template Literals (ES6+)
```javascript
let name = "Alice";
let age = 25;
let message = `My name is ${name} and I am ${age} years old`;
console.log(message);  // My name is Alice and I am 25 years old

// Multi-line strings
let multiline = `
    This is a
    multi-line
    string
`;
```

### 3. Multiple Concatenations
```javascript
let result = "JavaScript" + " " + "is" + " " + "awesome";
console.log(result);  // JavaScript is awesome

// With variables
let language = "JavaScript";
let adjective = "powerful";
let sentence = language + " is " + adjective + "!";
console.log(sentence);  // JavaScript is powerful!
```

### 4. Alternative Methods
```javascript
// Using Array.join()
let words = ["JavaScript", "is", "great"];
let sentence = words.join(" ");  // JavaScript is great

// Using concat() method
let str1 = "Hello";
let str2 = " World";
let result = str1.concat(str2);  // Hello World
```

### 5. Type Coercion with +
```javascript
// Automatic string conversion
let result = "Age: " + 25;
console.log(result);  // "Age: 25"

let mixed = "5" + 3;
console.log(mixed);   // "53" (string concatenation, not addition)

// To force addition:
let sum = Number("5") + 3;  // 8
// or
let sum2 = +"5" + 3;        // 8 (unary + converts to number)
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_concatenation",
        "points": 1,
        "answers": [
            {"text": "&", "is_correct": False},
            {"text": "+", "is_correct": True},
            {"text": "*", "is_correct": False},
            {"text": ".", "is_correct": False},
        ],
    },
    {
        "text": "What will be the output of console.log(Math.floor(5.7))?",
        "explanation": """# Math.floor() Method in JavaScript

**Math.floor()** returns the largest integer less than or equal to a given number (rounds down).

## Math Methods:

### 1. Math.floor() - Round Down
```javascript
console.log(Math.floor(5.7));    // 5
console.log(Math.floor(5.1));    // 5
console.log(Math.floor(5.9));    // 5
console.log(Math.floor(-5.1));   // -6 (rounds down toward negative infinity)
```

### 2. Related Math Methods
```javascript
// Math.ceil() - Round Up
console.log(Math.ceil(5.1));     // 6
console.log(Math.ceil(5.9));     // 6
console.log(Math.ceil(-5.1));    // -5

// Math.round() - Round to Nearest
console.log(Math.round(5.4));    // 5
console.log(Math.round(5.5));    // 6
console.log(Math.round(5.6));    // 6

// Math.trunc() - Remove Decimal Part
console.log(Math.trunc(5.9));    // 5
console.log(Math.trunc(-5.9));   // -5
```

### 3. Practical Examples
```javascript
// Calculate pages needed for pagination
let totalItems = 23;
let itemsPerPage = 5;
let pages = Math.ceil(totalItems / itemsPerPage);
console.log(`Need ${pages} pages`);  // Need 5 pages

// Round down to nearest 10
let price = 47.99;
let roundedDown = Math.floor(price / 10) * 10;
console.log(roundedDown);  // 40

// Generate random integer between 1 and 6 (dice)
let dice = Math.floor(Math.random() * 6) + 1;
console.log(dice);  // Random number: 1, 2, 3, 4, 5, or 6
```

### 4. Working with Time
```javascript
// Convert milliseconds to seconds (round down)
let milliseconds = 5750;
let seconds = Math.floor(milliseconds / 1000);
console.log(seconds);  // 5

// Age calculation (round down)
let birthYear = 1995;
let currentYear = 2023;
let age = Math.floor((currentYear - birthYear));
console.log(age);  // 28
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor",
        "points": 1,
        "answers": [
            {"text": "5.7", "is_correct": False},
            {"text": "5", "is_correct": True},
            {"text": "6", "is_correct": False},
            {"text": "6.0", "is_correct": False},
        ],
    },
    {
        "text": "Which keyword is used to define a function in JavaScript?",
        "explanation": """# Function Definition in JavaScript

**function** keyword is used to define functions in JavaScript, along with arrow functions and function expressions.

## Function Declaration Syntax:
```javascript
function functionName(parameters) {
    // Function body
    return value;  // Optional
}
```

## Examples:

### 1. Simple Function
```javascript
function greet() {
    console.log("Hello, World!");
}

greet();  // Call the function
// Output: Hello, World!
```

### 2. Function with Parameters
```javascript
function greetPerson(name) {
    console.log(`Hello, ${name}!`);
}

greetPerson("Alice");  // Hello, Alice!
greetPerson("Bob");    // Hello, Bob!
```

### 3. Function with Return Value
```javascript
function addNumbers(a, b) {
    let result = a + b;
    return result;
}

let sum = addNumbers(5, 3);
console.log(sum);  // 8
```

### 4. Function Expression
```javascript
const multiply = function(a, b) {
    return a * b;
};

console.log(multiply(4, 5));  // 20
```

### 5. Arrow Functions (ES6+)
```javascript
// Arrow function syntax
const divide = (a, b) => {
    return a / b;
};

// Shorter arrow function for simple expressions
const square = x => x * x;
const add = (a, b) => a + b;

console.log(square(5));    // 25
console.log(add(3, 4));    // 7
```

### 6. Function with Default Parameters
```javascript
function introduce(name, age = 25) {
    return `My name is ${name} and I am ${age} years old`;
}

console.log(introduce("Alice"));         // Uses default age
console.log(introduce("Bob", 30));       // Uses provided age
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions",
        "points": 1,
        "answers": [
            {"text": "def", "is_correct": False},
            {"text": "function", "is_correct": True},
            {"text": "func", "is_correct": False},
            {"text": "define", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of console.log([1, 2, 3])?",
        "explanation": """# Array Output in JavaScript

**Arrays** are displayed as comma-separated values in square brackets when logged to the console.

## Array Display:

### 1. Basic Array Logging
```javascript
console.log([1, 2, 3]);        // [1, 2, 3]
console.log(["a", "b", "c"]);  // ['a', 'b', 'c']
console.log([]);               // []
```

### 2. Mixed Data Types
```javascript
let mixedArray = [1, "hello", true, null];
console.log(mixedArray);  // [1, 'hello', true, null]

let nestedArray = [1, [2, 3], 4];
console.log(nestedArray);  // [1, [2, 3], 4]
```

### 3. Array Properties and Methods
```javascript
let numbers = [1, 2, 3];
console.log(numbers.length);     // 3
console.log(numbers[0]);         // 1 (first element)
console.log(numbers[numbers.length - 1]); // 3 (last element)

// Array methods
console.log(numbers.join(", "));  // "1, 2, 3"
console.log(numbers.toString());  // "1,2,3"
```

### 4. Array vs String Representation
```javascript
let arr = [1, 2, 3];
console.log(arr);              // [1, 2, 3] (array)
console.log(String(arr));      // "1,2,3" (string)
console.log(JSON.stringify(arr)); // "[1,2,3]" (JSON string)
```

### 5. Console Methods for Arrays
```javascript
let data = [
    {name: "Alice", age: 25},
    {name: "Bob", age: 30}
];

console.log(data);          // Standard array display
console.table(data);        // Table format in console
console.dir(data);          // Directory-style listing
```

### 6. Array Iteration
```javascript
let fruits = ["apple", "banana", "orange"];

// For loop
for (let i = 0; i < fruits.length; i++) {
    console.log(i, fruits[i]);
}

// For...of loop
for (let fruit of fruits) {
    console.log(fruit);
}

// forEach method
fruits.forEach((fruit, index) => {
    console.log(`${index}: ${fruit}`);
});
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array",
        "points": 1,
        "answers": [
            {"text": "[1, 2, 3]", "is_correct": True},
            {"text": "(1, 2, 3)", "is_correct": False},
            {"text": "1 2 3", "is_correct": False},
            {"text": "Array(3)", "is_correct": False},
        ],
    },
    {
        "text": "Which statement is used to exit from a loop in JavaScript?",
        "explanation": """# Loop Control Statements in JavaScript

**break** statement is used to exit/terminate a loop immediately.

## Loop Control Keywords:
- `break` - Exit loop completely
- `continue` - Skip current iteration, continue with next
- `return` - Exit function (and any loops within)

## Examples:

### 1. Using break
```javascript
// Exit loop when condition met
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break;
    }
    console.log(i);
}
// Output: 0, 1, 2, 3, 4

// Search and exit
let numbers = [1, 3, 7, 2, 9, 5];
let target = 7;
for (let num of numbers) {
    if (num === target) {
        console.log(`Found ${target}!`);
        break;
    }
}
```

### 2. Using continue
```javascript
// Skip even numbers
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {
        continue;  // Skip rest of loop body
    }
    console.log(i);
}
// Output: 1, 3, 5, 7, 9

// Process only valid data
let data = [1, -2, 3, 0, 5, -1];
for (let value of data) {
    if (value <= 0) {
        continue;  // Skip negative/zero values
    }
    console.log(`Processing: ${value}`);
}
```

### 3. Nested Loops with break
```javascript
// Break only exits innermost loop
for (let i = 0; i < 3; i++) {
    console.log(`Outer loop: ${i}`);
    for (let j = 0; j < 3; j++) {
        if (j === 1) {
            break;  // Only breaks inner loop
        }
        console.log(`  Inner loop: ${j}`);
    }
}

// To break outer loop, use labeled break
outerLoop: for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        if (i === 1 && j === 1) {
            break outerLoop;  // Breaks outer loop
        }
        console.log(`${i}, ${j}`);
    }
}
```

### 4. While Loop with break
```javascript
let count = 0;
while (true) {  // Infinite loop
    count++;
    console.log(count);
    if (count >= 5) {
        break;  // Exit the loop
    }
}
// Output: 1, 2, 3, 4, 5
```

### 5. Switch Statement break
```javascript
let day = "Monday";
switch (day) {
    case "Monday":
        console.log("Start of work week");
        break;  // Prevents fall-through
    case "Friday":
        console.log("End of work week");
        break;
    default:
        console.log("Regular day");
}
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break",
        "points": 1,
        "answers": [
            {"text": "exit", "is_correct": False},
            {"text": "break", "is_correct": True},
            {"text": "stop", "is_correct": False},
            {"text": "end", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of console.log('JavaScript'[0])?",
        "explanation": """# String Indexing in JavaScript

**String indexing** uses square brackets to access individual characters. JavaScript uses **zero-based indexing**.

## String Indexing:

### 1. Positive Indexing
```javascript
let text = "JavaScript";
console.log(text[0]);    // 'J' - First character
console.log(text[1]);    // 'a' - Second character
console.log(text[2]);    // 'v' - Third character
console.log(text[9]);    // 't' - Last character
```

### 2. Accessing Characters
```javascript
let text = "JavaScript";
console.log(text[0]);               // 'J'
console.log(text.charAt(0));        // 'J' (alternative method)
console.log(text.charAt(100));      // '' (empty string for out of bounds)
console.log(text[100]);             // undefined (for out of bounds)
```

### 3. String Slicing
```javascript
let text = "JavaScript";
console.log(text.slice(0, 4));      // 'Java' - Characters 0-3
console.log(text.slice(4));         // 'Script' - From index 4 to end
console.log(text.slice(-6));        // 'Script' - Last 6 characters
console.log(text.slice(-6, -2));    // 'Scri' - From -6 to -2
```

### 4. String Substring Methods
```javascript
let text = "JavaScript";
console.log(text.substring(0, 4));  // 'Java'
console.log(text.substr(4, 6));     // 'Script' (deprecated)
console.log(text.slice(4, 10));     // 'Script'
```

### 5. Practical Examples
```javascript
let email = "user@example.com";
let atIndex = email.indexOf('@');
let username = email.slice(0, atIndex);     // 'user'
let domain = email.slice(atIndex + 1);      // 'example.com'

// Check file extension
let filename = "document.pdf";
let extension = filename.slice(-4);         // '.pdf'

// Get first and last characters
let word = "Hello";
let firstLast = word[0] + word[word.length - 1];  // 'Ho'

// Check if string starts with specific character
let text2 = "JavaScript";
if (text2[0] === 'J') {
    console.log("Starts with J");
}
```

### 6. String Immutability
```javascript
let text = "Hello";
text[0] = "h";  // This doesn't work - strings are immutable
console.log(text);  // Still "Hello"

// Create new string instead
let newText = "h" + text.slice(1);  // "hello"
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#character_access",
        "points": 1,
        "answers": [
            {"text": "'J'", "is_correct": True},
            {"text": "'a'", "is_correct": False},
            {"text": "'JavaScript'", "is_correct": False},
            {"text": "0", "is_correct": False},
        ],
    },
    {
        "text": "Which data structure is mutable in JavaScript?",
        "explanation": """# Mutable vs Immutable Data Structures in JavaScript

**Arrays** are mutable in JavaScript, meaning their contents can be changed after creation.

## Mutable Types (Can be changed):
- **Arrays** `[]`
- **Objects** `{}`
- **Functions** (properties can be added)

## Immutable Types (Cannot be changed):
- **Strings** `""`
- **Numbers**
- **Booleans**
- **null**, **undefined**

## Examples:

### 1. Arrays are Mutable
```javascript
// Arrays can be modified
let fruits = ["apple", "banana"];
fruits.push("orange");              // Add element
fruits[0] = "grape";                // Change element
fruits.pop();                       // Remove last element
console.log(fruits);  // ['grape', 'banana']

// Array methods that modify the original
fruits.splice(1, 0, "kiwi");        // Insert at index 1
fruits.sort();                      // Sort in place
fruits.reverse();                   // Reverse in place
```

### 2. Strings are Immutable
```javascript
// Strings cannot be modified
let text = "Hello";
text[0] = "h";  // This doesn't work
console.log(text);  // Still "Hello"

// Create new string instead
let newText = "h" + text.slice(1);  // "hello"
let upperText = text.toUpperCase(); // "HELLO" (creates new string)
```

### 3. Objects are Mutable
```javascript
let student = {name: "Alice", age: 20};
student.grade = "A";                // Add new property
student.age = 21;                   // Modify existing property
delete student.name;                // Remove property
console.log(student);  // {age: 21, grade: "A"}

// Nested objects
let person = {
    name: "Bob",
    address: {city: "New York", zip: "10001"}
};
person.address.city = "Boston";     // Modifies nested object
```

### 4. Reference vs Value
```javascript
// Arrays and objects are passed by reference
let arr1 = [1, 2, 3];
let arr2 = arr1;  // Both point to same array
arr2.push(4);
console.log(arr1);  // [1, 2, 3, 4] - Original array changed!

// Primitives are passed by value
let str1 = "hello";
let str2 = str1;  // Copy of the value
str2 = "world";   // Creates new string
console.log(str1);  // "hello" - Original unchanged
```

### 5. Avoiding Mutation
```javascript
// Create copies to avoid mutation
let original = [1, 2, 3];

// Shallow copy methods
let copy1 = [...original];          // Spread operator
let copy2 = Array.from(original);   // Array.from()
let copy3 = original.slice();       // slice() method

copy1.push(4);
console.log(original);  // [1, 2, 3] - Unchanged

// For objects
let originalObj = {name: "Alice", age: 25};
let copyObj = {...originalObj};     // Spread operator
let copyObj2 = Object.assign({}, originalObj);
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array",
        "points": 1,
        "answers": [
            {"text": "String", "is_correct": False},
            {"text": "Array", "is_correct": True},
            {"text": "Number", "is_correct": False},
            {"text": "Boolean", "is_correct": False},
        ],
    },
    {
        "text": "What keyword is used to check if a value exists in an array?",
        "explanation": """# Checking Array Membership in JavaScript

**includes()** method is commonly used to check if a value exists in an array, along with **indexOf()**.

## Array Membership Methods:

### 1. includes() Method (ES2016+)
```javascript
let numbers = [1, 2, 3, 4, 5];
console.log(numbers.includes(3));      // true
console.log(numbers.includes(6));      // false

let colors = ["red", "blue", "green"];
console.log(colors.includes("blue"));  // true
console.log(colors.includes("yellow")); // false
```

### 2. indexOf() Method
```javascript
let fruits = ["apple", "banana", "orange"];
console.log(fruits.indexOf("banana"));     // 1 (index position)
console.log(fruits.indexOf("grape"));      // -1 (not found)

// Check existence
if (fruits.indexOf("apple") !== -1) {
    console.log("Apple found!");
}
```

### 3. find() and findIndex() Methods
```javascript
let users = [
    {name: "Alice", age: 25},
    {name: "Bob", age: 30},
    {name: "Charlie", age: 35}
];

// Find object
let user = users.find(u => u.name === "Bob");
console.log(user);  // {name: "Bob", age: 30}

// Find index of object
let index = users.findIndex(u => u.age > 30);
console.log(index);  // 2 (Charlie's index)
```

### 4. some() Method
```javascript
let numbers = [1, 2, 3, 4, 5];

// Check if any element meets condition
let hasEven = numbers.some(num => num % 2 === 0);
console.log(hasEven);  // true

let hasLarge = numbers.some(num => num > 10);
console.log(hasLarge); // false
```

### 5. Practical Examples
```javascript
// Validate user input
let validChoices = ["yes", "no", "maybe"];
let userInput = "yes";
if (validChoices.includes(userInput)) {
    console.log("Valid choice");
}

// Check file extensions
let allowedExtensions = [".jpg", ".png", ".gif"];
let filename = "image.png";
let isAllowed = allowedExtensions.some(ext => filename.endsWith(ext));
console.log(isAllowed);  // true

// Filter arrays
let emails = ["user1@gmail.com", "user2@yahoo.com", "user3@gmail.com"];
let gmailUsers = emails.filter(email => email.includes("@gmail.com"));
console.log(gmailUsers);  // ['user1@gmail.com', 'user3@gmail.com']
```

### 6. String Contains Check
```javascript
let text = "JavaScript programming";
console.log(text.includes("Script"));     // true
console.log(text.includes("Python"));     // false

// Case sensitive
console.log(text.includes("javascript")); // false
console.log(text.toLowerCase().includes("javascript")); // true
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes",
        "points": 1,
        "answers": [
            {"text": "contains", "is_correct": False},
            {"text": "includes", "is_correct": True},
            {"text": "in", "is_correct": False},
            {"text": "has", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between '==' and '===' operators in JavaScript?",
        "explanation": """# Equality Operators in JavaScript

**==** performs type coercion and compares values, while **===** compares both value and type without coercion.

## Comparison Operators:

### 1. Loose Equality (==)
```javascript
console.log(5 == "5");        // true (string "5" converted to number)
console.log(true == 1);       // true (true converted to 1)
console.log(false == 0);      // true (false converted to 0)
console.log(null == undefined); // true (special case)
console.log(0 == "");         // true (empty string converted to 0)
```

### 2. Strict Equality (===)
```javascript
console.log(5 === "5");       // false (different types)
console.log(true === 1);      // false (different types)
console.log(false === 0);     // false (different types)
console.log(null === undefined); // false (different types)
console.log(0 === "");        // false (different types)
console.log(5 === 5);         // true (same type and value)
```

### 3. Type Coercion Examples
```javascript
// Loose equality with type coercion
console.log("5" == 5);        // true
console.log([1] == 1);        // true (array converted to primitive)
console.log([1,2] == "1,2");  // true (array.toString())
console.log({} == "[object Object]"); // true

// Strict equality without coercion
console.log("5" === 5);       // false
console.log([1] === 1);       // false
console.log([1,2] === "1,2"); // false
```

### 4. Best Practices
```javascript
// Recommended: Use strict equality
let userAge = "25";
if (userAge === "25") {       // Check for exact string match
    console.log("User age is string 25");
}

if (Number(userAge) === 25) { // Convert then compare
    console.log("User age is number 25");
}

// Avoid loose equality for clarity
// if (userAge == 25) { }     // Unclear intent
```

### 5. Inequality Operators
```javascript
// Loose inequality
console.log(5 != "5");        // false (values are equal after coercion)
console.log(5 != 3);          // true

// Strict inequality
console.log(5 !== "5");       // true (different types)
console.log(5 !== 5);         // false (same type and value)
```

### 6. Common Gotchas
```javascript
// Surprising results with ==
console.log(0 == false);      // true
console.log("" == false);     // true
console.log([] == false);     // true
console.log([] == "");        // true
console.log("0" == false);    // true

// But:
console.log(false == "false"); // false!
console.log(0 == null);       // false!

// Always use === for predictable results
console.log(0 === false);     // false
console.log("" === false);    // false
console.log([] === false);    // false
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness",
        "points": 1,
        "answers": [
            {"text": "No difference", "is_correct": False},
            {"text": "=== is stricter and doesn't perform type coercion", "is_correct": True},
            {"text": "== is stricter", "is_correct": False},
            {"text": "They work only with numbers", "is_correct": False},
        ],
    },
]