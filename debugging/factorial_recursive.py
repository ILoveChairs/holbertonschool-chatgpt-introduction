#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): The number whose factorial is to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Extract the command line argument which represents the number
# whose factorial is to be calculated.
number = int(sys.argv[1])

# Calculate the factorial of the given number.
factorial_result = factorial(number)

# Print the factorial result.
print(factorial_result)
