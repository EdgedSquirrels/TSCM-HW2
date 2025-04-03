def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b

def factorial(n):
    """
    Computes the factorial of a number.

    Args:
        n (int): The number to compute the factorial of.

    Returns:
        int: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def isOdd(n):
    """
    Checks if a number is odd.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is odd, False otherwise.
    """
    return n % 2 != 0