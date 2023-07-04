#!/usr/bin/python3

import unittest
from unittest.mock import patch
from advanced.user_password_changer import UserPasswordChanger


class UserPasswordChangerTests(unittest.TestCase):
    """UserPasswordChangerTests"""
    def setUp(self):
        """_summary_

        Args:
            unittest (_type_): _description_
        """
        self.password_changer = UserPasswordChanger()

    @patch("getpass.getpass")
    @patch("builtins.input")
    def test_get_user_input(self, mock_input, mock_getpass):
        """
        Test the get_user_input method.

        Mocks the user input and verifies that the method returns the expected
        username and password.

        Args:
            mock_input (MagicMock): Mock for the built-in input function.
            mock_getpass (MagicMock): Mock for the getpass.getpass function.
        """
        # Mock user input
        mock_input.side_effect = ["test", "password"]
        mock_getpass.return_value = "password"

        # Call the method
        username, password = self.password_changer.get_user_input()

        # Assert the results
        self.assertEqual(username, "test")
        self.assertEqual(password, "password")

    def test_check_user_exist_existing_user(self):
        """
        Test the check_user_exist method with an existing user.

        Checks if the method returns True for an existing user.

        """
        # Existing user
        username = "test"
        self.assertTrue(self.password_changer.check_user_exist(username))

    def test_check_user_exist_non_existing_user(self):
        """
        Test the check_user_exist method with a non-existing user.

        Checks if the method returns False for a non-existing user.

        """
        # Non-existing user
        username = "non_existing_user"
        self.assertFalse(self.password_changer.check_user_exist(username))

    def test_check_password_requirements_meets_requirements(self):
        """
        Test the check_password_requirements method with a password that meets
        the requirements.

        Checks if the method returns True for a password that meets the
        requirements.

        """
        # Password meets the requirements
        password = "Passw0rd!"
        self.assertTrue(
            self.password_changer.check_password_requirements(password)
        )

    def test_check_password_requirements_does_not_meet_requirements(self):
        """
        Test the check_password_requirements method with a password that does
        not meet the requirements.

        Checks if the method returns False for a password that does not meet
        the requirements.

        """
        # Password does not meet the requirements
        password = "weakpassword"
        self.assertFalse(
            self.password_changer.check_password_requirements(password)
        )

    def test_generate_password(self):
        """
        Test the generate_password method.

        Checks if the generated password has the expected length.

        """
        # Generate a password
        password = self.password_changer.generate_password()

        # Assert the password length
        self.assertEqual(len(str(password)), 16)
