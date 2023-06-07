# 0x01. Python - if/else, loops, functions

This repository contains solutions to various programming tasks and exercises in Python, focusing on if/else statements, loops, and functions.

## List of Tasks

1. Positive anything is better than negative nothing
2. The last digit
3. Print the ASCII alphabet in lowercase
4. Print the ASCII alphabet in lowercase excluding 'q' and 'e'
5. Print numbers from 0 to 98 in decimal and hexadecimal
6. Print numbers from 0 to 99
7. Print all possible different combinations of two digits
8. Check for lowercase character
9. Print string in uppercase
10. Print the last digit of a number
11. Add two integers and return the result
12. Compute a to the power of b and return the value
13. Print numbers from 1 to 100 with specific conditions (Fizz Buzz)
14. Insert a number into a sorted singly linked list (C language)
15. Print the ASCII alphabet in reverse order, alternating lowercase and uppercase
16. Create a copy of the string, removing the character at the given position
17. Implement the Python function `magic_calculation(a, b, c)` to match specific bytecode behavior:

```python
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```

## Getting Started

To get started with any of the tasks, simply navigate to the corresponding file

## License

This project is licensed under the [MIT License](LICENSE).
