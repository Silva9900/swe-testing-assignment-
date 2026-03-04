# Quick-Calc

Quick-Calc is a simple calculator application developed for the Advanced Software Engineering course. The application performs basic arithmetic operations including addition, subtraction, multiplication, and division. The project demonstrates software testing practices using unit testing and integration testing together with version control using Git and GitHub.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with division-by-zero handling)
- Clear function

## Setup Instructions

1. Clone the repository

git clone https://github.com/Silva9900/swe-testing-assignment-

2. Navigate into the project folder

cd swe-testing-assignment-

3. Install dependencies

pip install -r requirements.txt

## How to Run Tests

Run the test suite using the command:

pytest

## Testing Framework Research

Two popular Python testing frameworks are **Unittest** and **Pytest**.

Unittest is Python’s built-in testing framework. It allows developers to create structured test cases using classes and methods. Since it is included in the Python standard library, it does not require installation. However, writing tests using unittest often requires more boilerplate code and can be more complex for small projects.

Pytest is a modern and widely used testing framework that allows developers to write tests using simple functions. It provides useful features such as fixtures, parameterized tests, and detailed error reporting. Pytest also requires less code and produces clearer output when tests fail.

For this project, **Pytest was chosen** because it is easier to use, requires less boilerplate code, and provides better readability and debugging information.
