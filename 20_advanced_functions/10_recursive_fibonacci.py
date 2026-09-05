"""
Question 10 - Recursive Fibonacci
==================================
In the Fibonacci sequence every number is the sum of the two before it:

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

THIS ONE NEEDS **TWO** BASE CASES, not one:
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n - 1) + fib(n - 2)      for n >= 2

Why two? The recursive case reaches back TWO steps, so stopping only at
n == 0 would let n == 1 fall through to fib(0) + fib(-1) and run away
into negative numbers.

THE OTHER BIG DIFFERENCE FROM FACTORIAL:
factorial makes ONE recursive call per level, so the calls form a straight
line. Fibonacci makes TWO, so the calls form a branching TREE - and the
same values get recalculated over and over. The program counts them below.
"""

# A counter so we can measure how much repeated work happens
call_count = 0


def fib(n):
    """Return the nth Fibonacci number (recursively)."""
    global call_count
    call_count += 1

    # BASE CASE 1
    if n == 0:
        return 0
    # BASE CASE 2
    if n == 1:
        return 1
    # RECURSIVE CASE - two calls, not one
    return fib(n - 1) + fib(n - 2)


print("=" * 60)
print("THE NTH FIBONACCI NUMBER")
print("=" * 60)
for n in range(0, 13):
    call_count = 0
    value = fib(n)
    print(f"   fib({n:>2}) = {value:<4}  (took {call_count} function calls)")
print()

# --- Generating the whole sequence -----------------------------------------
print("=" * 60)
print("THE SEQUENCE UP TO THE 15TH TERM")
print("=" * 60)

sequence = []
for n in range(15):
    sequence.append(fib(n))

print(sequence)
print()
print("Each term is the sum of the two before it:")
for i in range(2, 10):
    print(f"   {sequence[i - 2]} + {sequence[i - 1]} = {sequence[i]}")
print()


# ---------------------------------------------------------------------------
# A TRACED VERSION - showing the branching tree
# ---------------------------------------------------------------------------

def fib_traced(n, depth=0):
    """Same function, printing the tree of calls."""
    indent = "   " * depth
    print(f"{indent}-> fib({n})")

    if n == 0:
        print(f"{indent}   BASE CASE -> 0")
        return 0
    if n == 1:
        print(f"{indent}   BASE CASE -> 1")
        return 1

    left = fib_traced(n - 1, depth + 1)
    right = fib_traced(n - 2, depth + 1)
    result = left + right
    print(f"{indent}<- fib({n}) = {left} + {right} = {result}")
    return result


print("=" * 60)
print("MANUAL TRACE OF fib(5)")
print("=" * 60)
print()
answer = fib_traced(5)
print()
print("FINAL ANSWER: fib(5) =", answer)
print()

print("=" * 60)
print("READING THAT TRACE")
print("=" * 60)
print("""
Notice the SHAPE. factorial(5) went straight down and straight back up.
fib(5) SPLITS IN TWO at every level:

                    fib(5)
                   /      \\
              fib(4)      fib(3)
             /     \\      /     \\
        fib(3)  fib(2) fib(2)  fib(1)
        ...

Look for fib(3) in the trace - it is computed TWICE, completely from
scratch. fib(2) is computed three times. This duplicated work is why
recursive Fibonacci gets slow very quickly.
""")

# --- Measuring the wasted work ---------------------------------------------
print("=" * 60)
print("HOW FAST THE WASTED WORK GROWS")
print("=" * 60)
print("    n     fib(n)     calls made")
print("    " + "-" * 34)
for n in [5, 10, 15, 20, 25, 30]:
    call_count = 0
    value = fib(n)
    print(f"   {n:>2}   {value:>8}     {call_count:>10}")

print()
print("fib(30) needs over a million calls to find a number the loop below")
print("finds in 30 steps. Recursion is elegant here, but not efficient.")
print()

# --- The efficient loop version --------------------------------------------
print("=" * 60)
print("THE ITERATIVE VERSION - SAME ANSWERS, NO WASTE")
print("=" * 60)


def fib_loop(n):
    """Return the nth Fibonacci number using a loop."""
    if n == 0:
        return 0
    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current


print("    n    recursive    loop     agree?")
print("    " + "-" * 40)
for n in [0, 1, 5, 10, 20, 25]:
    print(f"   {n:>2}    {fib(n):>9}    {fib_loop(n):>4}     {fib(n) == fib_loop(n)}")

print()
print("fib_loop(50) =", fib_loop(50))
print("fib_loop(90) =", fib_loop(90))
print("The recursive version cannot reach those in any practical time -")
print("it would need roughly 2 ** n calls, which is billions by n = 50.")
