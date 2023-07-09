#!/usr/bin/python3
'''
## Task: Create a Calculator

### Intro
calculator.py:              Class object which realizing as calculator for
                            4 operation
author:                     Nakonechnyi Mikhail
date:                       04.07.23
version:                    1.1 (with OOP)
description of homework:


### Description

As we started discuss on Lection a basic program that can ever exist
- Calculator,

Your task is to create a basic calculator program using Python.

The program should allow the user to perform simple arithmetic operations on
two numbers.

### Requirements:

    Prompt the user to enter two numbers.
    Prompt the user to select an operation from the following options:

    addition
    subtraction
    multiplication
    division.

Based on the selected operation, perform the corresponding calculation.
Display the result to the user.

```
#python01-hw % calculator.py
Welcome to the Calculator Program!

Please enter the first number: 10
Please enter the second number: 5

Please select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter your choice (1-4): 3

The result of multiplication is: 50
```

### Note:

Ensure that the program handles division by zero and provides an appropriate
 error message if the user attempts to divide by zero. Consider using
 functions to encapsulate the calculation logic for each operation.
 Include clear instructions and error handling for invalid input.

### Useful links:
* https://docs.python.org/3/library/functions.html#input
* https://docs.python.org/3/library/functions.html#print
* https://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html


### Versions:
* 1.0 OOP realization
* 1.1 Change Logic and Fix Error Exception
'''
from sys import exit as ex


class Calculator:
    """Calculator class for performing arithmetic operations."""

    def __init__(self):
        self.description = """Welcome to the Calculator Program!"""
        self.number1 = None
        self.number2 = None
        self.operation = None
        self.operations = {
            1: self.add,
            2: self.subtract,
            3: self.multiply,
            4: self.divide,
        }

    def hello(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.description

    def add(self, number1, number2):
        """Perform addition of two numbers."""
        return number1 + number2

    def subtract(self, number1, number2):
        """Perform subtraction of two numbers."""
        return number1 - number2

    def multiply(self, number1, number2):
        """Perform multiplication of two numbers."""
        return number1 * number2

    def divide(self, number1, number2):
        """Perform division of two numbers."""
        if number2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return number1 / number2

    def print_operation_menu(self):
        """_summary_
        """
        print("\nPlease select an operation:")
        for i in self.operations:
            print(f"{i}. {self.operations[i].__name__}")

    def input_number(self, prompt):
        """Input a number from the user."""
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError as valerr:
                print(f"{str(valerr)}")
                # Invalid input. Please enter a valid number.
            except TypeError as typeerr:
                print(f"Error: {str(typeerr)}")

    def select_operation(self):
        """Select an operation from the available options."""
        while True:
            try:
                self.print_operation_menu()

                operation = int(input("Enter your choice (1-4): "))
                if operation not in self.operations:
                    raise \
                        ValueError(
                            "Invalid choice. \
                                Please select a valid operation (1-4).")
                if operation not in self.operations.keys():
                    raise KeyError(
                        "Invalid choice. \
                            Please select a valid operation (1-4).")
                return operation
            except TypeError as typeerr:
                print(f"Error: {str(typeerr)}")
                return False
            except ValueError as valerr:
                print(f"Error: {str(valerr)}")
                return False
            except KeyError as keyerr:
                print(f"Error: {str(keyerr)}")

    def run_calculator(self):
        """Run the calculator program."""
        try:
            while not self.number1 or not self.number2 or not self.operation:
                try:
                    self.number1 = self.input_number(
                        "Please enter the first number: ")
                    self.number2 = self.input_number(
                        "Please enter the second number: ")
                    self.operation = self.select_operation()
                except KeyboardInterrupt:
                    print("\nUser interrupted. Exiting...")
                    ex()

            result = self.operations[self.operation](
                self.number1,
                self.number2)
            print("\nThe result is:", result)

        except ZeroDivisionError as zeroexc:
            print("Error:", str(zeroexc))
        except KeyboardInterrupt:
            print("\nUser interrupted. Exiting...")
            ex()
