#!/usr/bin/python3
import getpass
import crypt
import subprocess

from advanced.password_generation import PasswordGenerator


class UserPasswordChanger:
    """_summary_
    """
    def __init__(self):
        """_summary_
        """
        self.minimal_default_length = 16
        self.description = """User password changer"""
        self.password_generator = PasswordGenerator(self.minimal_default_length)

    def hello(self):
        """_summary_
        """
        return self.description

    def get_user_input(self):
        """
        Prompt the user to enter a username and a new password.

        Returns:
            tuple: Username and password entered by the user.
        """
        username = input("Enter the username: ")
        password = getpass.getpass("Enter the new password (leave blank to generate one): ")
        return username, password

    def check_user_exist(self, username):
        """
        Check if the user exists in the system.

        Args:
            username (str): Username to check.

        Returns:
            bool: True if the user exists, False otherwise.
        """
        try:
            subprocess.check_output(["id", username])
            return True
        except subprocess.CalledProcessError:
            return False

    def check_password_requirements(self, password):
        """
        Check if the password meets the specified requirements.
        """
        return self.password_generator.check_password_requirements(password)

    def generate_password(self):
        """
        Generate a random password using the PasswordGenerator class.

        Args:
            length (int): Length of the password. Defaults to 16.

        Returns:
            str: Generated password.
        """
        return self.password_generator.generate_password()

    def change_password(self, username=None, password=None):
        """
        Change the password for the specified username.

        Args:
            username (str): Username to change the password for.
            password (str, optional): New password. Defaults to None.
                If None, a random password will be generated.

        Returns:
            bool: True if the password is successfully changed, False otherwise.
        """
        username, password = self.get_user_input()

        if password is None or len(password) < 16:
            password = self.generate_password()
            print(password)

        if not self.check_user_exist(username):
            print(f"User '{username}' does not exist.")
            return False


        if not self.check_password_requirements(password):
            print("The password does not meet the requirements.")
            return False

        password_hash = crypt.crypt(str(password), crypt.mksalt(crypt.METHOD_SHA512))
        try:
            subprocess.check_call(["sudo", "usermod", "-p", password_hash, username])
            print(f"Password changed for user '{username}'.")
            return True
        except subprocess.CalledProcessError:
            print("Failed to change the password.")
            return False
