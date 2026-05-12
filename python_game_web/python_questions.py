"""Question bank for Python Quest.

Questions are kept in this separate file so they can be edited or expanded
without changing the main game logic.
"""

from models import BossLevel, Level, Question


def make_question(text, options, correct_answer, explanation, topic):
    """Small helper to keep the question list easy to read."""
    return Question(text, options, correct_answer, explanation, topic)


def get_levels():
    """Create and return all game levels."""
    return [
        Level(
            1,
            "Syntax Basics",
            [
                make_question(
                    "Which symbol is used to write a comment in Python?",
                    {"A": "//", "B": "#", "C": "/* */", "D": "<!-- -->"},
                    "B",
                    "Python uses # for single-line comments.",
                    "basic syntax",
                ),
                make_question(
                    "Which line correctly prints Hello in Python?",
                    {"A": "print('Hello')", "B": "echo 'Hello'", "C": "Console.WriteLine('Hello')", "D": "printf('Hello')"},
                    "A",
                    "print() is the built-in Python function for output.",
                    "basic syntax",
                ),
                make_question(
                    "Which variable name is valid in Python?",
                    {"A": "2score", "B": "player-score", "C": "player_score", "D": "class"},
                    "C",
                    "Variable names can contain letters, numbers, and underscores, but cannot start with a number or use keywords.",
                    "basic syntax",
                ),
            ],
            "Syntax Starter",
        ),
        Level(
            2,
            "Loops and Conditionals",
            [
                make_question(
                    "What keyword starts a conditional statement?",
                    {"A": "if", "B": "when", "C": "check", "D": "condition"},
                    "A",
                    "Python uses if, elif, and else for conditional logic.",
                    "control structures",
                ),
                make_question(
                    "Which loop is best when you know you want to repeat once for every item in a list?",
                    {"A": "if loop", "B": "for loop", "C": "try loop", "D": "def loop"},
                    "B",
                    "A for loop is commonly used to iterate through items in a sequence.",
                    "loops",
                ),
                make_question(
                    "What does break do inside a loop?",
                    {"A": "Skips the current item only", "B": "Ends the loop immediately", "C": "Creates a function", "D": "Deletes the loop variable"},
                    "B",
                    "break exits the nearest loop immediately.",
                    "loops",
                ),
            ],
            "Control Hero",
        ),
        Level(
            3,
            "Functions",
            [
                make_question(
                    "Which keyword is used to define a function in Python?",
                    {"A": "function", "B": "def", "C": "func", "D": "method"},
                    "B",
                    "Python uses def to define a function.",
                    "functions",
                ),
                make_question(
                    "What does a return statement do?",
                    {"A": "Displays text only", "B": "Stops the whole program", "C": "Sends a value back from a function", "D": "Imports a module"},
                    "C",
                    "return gives a result back to the code that called the function.",
                    "functions",
                ),
                make_question(
                    "In def add(a, b), what are a and b called?",
                    {"A": "Parameters", "B": "Strings", "C": "Loops", "D": "Files"},
                    "A",
                    "Parameters are named inputs used by a function.",
                    "functions",
                ),
            ],
            "Function Builder",
        ),
        Level(
            4,
            "Data Structures",
            [
                make_question(
                    "Which data structure stores key-value pairs?",
                    {"A": "List", "B": "Tuple", "C": "Dictionary", "D": "Set"},
                    "C",
                    "A dictionary stores data as keys linked to values.",
                    "dictionaries",
                ),
                make_question(
                    "Which data structure is ordered and cannot be changed after creation?",
                    {"A": "List", "B": "Tuple", "C": "Dictionary", "D": "Set"},
                    "B",
                    "A tuple is ordered and immutable.",
                    "tuples",
                ),
                make_question(
                    "Which data structure automatically avoids duplicate items?",
                    {"A": "List", "B": "Tuple", "C": "String", "D": "Set"},
                    "D",
                    "A set stores unique items.",
                    "sets",
                ),
                make_question(
                    "Which method adds one item to the end of a list?",
                    {"A": "append()", "B": "add_key()", "C": "push_front()", "D": "insert_all()"},
                    "A",
                    "append() adds one item to the end of a list.",
                    "lists",
                ),
            ],
            "Data Collector",
        ),
        BossLevel(
            5,
            "OOP Boss Battle",
            [
                make_question(
                    "What is a class in Python?",
                    {"A": "A blueprint for creating objects", "B": "Only a type of loop", "C": "A JSON file", "D": "A password"},
                    "A",
                    "A class is a blueprint that defines data and behavior for objects.",
                    "OOP",
                ),
                make_question(
                    "What is an object?",
                    {"A": "An instance of a class", "B": "A syntax error", "C": "A type of comment", "D": "Only a number"},
                    "A",
                    "An object is created from a class.",
                    "objects",
                ),
                make_question(
                    "What does inheritance allow one class to do?",
                    {"A": "Read a text file", "B": "Receive attributes and methods from another class", "C": "Run forever", "D": "Avoid all errors"},
                    "B",
                    "Inheritance lets a child class reuse and extend code from a parent class.",
                    "inheritance",
                ),
                make_question(
                    "Which block is used to handle exceptions?",
                    {"A": "for/while", "B": "try/except", "C": "class/object", "D": "list/set"},
                    "B",
                    "try/except lets a program handle errors without crashing.",
                    "exception handling",
                ),
                make_question(
                    "Which function can open a file in Python?",
                    {"A": "open()", "B": "file()", "C": "readfile()", "D": "startfile()"},
                    "A",
                    "open() is used to open files for reading or writing.",
                    "file IO",
                ),
            ],
            "OOP Champion",
        ),
    ]
