## 0x01. Python - if/else, loops, functions
- 0 Positive anything is better than negative nothing
- 1 The last digit
- 2 Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
- 3 Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line. Print all the letters except q and e
- 4 Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal
- 5 Write a program that prints numbers from 0 to 99.
- 6 Write a program that prints all possible different combinations of two digits.
- 7 Write a function that checks for lowercase character
- 8 Write a function that prints a string in uppercase followed by a new line
- 9. Write a function that prints the last digit of a number.
- 10 Write a function that adds two integers and returns the result
- 11 Write a function that computes a to the power of b and return the value
- 12 Write a function that prints the numbers from 1 to 100 separated by a space Fizz Buzz
- 13 Technical interview preparation: Write a function in C that inserts a number into a sorted singly linked list.
- 100 Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
- 101 Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).
- 102 Write the Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:

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

