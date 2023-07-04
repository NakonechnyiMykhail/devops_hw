#!/usr/bin/python3

class Calculator:
    """Calculator class for performing arithmetic operations."""

    def __init__(self):
        self.description = """Welcome to the Calculator Program!"""
        self.operations = {
            1: self.add,
            2: self.subtract,
            3: self.multiply,
            4: self.divide,
        }

    def hello(self):
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

    def run_calculator(self):
        """Run the calculator program."""

        # Prompt the user to enter two numbers
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))

        # Prompt the user to select an operation

        print("\nPlease select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = int(input("Enter your choice (1-4): "))

        # Perform the corresponding calculation based on the selected operation
        if operation in self.operations:
            try:
                result = self.operations[operation](num1, num2)
                print("\nThe result is:", result)
            except ZeroDivisionError as e:
                print("Error:", str(e))
        else:
            print("Invalid choice. Please select a valid operation (1-4).")
