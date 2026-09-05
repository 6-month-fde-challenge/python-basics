"""
Question 12 - Print All Prime Numbers Between 1 and 100
========================================================
Concept: NESTED LOOPS combined with for-else.

    OUTER loop -> every candidate number from 2 to 100
    INNER loop -> every possible divisor of that candidate

The for-else is a perfect fit here:
    the inner loop finds a divisor -> break    -> the else is SKIPPED
    the inner loop finds nothing   -> no break -> the else RUNS -> prime

That removes the need for an is_prime flag variable entirely.

We start the outer loop at 2 because 1 is not prime - it has only one
divisor, and a prime must have exactly two.
"""

END = 100

print("=" * 55)
print("PRIME NUMBERS BETWEEN 1 AND", END)
print("=" * 55)

primes = []

for candidate in range(2, END + 1):                        # outer loop
    for divisor in range(2, int(candidate ** 0.5) + 1):    # inner loop
        if candidate % divisor == 0:
            break                                          # divisible -> not prime
    else:
        # no break happened -> no divisor found -> it is prime
        primes.append(candidate)

print(primes)
print()
print("How many primes :", len(primes))
print("Their total     :", sum(primes))
print("Smallest        :", primes[0])
print("Largest         :", primes[-1])
print()

# --- Displayed as a neat grid ----------------------------------------------
print("=" * 55)
print("AS A GRID, 10 PER LINE")
print("=" * 55)

position = 0
for p in primes:
    print(f"{p:>5}", end="")
    position += 1
    if position % 10 == 0:
        print()
print()
print()

# --- Showing why individual numbers were accepted or rejected --------------
print("=" * 55)
print("WHY SOME NUMBERS WERE REJECTED")
print("=" * 55)

for candidate in [2, 9, 17, 51, 91, 97]:
    for divisor in range(2, int(candidate ** 0.5) + 1):
        if candidate % divisor == 0:
            print(f"   {candidate:>3} -> divisible by {divisor}"
                  f"  ({candidate} = {divisor} x {candidate // divisor})  -> not prime")
            break
    else:
        print(f"   {candidate:>3} -> no divisor found  -> PRIME")

print()
print("51 is the interesting one - it looks prime, but 51 = 3 x 17.")
print()

# --- A visual map of 1 to 100 ----------------------------------------------
print("=" * 55)
print("MAP OF 1 TO 100   (P = prime, . = not prime)")
print("=" * 55)

for n in range(1, END + 1):
    if n in primes:
        print("  P", end="")
    else:
        print("  .", end="")
    if n % 10 == 0:
        print("   <- up to", n)
