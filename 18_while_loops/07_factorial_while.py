"""
Question 7 - Factorial Using a while Loop
==========================================
    5! = 1 x 2 x 3 x 4 x 5 = 120

Two accumulators are running at once here, which is worth noticing:

    i      - the COUNTER, driving the loop from 1 up to n
    result - the PRODUCT, collecting the answer

THE PRODUCT STARTS AT 1, NOT 0. Multiplying by 0 destroys everything,
so a product must start at the value that changes nothing - which is 1.
(A sum starts at 0 for the same reason.)

The counter is what makes the loop terminate; the product is just
carried along for the ride.
"""


def factorial(n):
    """Return the factorial of n using a while loop, or None if n is negative."""
    if n < 0:
        return None                # factorial is undefined for negatives

    # INITIALIZATION : the counter starts at 1, and the product starts at 1
    i = 1
    result = 1

    # CONDITION : keep multiplying while the counter has not passed n.
    #             For n = 0 this is False immediately, so result stays 1,
    #             which is exactly the correct value of 0!.
    while i <= n:
        result *= i

        # UPDATE / TERMINATION : the counter climbs towards n each pass,
        # so the condition must eventually become False.
        i += 1

    return result


print("=" * 55)
print("CALCULATING 6! STEP BY STEP")
print("=" * 55)

n = 6
i = 1
result = 1

print(f"   start: i = 1, result = 1")

# CONDITION
while i <= n:
    result *= i
    print(f"   i = {i}: result = result x {i} = {result}")
    # UPDATE
    i += 1

print()
print(f"   RESULT: {n}! = {result}")
print()

print("=" * 55)
print("FACTORIALS FROM 0 TO 12")
print("=" * 55)

# INITIALIZATION
n = 0
# CONDITION
while n <= 12:
    print(f"   {n:>2}! = {factorial(n)}")
    # UPDATE
    n += 1

print()

print("=" * 55)
print("EDGE CASES")
print("=" * 55)
print("   factorial(0)  =", factorial(0), " <- the loop runs zero times, result stays 1")
print("   factorial(1)  =", factorial(1))
print("   factorial(-3) =", factorial(-3), " <- undefined, so None is returned")
print()

print("=" * 55)
print("WHY THE PRODUCT STARTS AT 1")
print("=" * 55)


def factorial_broken(n):
    """Deliberately wrong: the product starts at 0."""
    i = 1
    result = 0                     # wrong starting value
    while i <= n:
        result *= i
        i += 1
    return result


print("   Correct (start at 1) -> 5! =", factorial(5))
print("   Broken  (start at 0) -> 5! =", factorial_broken(5),
      "   because anything x 0 is 0")
print()

print("=" * 55)
print("while VERSUS for FOR THIS PROBLEM")
print("=" * 55)
print("""
   Here `for i in range(1, n + 1)` is actually the BETTER choice, because
   the number of passes IS known in advance - it is exactly n.

   The while version is written out to show the three parts explicitly,
   but this is a case where for is cleaner. Compare with Questions 4, 5
   and 6, where the pass count depends on the data and while genuinely wins.
""")
