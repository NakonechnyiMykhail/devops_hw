#!/usr/bin/python3
'''
## Intro
password_generation.py:     Class object which generating secure password
author:                     Nakonechnyi Mikhail
date:                       04.07.23
version:                    2.0 (with OOP)
description of homework:

## *Task Advanced:* Create a Password Generator for Linux Users

Your task is to create a password generator program using Python specifically
designed for Linux users. The program should generate strong and secure
passwords that can be used for user accounts on Linux systems.

## *Requirements:*

Prompt the user to enter the desired length for the password. Generate a
random password consisting of a combination of uppercase letters, lowercase
letters, numbers, and special characters. Ensure that the generated password
meets the following criteria:

    Contains at least one uppercase letter
    Contains at least one lowercase letter
    Contains at least one number
    Contains at least one special character (e.g., !, @, #, $, %, etc.)
    Display the generated password to the user.

## *Example Output:*

Welcome to the Linux User Password Generator!

Please enter the desired password length: 12

Generated password: 3@5uJ9#p1L$w

##*Note:*

You can utilize the random module in Python to generate random characters and
build the password. Consider using the string module in Python to access sets
of characters (uppercase, lowercase, numbers, and special characters). Make
sure to include clear instructions and error handling for invalid input.


TODO: add initialization with constructor
'''

import sys
import random
import string


class PasswordGenerator:
    """Class to generate secure passwords."""

    def __init__(self, length=None):
        """
        Initialize a PasswordGenerator object.

        Args:
            length (int, optional): Length of the password. Defaults to None.
        """
        self.description = """Welcome to the Linux User Password Generator!"""
        self.length = length

    def hello(self):
        """_summary_
        """
        return self.description

    def generate_password(self):
        """Generate a secure password.

        Returns:
            str: Generated password.
        """
        if self.length is None:
            # Input validation from user
            while True:
                try:
                    length_input = \
                        input("Please enter the desired password length: ")
                    self.length = abs(int(round(float(length_input))))
                    if self.length < 16:
                        raise \
                            ValueError("Password length must be at least 16.")
                    break
                except ValueError:
                    print("Invalid input. Please enter a positive integer.")
                except KeyboardInterrupt:
                    print("\nUser interrupted. Exiting...")
                    sys.exit()
        else:
            # Check correct length
            if not isinstance(self.length, int) or self.length < 0:
                raise TypeError("Password length must be a positive integer.")
            if self.length < 16:
                raise ValueError("Password length must be at least 16.")

        try:
            # Define character sets
            lowercase_letters = string.ascii_lowercase
            uppercase_letters = string.ascii_uppercase
            numbers = string.digits
            special_characters = string.punctuation

            # Ensure the password has at least one character from each set
            password = []
            password.append(random.choice(lowercase_letters))
            password.append(random.choice(uppercase_letters))
            password.append(random.choice(numbers))
            password.append(random.choice(special_characters))

            # Fill the remaining password length with random characters
            remaining_length = self.length - 4
            password.extend(random.choice(
                lowercase_letters + uppercase_letters +
                numbers + special_characters
            ) for _ in range(remaining_length))

            # Shuffle the password to make it random
            random.shuffle(password)

            # Convert the password list to a string
            password = ''.join(password)

            return password

        except ValueError as exc:
            print("Error:", str(exc))
        except Exception as exc:
            print("An error occurred:", str(exc))

    def check_password_requirements(self, password):
        """
        Check if the password meets the specified requirements.

        Args:
            password (str): Password to check.

        Returns:
            bool: True if the password meets the requirements, False otherwise.
        """
        minimum_length = 8
        has_lowercase = any(char.islower() for char in str(password))
        has_uppercase = any(char.isupper() for char in str(password))
        has_digit = any(char.isdigit() for char in str(password))
        has_special_char = any(
            char in string.punctuation for char in str(password))

        return (
            len(password) >= minimum_length
            and has_lowercase
            and has_uppercase
            and has_digit
            and has_special_char
        )