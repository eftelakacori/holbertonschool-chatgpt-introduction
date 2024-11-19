#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given number. If n is 0, returns 1 (base case).
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case: n * factorial of (n-1)

# Read the number from the command-line arguments
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)