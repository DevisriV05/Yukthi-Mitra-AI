question_bank_python = [
    # Basics
    {"question": "Which keyword is used to start a Python program script?", "options": ["start", "main", "def", "None of these"], "answer": "None of these", "topic": "Basics"},
    {"question": "Which symbol is used to comment a single line?", "options": ["//", "#", "/* */", "--"], "answer": "#", "topic": "Basics"},
    {"question": "Which function is used to take input from the user?", "options": ["input()", "scan()", "read()", "get()"], "answer": "input()", "topic": "Basics"},

    # Data types
    {"question": "The output type of 3 / 2 in Python is:", "options": ["int", "float", "string", "bool"], "answer": "float", "topic": "Data Types"},
    {"question": "Which of the following is an immutable data type?", "options": ["list", "set", "dictionary", "tuple"], "answer": "tuple", "topic": "Data Types"},
    {"question": "Which keyword is used to define a dictionary?", "options": ["()", "[]", "{}", "<>"], "answer": "{}", "topic": "Data Types"},

    # String
    {"question": "What will be the output of 'Hello'[1]?", "options": ["H", "e", "l", "o"], "answer": "e", "topic": "String"},
    {"question": "Strings in Python are:", "options": ["Mutable", "Immutable", "Changeable", "None"], "answer": "Immutable", "topic": "String"},

    # List
    {"question": "Which method is used to add an item to the end of a list?", "options": ["add()", "append()", "push()", "insert()"], "answer": "append()", "topic": "List"},
    {"question": "What is the result of len([1, 2, 3])?", "options": ["2", "3", "4", "Error"], "answer": "3", "topic": "List"},

    # Tuple
    {"question": "Tuples are defined using which brackets?", "options": ["()", "[]", "{}", "<>"], "answer": "()", "topic": "Tuple"},
    {"question": "Tuples are:", "options": ["Mutable", "Immutable", "Both", "None"], "answer": "Immutable", "topic": "Tuple"},

    # Set
    {"question": "Which method removes all items from a set?", "options": ["clear()", "delete()", "remove()", "empty()"], "answer": "clear()", "topic": "Set"},
    {"question": "Which of the following does NOT allow duplicates?", "options": ["List", "Tuple", "Set", "Dictionary"], "answer": "Set", "topic": "Set"},

    # Dictionary
    {"question": "Dictionary in Python stores data in:", "options": ["Key-value pairs", "Indexed elements", "Single values", "None"], "answer": "Key-value pairs", "topic": "Dictionary"},
    {"question": "Which method is used to get all keys of a dictionary?", "options": ["items()", "get()", "keys()", "values()"], "answer": "keys()", "topic": "Dictionary"},

    # Functions
    {"question": "Which keyword is used to define a function?", "options": ["func", "define", "def", "lambda"], "answer": "def", "topic": "Functions"},
    {"question": "What is the correct way to call a function in Python?", "options": ["call funcName()", "funcName()", "run funcName", "execute funcName"], "answer": "funcName()", "topic": "Functions"},
    {"question": "Which keyword is used to return a value from a function?", "options": ["send", "give", "return", "yield"], "answer": "return", "topic": "Functions"},

    # OOPs
    {"question": "Which keyword is used to create a class in Python?", "options": ["function", "class", "object", "def"], "answer": "class", "topic": "OOPs"},
    {"question": "What is 'self' in Python classes?", "options": ["A keyword", "Reference to object", "Class name", "None"], "answer": "Reference to object", "topic": "OOPs"},
    {"question": "What is the process of creating an instance of a class called?", "options": ["Instantiation", "Initialization", "Inheritance", "Polymorphism"], "answer": "Instantiation", "topic": "OOPs"}
]

question_bank_java = [
  # Basics
  {"question": "Which keyword is used to define a class in Java?", "options": ["function", "class", "struct", "object"], "answer": "class", "topic": "Basics"},
  {"question": "What is the file extension for Java files?", "options": [".js", ".class", ".py", ".java"], "answer": ".java", "topic": "Basics"},
  {"question": "Which method is the entry point of a Java program?", "options": ["start()", "main()", "run()", "execute()"], "answer": "main()", "topic": "Basics"},

  # Data types / Variables
  {"question": "Which is a valid integer data type in Java?", "options": ["int", "number", "integer", "decimal"], "answer": "int", "topic": "Data Types"},
  {"question": "Which keyword is used to create constants in Java?", "options": ["const", "final", "static", "constant"], "answer": "final", "topic": "Data Types"},
  {"question": "What is the default value of a boolean in Java?", "options": ["true", "false", "0", "null"], "answer": "false", "topic": "Data Types"},

  # Loops / Conditionals
  {"question": "Which loop runs at least once even if condition is false?", "options": ["for", "while", "do-while", "foreach"], "answer": "do-while", "topic": "Loops"},
  {"question": "Which keyword is used for decision making in Java?", "options": ["if", "select", "decide", "switch"], "answer": "if", "topic": "Conditionals"},

  # Arrays
  {"question": "What is the correct way to declare an array in Java?", "options": ["int arr[];", "arr int[];", "array int;", "int array;"], "answer": "int arr[];", "topic": "Arrays"},
  {"question": "Arrays in Java are:", "options": ["Objects", "Primitive types", "Functions", "Methods"], "answer": "Objects", "topic": "Arrays"},

  # Methods / Functions
  {"question": "Which keyword is used to call parent class constructor?", "options": ["this", "super", "parent", "base"], "answer": "super", "topic": "Methods"},
  {"question": "Which of these is used to return a value from a method?", "options": ["return", "get", "send", "exit"], "answer": "return", "topic": "Methods"},
  {"question": "What is method overloading?", "options": ["Same method name, different parameters", "Same return type", "Two classes having same method", "None"], "answer": "Same method name, different parameters", "topic": "Methods"},

  # OOP Basics
  {"question": "Which concept allows same function name in different classes?", "options": ["Inheritance", "Polymorphism", "Abstraction", "Encapsulation"], "answer": "Polymorphism", "topic": "OOP"},
  {"question": "Which access modifier makes a member visible only within its own class?", "options": ["public", "private", "protected", "static"], "answer": "private", "topic": "OOP"},
  {"question": "What is the process of acquiring properties of another class called?", "options": ["Abstraction", "Encapsulation", "Inheritance", "Overloading"], "answer": "Inheritance", "topic": "OOP"},

  # OOP Concepts
  {"question": "Which class cannot be instantiated?", "options": ["Abstract class", "Normal class", "Static class", "Final class"], "answer": "Abstract class", "topic": "OOP"},
  {"question": "What keyword is used to inherit a class?", "options": ["inherits", "extends", "super", "implements"], "answer": "extends", "topic": "OOP"},
  {"question": "What is encapsulation?", "options": ["Wrapping data & methods into one unit", "Inheritance", "Multiple methods", "None"], "answer": "Wrapping data & methods into one unit", "topic": "OOP"},

  # Bonus (Exception handling / etc)
  {"question": "Which keyword is used to handle exceptions?", "options": ["catch", "error", "throw", "try"], "answer": "try", "topic": "OOP"}
]

question_bank_c = [
  # Basics
  {"question": "Which symbol is used to end a statement in C?", "options": [";", ":", ".", ","], "answer": ";", "topic": "Basics"},
  {"question": "Which of the following is the correct file extension for C programs?", "options": [".py", ".c", ".cpp", ".java"], "answer": ".c", "topic": "Basics"},
  {"question": "Who is the creator of C language?", "options": ["Bjarne Stroustrup", "Dennis Ritchie", "James Gosling", "Guido van Rossum"], "answer": "Dennis Ritchie", "topic": "Basics"},

  # Data Types
  {"question": "Which is a floating point data type in C?", "options": ["int", "float", "char", "double"], "answer": "float", "topic": "Data Types"},
  {"question": "The size of 'int' type in C is usually:", "options": ["8 bytes", "4 bytes", "2 bytes", "1 byte"], "answer": "4 bytes", "topic": "Data Types"},
  {"question": "Which of the following is a character data type?", "options": ["char", "int", "float", "void"], "answer": "char", "topic": "Data Types"},

  # Arrays
  {"question": "Which is the correct way to declare an array in C?", "options": ["int arr[5];", "arr int[5];", "array int(5);", "int arr;"], "answer": "int arr[5];", "topic": "Arrays"},
  {"question": "Arrays in C are:", "options": ["Homogeneous", "Heterogeneous", "Objects", "Structures"], "answer": "Homogeneous", "topic": "Arrays"},

  # Loops / Conditionals
  {"question": "Which loop checks the condition after executing the loop body?", "options": ["for", "while", "do-while", "if"], "answer": "do-while", "topic": "Loops"},
  {"question": "Which keyword is used to skip to the next iteration in C loops?", "options": ["break", "continue", "skip", "pass"], "answer": "continue", "topic": "Loops"},

  # Pointers
  {"question": "What symbol is used to declare a pointer?", "options": ["*", "&", "$", "#"], "answer": "*", "topic": "Pointers"},
  {"question": "Which operator is used to access the value at the address pointed by a pointer?", "options": ["*", "&", "%", "@"], "answer": "*", "topic": "Pointers"},

  # Functions
  {"question": "Which keyword is used to return a value from a function?", "options": ["return", "send", "yield", "give"], "answer": "return", "topic": "Functions"},
  {"question": "Which of these is a correct function signature?", "options": ["void func()", "func void()", "function void", "void ()func"], "answer": "void func()", "topic": "Functions"},
  
  # Conditionals
  {"question": "Which statement is used for decision making in C?", "options": ["if statement", "for statement", "loop", "switch"], "answer": "if statement", "topic": "Conditionals"},
  {"question": "Which keyword is used to exit a loop in C?", "options": ["exit", "return", "break", "stop"], "answer": "break", "topic": "Conditionals"},

  # Structures (OOP style basic)
  {"question": "Which keyword is used to define a structure?", "options": ["struct", "class", "record", "union"], "answer": "struct", "topic": "Struct"},
  {"question": "Members of a structure are accessed using:", "options": [". operator", "-> operator", "& operator", "* operator"], "answer": ". operator", "topic": "Struct"},

  # Extra general
  {"question": "Which function is used to print output on the screen?", "options": ["scanf()", "print()", "printf()", "output()"], "answer": "printf()", "topic": "Basics"},
  {"question": "C language is:", "options": ["Object-oriented", "High level", "Procedural", "Functional"], "answer": "Procedural", "topic": "Basics"}
]

question_bank_html = [
  # Basics
  {"question": "HTML stands for:", "options": ["Hyperlinks and Text Markup Language", "Hyper Text Markup Language", "Home Tool Markup Language", "Hyperlink Markup Language"], "answer": "Hyper Text Markup Language", "topic": "Basics"},
  {"question": "Which tag is used for the largest heading?", "options": ["<h6>", "<heading>", "<h1>", "<h3>"], "answer": "<h1>", "topic": "Headings"},
  {"question": "Which HTML element is used to define a paragraph?", "options": ["<p>", "<pre>", "<text>", "<para>"], "answer": "<p>", "topic": "Basics"},

  # Elements & Attributes
  {"question": "Which attribute is used to provide alternative text for an image?", "options": ["alt", "src", "title", "href"], "answer": "alt", "topic": "Attributes"},
  {"question": "The correct HTML tag for inserting a line break is:", "options": ["<lb>", "<br>", "<break>", "</br>"], "answer": "<br>", "topic": "Basics"},
  {"question": "Which element is used to create a hyperlink?", "options": ["<a>", "<link>", "<href>", "<url>"], "answer": "<a>", "topic": "Links"},

  # Lists
  {"question": "Which tag defines an unordered list?", "options": ["<ol>", "<ul>", "<li>", "<list>"], "answer": "<ul>", "topic": "Lists"},
  {"question": "Each item in a list is defined using:", "options": ["<item>", "<list>", "<li>", "<il>"], "answer": "<li>", "topic": "Lists"},

  # Images
  {"question": "Which attribute specifies the path to an image?", "options": ["href", "link", "src", "path"], "answer": "src", "topic": "Images"},
  {"question": "Which tag is used to display an image?", "options": ["<pic>", "<img>", "<image>", "<src>"], "answer": "<img>", "topic": "Images"},

  # Forms
  {"question": "Which HTML element is used to create a text input field?", "options": ["<input>", "<textarea>", "<text>", "<form>"], "answer": "<input>", "topic": "Forms"},
  {"question": "What type of form control is used for multiline text?", "options": ["<input type='text'>", "<textarea>", "<input type='area'>", "<textbox>"], "answer": "<textarea>", "topic": "Forms"},

  # Semantic
  {"question": "Which tag represents a section of navigation links?", "options": ["<footer>", "<section>", "<nav>", "<main>"], "answer": "<nav>", "topic": "Semantic"},
  {"question": "Which HTML5 element defines important text?", "options": ["<strong>", "<b>", "<em>", "<i>"], "answer": "<strong>", "topic": "Semantic"},

  # Tables
  {"question": "Which tag is used to define a table row?", "options": ["<tr>", "<th>", "<td>", "<table>"], "answer": "<tr>", "topic": "Table"},
  {"question": "The table header cells are defined using which tag?", "options": ["<td>", "<th>", "<tab>", "<header>"], "answer": "<th>", "topic": "Table"},

  # Extra
  {"question": "Which doctype is used for HTML5?", "options": ["<!DOCTYPE HTML5>", "<!HTML>", "<!DOCTYPE html>", "<!DOCTYPE>"], "answer": "<!DOCTYPE html>", "topic": "Basics"},
  {"question": "Which tag is used to group content together in a block?", "options": ["<span>", "<div>", "<group>", "<content>"], "answer": "<div>", "topic": "Basics"},
  {"question": "Which tag is used to define the title of the document?", "options": ["<header>", "<title>", "<head>", "<meta>"], "answer": "<title>", "topic": "Basics"}
]

question_bank_css = [
  # Basics
  {"question": "CSS stands for:", "options": ["Computer Style Sheets", "Cascading Style Sheets", "Creative Style Sheets", "Colorful Style Sheets"], "answer": "Cascading Style Sheets", "topic": "Basics"},
  {"question": "Which HTML tag is used to link an external CSS file?", "options": ["<css>", "<style>", "<link>", "<script>"], "answer": "<link>", "topic": "Basics"},
  {"question": "Where in HTML document is the correct place to refer to an external CSS file?", "options": ["Head Section", "Body Section", "End of document", "Anywhere"], "answer": "Head Section", "topic": "Basics"},

  # Selectors
  {"question": "Which symbol is used for ID selector in CSS?", "options": [".", "#", "*", "&"], "answer": "#", "topic": "Selectors"},
  {"question": "Which symbol is used for class selector in CSS?", "options": [".", "#", "*", "$"], "answer": ".", "topic": "Selectors"},
  {"question": "Which universal selector is used to select all elements?", "options": ["*", "#", ".", "&"], "answer": "*", "topic": "Selectors"},

  # Properties
  {"question": "Which CSS property is used to change text color?", "options": ["font-color", "text-color", "color", "style"], "answer": "color", "topic": "Properties"},
  {"question": "Which property changes the background color of an element?", "options": ["bgcolor", "style", "background-color", "color"], "answer": "background-color", "topic": "Properties"},
  {"question": "To make text bold we use:", "options": ["font-weight:bold", "text-bold", "font:bold", "weight:bold"], "answer": "font-weight:bold", "topic": "Properties"},

  # Box Model
  {"question": "Padding is:", "options": ["Space outside border", "Space inside border", "Same as margin", "Text color"], "answer": "Space inside border", "topic": "Box Model"},
  {"question": "Margin is:", "options": ["Space inside element", "Space outside the border", "Border thickness", "None"], "answer": "Space outside the border", "topic": "Box Model"},

  # Layout / Display
  {"question": "Which property controls the type of box used for an element?", "options": ["position", "display", "float", "align"], "answer": "display", "topic": "Layout"},
  {"question": "Which CSS property is used to position elements relative to their normal position?", "options": ["absolute", "fixed", "relative", "static"], "answer": "relative", "topic": "Layout"},
  {"question": "Which property is used to make elements float beside each other?", "options": ["align", "position", "float", "display"], "answer": "float", "topic": "Layout"},

  # Fonts & Text
  {"question": "Which property changes the size of text?", "options": ["font-style", "font-size", "text-size", "size"], "answer": "font-size", "topic": "Text"},
  {"question": "Which CSS property adds space between letters?", "options": ["line-height", "letter-spacing", "word-spacing", "spacing"], "answer": "letter-spacing", "topic": "Text"},

  # Extra Styling
  {"question": "Which is correct for making text italic?", "options": ["font-italic", "font-style:italic", "text-italic", "style-italic"], "answer": "font-style:italic", "topic": "Properties"},
  {"question": "Which property adds shadow to text?", "options": ["text-shadow", "font-shadow", "box-shadow", "style-shadow"], "answer": "text-shadow", "topic": "Properties"},
  {"question": "Which shorthand property can change margin on all four sides at once?", "options": ["margin-all", "margin", "padding", "spacing"], "answer": "margin", "topic": "Box Model"}
]

question_bank_js = [
  # Basics
  {"question": "JavaScript is a ___ scripting language.", "options": ["Server-side", "Client-side", "Mid-side", "None"], "answer": "Client-side", "topic": "Basics"},
  {"question": "Which symbol is used for single line comments in JavaScript?", "options": ["/* */", "<!-- -->", "//", "#"], "answer": "//", "topic": "Basics"},
  {"question": "What is correct syntax to declare a variable?", "options": ["var x;", "int x;", "let x:", "declare x"], "answer": "var x;", "topic": "Variables"},

  # Data Types
  {"question": "Which of the following is NOT a JavaScript data type?", "options": ["String", "Number", "Boolean", "Character"], "answer": "Character", "topic": "Data Types"},
  {"question": "How do you check the type of a variable in JS?", "options": ["typeof", "type()", "check()", "kindof"], "answer": "typeof", "topic": "Data Types"},
  {"question": "Which keyword declares a constant?", "options": ["let", "var", "const", "constant"], "answer": "const", "topic": "Variables"},

  # Arrays / Objects
  {"question": "How do you define an array in JavaScript?", "options": ["()", "{}", "[]", "<>"], "answer": "[]", "topic": "Arrays"},
  {"question": "How do you access the 2nd element of an array?", "options": ["arr(1)", "arr[1]", "arr{1}", "arr<1>"], "answer": "arr[1]", "topic": "Arrays"},
  {"question": "What is used to define a key-value pair in JS?", "options": ["List", "Array", "Object", "Tuple"], "answer": "Object", "topic": "Objects"},

  # Functions
  {"question": "Which keyword is used to create a function?", "options": ["function", "func", "method", "def"], "answer": "function", "topic": "Functions"},
  {"question": "Arrow functions were introduced in:", "options": ["ES5", "ES6", "ES7", "ES4"], "answer": "ES6", "topic": "Functions"},
  {"question": "How to call a function named hello?", "options": ["call hello()", "hello()", "execute hello", "hello"], "answer": "hello()", "topic": "Functions"},

  # Conditionals
  {"question": "Which operator is used for strict equality?", "options": ["==", "=", "===", "!=="], "answer": "===", "topic": "Conditionals"},
  {"question": "Which statement is used for decision making?", "options": ["switch", "if", "for", "loop"], "answer": "if", "topic": "Conditionals"},
  
  # DOM
  {"question": "Which method is used to select an element by ID?", "options": ["getElementByName", "getElementById", "select()", "queryId()"], "answer": "getElementById", "topic": "DOM"},
  {"question": "Which keyword refers to the current object?", "options": ["that", "self", "this", "obj"], "answer": "this", "topic": "OOP"},

  # Extra
  {"question": "What will console.log(typeof NaN) return?", "options": ["number", "NaN", "undefined", "string"], "answer": "number", "topic": "Data Types"},
  {"question": "Which looping statement is used to iterate over array indices?", "options": ["while", "for", "for...of", "for...in"], "answer": "for...in", "topic": "Loops"},
  {"question": "How to write an alert box in JS?", "options": ["alert()", "msgBox()", "popup()", "show()"], "answer": "alert()", "topic": "Basics"}
]



import json

# Dictionary of all question banks
question_banks = {
    "python": question_bank_python,
    "java": question_bank_java,
    "c": question_bank_c,
    "html": question_bank_html,
    "css": question_bank_css,
    "javascript": question_bank_js
}

# Save each language as a separate JSON file in the same folder
for lang, questions in question_banks.items():
    filename = f"{lang}_questions.json"
    with open(filename, "w") as f:
        json.dump(questions, f, indent=4)

print("All question banks saved as separate JSON files!")
