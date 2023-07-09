# devops_hw

## Description

## Lections:

## Homeworks 

### 1. Homework Assignment: [Git Mastery](https://github.com/devops01ua/git_internal)
#### Task 1: Repository Basics

##### Solution: [commit](https://github.com/NakonechnyiMykhail/devops_hw/commit/56479cd3c584e243dbf615470295cfe4e0789687)

    Create a new repository on GitHub.
    Clone the repository to your local machine, create a new file called README.md, and commit the changes.
    Push the commits back to the remote repository on GitHub.

#### Task 2: Branching and Merging

##### Solution: [commit](https://github.com/NakonechnyiMykhail/devops_hw/commit/6bc2e9780c56f6e6fb51486aa0f69906adb5cfd7)

    Create a new branch called feature-branch from the main branch.
    Make some changes to an existing file or create a new file, commit the changes, and push the branch to GitHub.
    Then, merge the feature-branch into the main branch using a pull request.

#### Task 3: Resolving Conflicts

##### Solution: [commit](https://github.com/NakonechnyiMykhail/devops_hw/commit/23b214b2f5b0d407a161309976254c4623713c31)

    Create a new branch from the main branch.
    Make changes to a file in both the main branch and your new branch.
    Commit the changes to both branches, causing a conflict.
    Resolve the conflict by manually editing the conflicting file, commit the changes, and push them to GitHub.

#### Task 4: Collaboration with Forks

##### Solution: [commit](https://github.com/devops01ua/git_internal/pull/31)

    Fork the git_internal repo on GitHub.
    Make changes to student.txt: add your first and last name.
    Submit the changes as a pull request to the original repo.
    Add a link to the repo you created in tep 1 to a comment on the PR.

---

### 2. Homework Assignment: [Python Internals](https://github.com/devops01ua/python01-hw)

#### Task: [Create a Calculator](https://github.com/devops01ua/python01-hw/blob/main/homeworks/HW1.md)

##### Solution: [commit](https://github.com/NakonechnyiMykhail/devops_hw/commit/e0770a3882375dbc9bab8a38b1dec2d61ce5ac67)

As we started discuss on Lection a basic program that can ever exist - Calculator,

Your task is to create a basic calculator program using Python.

The program should allow the user to perform simple arithmetic operations on two numbers.

##### Requirements:
```
    Prompt the user to enter two numbers.
    Prompt the user to select an operation from the following options:

    addition
    subtraction
    multiplication
    division.
```
Based on the selected operation, perform the corresponding calculation. Display the result to the user.

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
````

##### Note:

Ensure that the program handles division by zero and provides an appropriate error message if the user attempts to divide by zero. Consider using functions to encapsulate the calculation logic for each operation. Include clear instructions and error handling for invalid input.

[Useful link](https://docs.python.org/3/library/functions.html#input)

[Useful link](https://docs.python.org/3/library/functions.html#print)

[Useful link](https://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html)



#### Task Advanced: [Create a Password Generator for Linux Users](https://github.com/devops01ua/python01-hw/blob/main/homeworks/HW1-advanced.md)

##### Solution: [commit](https://github.com/NakonechnyiMykhail/devops_hw/commit/bed1c5ef7293da51675a5269e97be308f5948d79)

Your task is to create a password generator program using Python specifically designed for Linux users. The program should generate strong and secure passwords that can be used for user accounts on Linux systems.

##### Requirements:

Prompt the user to enter the desired length for the password. Generate a random password consisting of a combination of uppercase letters, lowercase letters, numbers, and special characters. Ensure that the generated password meets the following criteria:

  *  Contains at least one uppercase letter
  *  Contains at least one lowercase letter
  *  Contains at least one number
  *  Contains at least one special character (e.g., !, @, #, $, %, etc.)
  *  Display the generated password to the user.

##### Example Output:

```
Welcome to the Linux User Password Generator!

Please enter the desired password length: 12

Generated password: 3@5uJ9#p1L$w
```

##### Note:

You can utilize the random module in Python to generate random characters and build the password. Consider using the string module in Python to access sets of characters (uppercase, lowercase, numbers, and special characters). Make sure to include clear instructions and error handling for invalid input.


---

#### Task: [Password change for Linux User](https://github.com/devops01ua/python01-hw/blob/main/homeworks/HW2.md)

##### Solution: [commit](https://github.com/NakonechnyiMykhail/devops_hw/commit/c476d4a5fc36f795f21c051c731986499212cce8)

Your task is to develop a Python script that implements the Linux chpasswd simulation

##### Requirements:

*    The program should prompt the user to enter a username.
*    The program should check if user exist in system.
*    The program should ask the user to input a password or generate a new one if not provided.
*    The program should check the password against specified requirements
   -     minimum length
   -     presence of different character types (uppercase, lowercase, digits, special characters)
   -     any other criteria you specify.
*    Change password for user
*    The program should print the results, including the username, the original or generated password, and whether the password meets the requirements.

##### Useful Links 
[link1](https://www.maketecheasier.com/how-linux-stores-manages-user-passwords/) 
[link2](https://www.section.io/engineering-education/how-to-execute-linux-commands-in-python/) 
[link3](https://unix.stackexchange.com/questions/238180/execute-shell-commands-in-python)


---

#### Group Homework #1: [Deployment Automation Script](https://github.com/devops01ua/python01-hw/blob/main/homeworks/HW1-group.md)

##### Solution: [commit]()

##### Task Description: Your task is to develop a deployment automation script that automates the deployment process of a web application on server.

##### The script should perform the following tasks:

    Pull the latest code from a version control system (e.g., Git) for https://github.com/rat9615/simple-nodejs-app application
    Build and package the web application.
    Deploy the application.
    Configure any necessary environment variables or settings.
    Restart the necessary services to apply the changes.
    Implement error handling and rollback mechanisms in case of deployment failures.
    Generate a deployment report summarizing the deployment status.

##### Requirements:

    Create a Python script that automate the deployment process.
    Integrate the script with a version control system (e.g., Git) to pull the latest code from the repository.
    Implement the necessary build steps to build and package the web application on server.
    Deploy the packaged application on the server.
    Configure any required environment variables or settings on the target servers to support the application.
    Implement appropriate error handling to detect deployment failures and provide rollback functionality if needed.
    Generate a deployment report that summarizes the deployment status for server, indicating success or failure.

##### Additional Challenge (Optional):

Extend the deployment automation script to include the following additional functionalities:

    Implement version tracking or tagging mechanisms to ensure traceability and rollback options.
    multiple servers deployment using SSH
    multiple report that summarize info per server

##### Submission:

Submit your Python script along with any necessary instructions or configuration files to your GitHub repo

Note: Ensure that your script securely connects to remote servers using SSH and automates the deployment process accurately. Handle any potential errors or exceptions gracefully and provide informative output or logs. Test your script with multiple servers and a sample web application to validate its functionality and performance.

Example Interaction: Here's an example of how you can interact with the Python script:

##### Run the script:
```
$ python deployment_script.py or python deployment_script <ip_address of server>
The script establishes SSH connections to the remote servers defined in the configuration file.

It pulls the latest code from the version control system (e.g., Git) repository for server(on each server).

The necessary build steps are executed to build and package the web application.

The packaged application is deployed to the target servers using secure file transfer mechanisms over SSH.

Any required environment variables or settings are configured on the target servers.

The necessary services are restarted to apply the changes.

The script generates a deployment report summarizing the deployment status for each server, indicating success or failure.
```
Remember to customize the script according to your specific deployment requirements and server configurations.

##### Useful links
