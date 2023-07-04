#!/usr/bin/python3
import unittest
from random import randint
import string
from advanced.password_generation import PasswordGenerator


class PasswordGeneratorTests(unittest.TestCase):
    """Test case class for PasswordGenerator."""

    def test_contains_uppercase_letter(self):
        """
        Test if generated password contains at least one uppercase letter.
        """
        generator = PasswordGenerator(length=randint(16, 24))
        password = generator.generate_password()
        self.assertTrue(any(
            char in string.ascii_uppercase for char in str(password)
        ))

    def test_contains_lowercase_letter(self):
        """
        Test if generated password contains at least one lowercase letter.
        """
        generator = PasswordGenerator(length=randint(16, 24))
        password = generator.generate_password()
        self.assertTrue(any(
            char in string.ascii_lowercase for char in str(password)
        ))

    def test_contains_number(self):
        """
        Test if generated password contains at least one number.
        """
        generator = PasswordGenerator(length=randint(16, 24))
        password = generator.generate_password()
        self.assertTrue(any(
            char in string.digits for char in str(password)
        ))

    def test_contains_special_character(self):
        """
        Test if generated password contains at least one special character.
        """
        generator = PasswordGenerator(randint(16, 24))
        password = generator.generate_password()
        self.assertTrue(any(
            char in string.punctuation for char in str(password)
        ))

    def test_minimum_length(self):
        """
        Test if ValueError is raised for passwords with length less than 16.
        """
        generator = PasswordGenerator(length=15)
        with self.assertRaises(ValueError):
            generator.generate_password()

    def test_negative_input_validation(self):
        """
        Test if TypeError is raised for negative password length.
        """
        generator = PasswordGenerator(length=-16)
        with self.assertRaises(TypeError):
            generator.generate_password()

    def test_float_input_validation(self):
        """
        Test if TypeError is raised for float password length.
        """
        generator = PasswordGenerator(length=16.5)
        with self.assertRaises(TypeError):
            generator.generate_password()

    def test_string_input_validation(self):
        """
        Test if TypeError is raised for string password length.
        """
        generator = PasswordGenerator(length="abc")
        with self.assertRaises(TypeError):
            generator.generate_password()

    # def test_generated_password_length(self):
    #     generator = PasswordGenerator()
    #     for _ in range(10):
    #         password = generator.generate_password()
    #         self.assertGreaterEqual(len(password), 16)

    def test_password_uniqueness(self):
        """
        Test if generated passwords are unique.
        """
        generator = PasswordGenerator(length=16)
        generated_passwords = set()
        for _ in range(100):
            password = generator.generate_password()
            self.assertNotIn(password, generated_passwords)
            generated_passwords.add(password)
