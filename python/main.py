#!/usr/bin/python3
import argparse
import getpass
import unittest
from advanced.password_generation import PasswordGenerator
from tests.test_password_generation import PasswordGeneratorTests
from tests.test_user_password_changer import UserPasswordChangerTests
from advanced.user_password_changer import UserPasswordChanger


def user_change_password():
    """
    Change the user's password based on user input.

    Prompts the user to enter a username and a new password. If no password is
    provided, a random password will be generated.
    Then, the password is changed for the user. Prints the result of the
    operation.

    """
    password_changer = UserPasswordChanger()
    username, password = password_changer.get_user_input()

    if not password:
        password = password_changer.generate_password()

    success = password_changer.change_password(username, password)

    if success:
        print(f"Password changed for user '{username}'.")
    else:
        print("Failed to change the password.")

def main():
    """
    _summary_

    Run script:
        python main.py --generate-password
        python main.py --run-tests
        python main.py --generate-password --run-tests
    """
    parser = argparse.ArgumentParser(description="Usefull scripts")

    parser.add_argument(
        "--generate-password",
        required=False,
        dest="generate_password",
        action="store_true",
        help="Generate a random password",
    )
    parser.add_argument(
        "--run-tests",
        required=False,
        dest="run_tests",
        action="store_true",
        help="Run the all tests",
    )
    parser.add_argument(
        "--change-user-pass",
        required=False,
        dest="change_user_pass",
        action="store_true",
        help="Run the user password changing",
    )
    args = parser.parse_args()

    if args.generate_password:
        generator = PasswordGenerator()
        print(generator.hello())
        password = generator.generate_password()
        print("Generated password:", password)

    if args.change_user_pass:
        password_changer = UserPasswordChanger()
        print(password_changer.hello())
        password_changer.change_password()


    if args.run_tests:
        print(f'Running: {PasswordGeneratorTests.__doc__}')
        unittest.TextTestRunner().run(
            unittest.TestLoader().loadTestsFromTestCase(PasswordGeneratorTests)
        )
        print(f'Running: {UserPasswordChangerTests.__doc__}')
        unittest.TextTestRunner().run(
            unittest.TestLoader().loadTestsFromTestCase(
                UserPasswordChangerTests
            )
        )


if __name__ == "__main__":
    main()
