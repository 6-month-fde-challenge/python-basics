"""
operations.py - the mathematical operations for the mini calculator
====================================================================
This is a MODULE: a Python file holding functions that another file
imports and uses. Keeping the maths here and the menu in
12_mini_calculator.py separates the two jobs:

    operations.py        -> WHAT the calculator can compute
    12_mini_calculator.py -> HOW the user interacts with it

Each function does exactly one thing, takes two numbers, and returns a
result. None of them print anything - printing is the menu's job. That
separation is what makes them easy to test and reuse.
"""


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a * b."""
    return a * b


def divide(a, b):
    """
    Return a / b.

    Dividing by zero is impossible, so instead of crashing we return None
    and let the caller decide what message to show.
    """
    if b == 0:
        return None
    return a / b


def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


def modulus(a, b):
    """Return the remainder of a divided by b, or None if b is zero."""
    if b == 0:
        return None
    return a % b


# Running this file directly runs a quick self-test instead of the menu.
# `__name__` is "__main__" only when this file is the one being executed;
# when 12_mini_calculator.py imports it, __name__ is "operations" and this
# block is skipped.
if __name__ == "__main__":
    print("Self-test of operations.py")
    print("-" * 40)
    print("add(10, 5)      =", add(10, 5))
    print("subtract(10, 5) =", subtract(10, 5))
    print("multiply(10, 5) =", multiply(10, 5))
    print("divide(10, 5)   =", divide(10, 5))
    print("divide(10, 0)   =", divide(10, 0), "(None means 'not possible')")
    print("power(10, 5)    =", power(10, 5))
    print("modulus(10, 3)  =", modulus(10, 3))
