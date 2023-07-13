# Scripts CLI
---

![actions](https://github.com/NakonechnyiMykhail/devops_hw/actions/workflows/python.yml/badge.svg)

This is a Python project for running most used scripts such as:

* calculate numbers
* generating secure passwords.
* change user password


## Requirements

- Python 3.8, 3.9, 3.10, 3.11 (tested)
- Virtual environment (venv, virtualenv, poetry)

## Installation

1. Clone the repository:

```bash
    git clone https://github.com/NakonechnyiMykhail/devops_hw/ passgen
```

2. Navigate to the project directory:

```bash
    cd passgen
```

---

3. **(version1)** Create and activate a virtual environment and install the required dependencies:

```bash
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
```


3. **(version2)** Install Poetry (if not already installed), then install the project dependencies::

```bash
    pip3 install poetry
    poetry install
```

## Usage example

You can use the `PasswordGenerator` class in your Python code to generate secure passwords.

```python
from advanced.password_generation import PasswordGenerator

# Create a password generator object
generator = PasswordGenerator()

# Generate a password
password = generator.generate_password()

# Print the generated password
print(password)
```

## Running the Tests

The unit tests for all scripts are located in the `tests` directory. To run the tests, use the following command:

**(version 1)**

```bash
python3 -m unittest discover tests
```

or

**(version 2)** use CLI:
```bash
python3 main.py --run-tests
```


## Links

[badges](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge)
[badge](https://dev.to/envoy_/150-badges-for-github-pnk)
[badge](https://github.com/badges/shields/tree/master)
[dependabot](https://docs.github.com/en/code-security/dependabot)
[dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)
[dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file)
