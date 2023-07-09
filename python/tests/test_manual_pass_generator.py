#!/usr/bin/python3
from advanced.password_generation import PasswordGenerator

# test 1
generator = PasswordGenerator(
    is_set=True,
    setdefault=False,
    setlength=15
    )
password = generator.generate_password()
print("Generated password:", password)

# test 2 - ok
# generator = PasswordGenerator(setdefault=True)
# password = generator.generate_password()
# print("Generated password:", password)

# test 2
generator = PasswordGenerator(
    is_set=True,
    setdefault=False,
    setlength=17,
    setinclude_uppercase=True,
    setinclude_lowercase=True,
    setinclude_digits=True,
    setinclude_special_chars=True,
    )
generator.set_length(15)
password = generator.generate_password()
print("Generated password:", password)

# test 2
generator = PasswordGenerator(
    is_set=True,
    setdefault=False,
    setlength=17,
    setinclude_uppercase=True,
    setinclude_lowercase=True,
    setinclude_digits=True,
    setinclude_special_chars=True,
    )
password = generator.generate_password()
print("Generated password:", password)
