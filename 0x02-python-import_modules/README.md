# Python Import Modules - README

This repository contains Python scripts that demonstrate the usage of import modules. Each script corresponds to a specific task. Below is a description of each task along with its requirements and an example of expected output.

## Task 0: Import a Simple Function from a Simple File

**Requirements:**
- Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition 1 + 2 = 3

**Example:**
```shell
$ ./0-add.py
1 + 2 = 3
```
## Task 1: My First Toolbox!

**Requirements:**
- Write a program that imports functions from the file `calculator_1.py`, performs some math operations, and prints the results.

**Example:**
```shell
$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
```
## Task 2: How to make a script dynamic!

**Requirements:**
- Write a program that imports a variable from the file variable_load_2.py and prints its value.
**Example:**
```shell
$ ./2-args.py
0 arguments.
$ ./2-args.py Hello
1 argument:
1: Hello
$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
$
```
## Task 3: Infinite addition
**Requirements:**
- Write a program that prints the result of the addition of all arguments
**Example:**
```shell
$ ./3-infinite_add.py
0
$ ./3-infinite_add.py 79 10
89
$ ./3-infinite_add.py 79 10 -40 -300 89
-162
$
```
## Task 4: Who are you?
**Requirements:**
- Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).
**Example:**
```shell
$ curl -Lso "hidden_4.pyc" "https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc"
$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
$
```
## Task 5: Everything can be imported
**Requirements:**
- Write a program that imports the variable a from the file variable_load_5.py and prints its value
**Example:**
```shell
$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

$ ./5-variable_load.py
98
$
```
## Task 6: Build my own calculator!
**Requirements:**
- Write a program that imports all functions from the file calculator_1.py and handles basic operations.
**Example:**
```shell
$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py a operator b
1
$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
$
```
