"""
Question 8 - Recursive Factorial
=================================
RECURSION is a function that calls ITSELF on a smaller version of the
same problem.

Every recursive function needs exactly two things:

    1. A BASE CASE     - the simplest input, answered without recursion.
                         This is what STOPS the recursion.
    2. A RECURSIVE CASE - the function calling itself on a SMALLER input,
                         which must move TOWARDS the base case.

Miss the base case, or fail to shrink the input, and the function calls
itself forever until Python raises RecursionError.

THE FACTORIAL DEFINITION IS ALREADY RECURSIVE:
    5! = 5 x 4!
    4! = 4 x 3!    ... and so on ...
    1! = 1         <- the base case, no further call needed

So the code is a direct translation of the mathematics:
    factorial(n) = 1                    when n is 0 or 1
    factorial(n) = n * factorial(n - 1) otherwise
"""


def factorial(n):
    """Return n! calculated recursively."""
    # BASE CASE - stops the recursion
    if n <= 1:
        return 1
    # RECURSIVE CASE - calls itself with a SMALLER value
    return n * factorial(n - 1)


print("=" * 60)
print("RECURSIVE FACTORIAL")
print("=" * 60)
for n in range(0, 11):
    print(f"   {n}! = {factorial(n)}")
print()


# ---------------------------------------------------------------------------
# A TRACED VERSION - this prints the call stack as it builds and unwinds
# ---------------------------------------------------------------------------

def factorial_traced(n, depth=0):
    """Same function, but it prints every call and every return."""
    indent = "   " * depth

    print(f"{indent}-> factorial({n}) called")

    if n <= 1:
        print(f"{indent}   BASE CASE reached: factorial({n}) returns 1")
        return 1

    print(f"{indent}   needs factorial({n - 1}) before it can finish...")
    smaller = factorial_traced(n - 1, depth + 1)
    result = n * smaller

    print(f"{indent}<- factorial({n}) returns {n} x {smaller} = {result}")
    return result


print("=" * 60)
print("MANUAL TRACE OF factorial(5)")
print("=" * 60)
print()
answer = factorial_traced(5)
print()
print("FINAL ANSWER:", answer)
print()

print("=" * 60)
print("READING THAT TRACE")
print("=" * 60)
print("""
GOING DOWN (the calls pile up, nothing is calculated yet):
    factorial(5) needs factorial(4)
    factorial(4) needs factorial(3)
    factorial(3) needs factorial(2)
    factorial(2) needs factorial(1)
    factorial(1) is the BASE CASE -> returns 1 immediately

COMING BACK UP (each call now finishes, using the answer below it):
    factorial(2) = 2 x 1  =   2
    factorial(3) = 3 x 2  =   6
    factorial(4) = 4 x 6  =  24
    factorial(5) = 5 x 24 = 120

The multiplications happen on the WAY BACK UP, not on the way down.
Until the base case is hit, all five calls are paused and waiting.
""")

# --- Recursive versus iterative --------------------------------------------
print("=" * 60)
print("RECURSIVE VERSUS ITERATIVE")
print("=" * 60)


def factorial_loop(n):
    """The same result using a loop instead of recursion."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print("   n    recursive    loop")
print("   " + "-" * 30)
for n in range(1, 9):
    print(f"   {n}    {factorial(n):>9}    {factorial_loop(n):>6}")

print()
print("Both give the same answers. The loop uses less memory because it")
print("does not stack up paused function calls, but the recursive version")
print("matches the mathematical definition line for line.")
print()

# --- What happens without a base case --------------------------------------
print("=" * 60)
print("WHY THE BASE CASE MATTERS")
print("=" * 60)


def factorial_broken(n):
    """Deliberately missing its base case."""
    return n * factorial_broken(n - 1)


try:
    factorial_broken(5)
except RecursionError:
    print("factorial_broken(5) -> RecursionError: maximum recursion depth exceeded")
    print("With no base case it calls 4, 3, 2, 1, 0, -1, -2 ... forever,")
    print("until Python refuses to stack up any more calls.")
