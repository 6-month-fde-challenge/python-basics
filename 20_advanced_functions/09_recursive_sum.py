"""
Question 9 - Recursive Sum of 1 + 2 + 3 + ... + n
==================================================
The same two-part recipe as the factorial:

    BASE CASE      sum_to(1) = 1          (nothing smaller to add)
    RECURSIVE CASE sum_to(n) = n + sum_to(n - 1)

Read the recursive line in words:
    "the total up to n is n, plus the total up to everything below n"

THE ONLY DIFFERENCE FROM THE FACTORIAL is the operator:
    factorial -> n * factorial(n - 1)
    sum       -> n + sum_to(n - 1)
and the base case value (1 for both here, but a sum could safely use 0).
"""


def sum_to(n):
    """Return 1 + 2 + ... + n, calculated recursively."""
    # BASE CASE - guards against 0 and negatives too
    if n <= 1:
        return n
    # RECURSIVE CASE - n plus the total of everything below it
    return n + sum_to(n - 1)


print("=" * 60)
print("RECURSIVE SUM 1 + 2 + ... + n")
print("=" * 60)
for n in range(1, 11):
    print(f"   sum_to({n:>2}) = {sum_to(n)}")
print()


# ---------------------------------------------------------------------------
# A TRACED VERSION
# ---------------------------------------------------------------------------

def sum_to_traced(n, depth=0):
    """Same function, printing each call and each return."""
    indent = "   " * depth

    print(f"{indent}-> sum_to({n}) called")

    if n <= 1:
        print(f"{indent}   BASE CASE: sum_to({n}) returns {n}")
        return n

    print(f"{indent}   needs sum_to({n - 1}) first...")
    smaller = sum_to_traced(n - 1, depth + 1)
    result = n + smaller

    print(f"{indent}<- sum_to({n}) returns {n} + {smaller} = {result}")
    return result


print("=" * 60)
print("MANUAL TRACE OF sum_to(5)")
print("=" * 60)
print()
answer = sum_to_traced(5)
print()
print("FINAL ANSWER:", answer)
print()

print("=" * 60)
print("READING THAT TRACE")
print("=" * 60)
print("""
GOING DOWN (calls pile up, nothing is added yet):
    sum_to(5) needs sum_to(4)
    sum_to(4) needs sum_to(3)
    sum_to(3) needs sum_to(2)
    sum_to(2) needs sum_to(1)
    sum_to(1) is the BASE CASE -> returns 1

COMING BACK UP (each paused call now completes):
    sum_to(2) = 2 + 1  =  3
    sum_to(3) = 3 + 3  =  6
    sum_to(4) = 4 + 6  = 10
    sum_to(5) = 5 + 10 = 15

Check: 1 + 2 + 3 + 4 + 5 = 15
""")

# --- Verification against the loop and the formula -------------------------
print("=" * 60)
print("THREE WAYS TO GET THE SAME ANSWER")
print("=" * 60)


def sum_loop(n):
    """The same total using a loop."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_formula(n):
    """The same total using the mathematical formula."""
    return n * (n + 1) // 2


print("    n    recursive    loop    formula")
print("    " + "-" * 38)
for n in [1, 5, 10, 25, 50, 100]:
    print(f"   {n:>3}    {sum_to(n):>9}    {sum_loop(n):>4}    {sum_formula(n):>7}")

print()
print("All three agree for every value tested:",
      all(sum_to(n) == sum_loop(n) == sum_formula(n) for n in range(1, 101)))
print()
print("The formula is instant, the loop is cheap, and the recursion is the")
print("clearest match to the definition - but it stacks up n paused calls,")
print("so it is the only one of the three that can hit RecursionError.")
