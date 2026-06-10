# Interactive Calculator Command-Line Application

This project is a simple command-line calculator developed in Python for IS 601.

The calculator allows users to perform the following arithmetic operations:

- Addition
- Subtraction
- Multiplication
- Division

The application uses a REPL (Read-Eval-Print Loop) pattern, allowing users to perform multiple calculations until they choose to exit the program.

## Features

- Interactive command-line menu
- Input validation
- Error handling for invalid inputs
- Division by zero protection
- Object-Oriented Programming (OOP) structure
- Unit testing with pytest
- Parameterized tests
- Git version control

## Project Structure

```text
A03_Interactive_Calculator_Command_Line
│
├── app
│   ├── __init__.py
│   ├── calculator.py
│   └── operations.py
│
├── tests
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_operations.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux / WSL:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the calculator from the project root directory:

```bash
python main.py
```

## Running Tests

Run all tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=app
```

## What I Learned

This project helped me review Python fundamentals, object-oriented programming concepts, error handling, testing with pytest, and project organization using Git and GitHub. It also reinforced the importance of validating user input and creating applications that handle unexpected situations gracefully.