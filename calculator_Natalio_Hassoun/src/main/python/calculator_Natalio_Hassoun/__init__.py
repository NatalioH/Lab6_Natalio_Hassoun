"""Basic and extended calculator operations for Lab 6."""

from math import sqrt


def add(x, y):
    """Return the sum of x and y."""
    return x + y


def subtract(x, y):
    """Return x minus y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """Return x divided by y; reject a zero divisor."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def modulus(x, y):
    """Return the Python remainder of x by y; reject a zero divisor."""
    if y == 0:
        raise ValueError("Cannot calculate modulus with a zero divisor.")
    return x % y


def power(x, y):
    """Return x raised to the power y using Python exponentiation rules."""
    return x ** y


def square_root(x):
    """Return the real square root of x; reject negative inputs."""
    if x < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return sqrt(x)
