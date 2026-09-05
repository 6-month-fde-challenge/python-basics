"""
Question 2 - Separate Functions for the Four Operations
========================================================
Each operation is its own function. That is the point of functions:
ONE function does ONE job, and can then be reused anywhere.

Every function here takes two parameters and RETURNS a value.
None of them print - printing is the caller's decision. A function that
returns can be used in more maths; a function that prints cannot.

DIVISION NEEDS A GUARD. Dividing by zero is impossible, so divide()
checks first and returns a message instead of crashing.
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers (a minus b)."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return a divided by b, or a message if b is zero."""
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


print("=" * 50)
print("THE FOUR OPERATIONS ON 20 AND 4")
print("=" * 50)

x = 20
y = 4

print(f"   add({x}, {y})      = {add(x, y)}")
print(f"   subtract({x}, {y}) = {subtract(x, y)}")
print(f"   multiply({x}, {y}) = {multiply(x, y)}")
print(f"   divide({x}, {y})   = {divide(x, y)}")
print()

print("=" * 50)
print("THE DIVIDE-BY-ZERO GUARD")
print("=" * 50)
print("   divide(20, 0)  =", divide(20, 0))
print("   Without the if-check this would raise ZeroDivisionError.")
print()

print("=" * 50)
print("MORE EXAMPLES")
print("=" * 50)
pairs = [(10, 5), (7, 3), (100, 25), (9, 2)]
for a, b in pairs:
    print(f"   {a} and {b}:  + {add(a, b)}   - {subtract(a, b)}"
          f"   * {multiply(a, b)}   / {divide(a, b)}")
print()

print("=" * 50)
print("WHY RETURNING (NOT PRINTING) MATTERS")
print("=" * 50)
print("Because each function RETURNS, the results can feed each other:")
print("   add(multiply(3, 4), subtract(10, 2))")
print("   = add(", multiply(3, 4), ",", subtract(10, 2), ")")
print("   =", add(multiply(3, 4), subtract(10, 2)))
print()
print("   Order matters:", multiply(add(2, 3), 4), "is (2+3)*4, not 2+(3*4)")
