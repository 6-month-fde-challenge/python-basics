"""
Question 5 - A Function That Calculates Factorial
==================================================
The factorial of n (written n!) is every whole number from 1 to n
multiplied together:

    5! = 1 x 2 x 3 x 4 x 5 = 120

All the logic lives inside the function: the validation, the loop and
the accumulator.

THE ACCUMULATOR STARTS AT 1, NOT 0.
Multiplying by 0 destroys everything, so a product must start at 1.
(A sum starts at 0, because adding 0 changes nothing.)

TWO SPECIAL CASES HANDLED INSIDE THE FUNCTION
    0! is defined as 1
    factorial is undefined for negative numbers -> return None
"""


def factorial(n):
    """Return the factorial of n, or None if n is negative."""
    if n < 0:
        return None                    # factorial is undefined here

    result = 1                         # a product must start at 1
    for i in range(1, n + 1):
        result *= i
    return result


print("=" * 50)
print("FACTORIALS FROM 0 TO 10")
print("=" * 50)

for n in range(0, 11):
    print(f"   {n:>2}! = {factorial(n)}")

print()
print("=" * 50)
print("EDGE CASES HANDLED INSIDE THE FUNCTION")
print("=" * 50)
print("   factorial(0)  =", factorial(0), " <- 0! is defined as 1")
print("   factorial(1)  =", factorial(1))
print("   factorial(-5) =", factorial(-5), " <- undefined, so None is returned")
print()

print("=" * 50)
print("A VERSION THAT SHOWS ITS WORKING")
print("=" * 50)


def factorial_verbose(n):
    """Return the factorial of n, printing each multiplication."""
    if n < 0:
        print("      factorial is not defined for negative numbers")
        return None

    result = 1
    print(f"      start: result = 1")
    for i in range(1, n + 1):
        result *= i
        print(f"      x {i}  ->  result = {result}")
    return result


print("   factorial_verbose(6)")
print("   RESULT:", factorial_verbose(6))
print()

print("=" * 50)
print("WHY THE ACCUMULATOR STARTS AT 1")
print("=" * 50)


def factorial_broken(n):
    """Deliberately wrong: starts the accumulator at 0."""
    result = 0
    for i in range(1, n + 1):
        result *= i
    return result


print("   Starting at 1 -> factorial(5) =", factorial(5), " (correct)")
print("   Starting at 0 -> factorial(5) =", factorial_broken(5),
      "   (wrong: anything x 0 is 0)")
print()

print("=" * 50)
print("HOW FAST FACTORIALS GROW")
print("=" * 50)
for n in [5, 10, 15, 20]:
    print(f"   {n:>2}! = {factorial(n)}")
