# Python Import Modules - README

This repository contains Python scripts that demonstrate the usage of import modules. Each script corresponds to a specific task. Below is a description of each task along with its requirements and an example of expected output.

## Task 0: Import a Simple Function from a Simple File

**Requirements:**
- Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition 1 + 2 = 3

**Example:**
```shell
$ cat add_0.py
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
$ ./0-add.py
1 + 2 = 3
```
## Task 1: My First Toolbox!

**Requirements:**
- Write a program that imports functions from the file `calculator_1.py`, performs some math operations, and prints the results.

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
## Task 7: Easy to print
**Requirements:**
- Write a program that prints #pythoniscool, followed by a new line, in the standard output.
- ou are not allowed to use print or eval or open or import sys in your file 101-easy_print.py
**Example:**
```shell
$ ./101-easy_print.py
#pythoniscool
$
```
## Task 8: ByteCode -> Python #3
**Requirements:**
- Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode
**Provided Bytecode:**
```python
  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```
## Task 9: Fast alphabet
**Requirements:**
- Write a program that prints the alphabet in uppercase, followed by a new line.
- Your program should be maximum 3 lines long
- You are not allowed to use:
- any loops
- any conditional statements
- str.join()
- any string literal
- any system calls
**Expected:**
```shell
$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
$ wc -l 103-fast_alphabet.py
3 103-fast_alphabet.py
$
```
