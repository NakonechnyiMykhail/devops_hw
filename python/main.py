#!/usr/bin/python3
import argparse
import unittest
from advanced.password_generation import PasswordGenerator
from tests.test_password_generation import PasswordGeneratorTests


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
        help="Run the password generator tests",
    )

    args = parser.parse_args()

    if args.generate_password:
        generator = PasswordGenerator()
        print(generator.hello())
        password = generator.generate_password()
        print("Generated password:", password)

    if args.run_tests:
        unittest.TextTestRunner().run(
            unittest.TestLoader().loadTestsFromTestCase(PasswordGeneratorTests)
        )


if __name__ == "__main__":
    main()
