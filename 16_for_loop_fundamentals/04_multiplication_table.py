"""
Question 4 - Multiplication Table of n, from 1 to 20
=====================================================
Concept: a for loop over range(1, 21) with a value supplied by the user.

input() ALWAYS returns a string, even when the user types digits.
    "7" * 3  would give  "777"   (string repetition)
    7 * 3    gives       21      (multiplication)
So int() must convert the input before any maths is done.

Sample input : 7
Sample output: 7 x 1 = 7
               7 x 2 = 14
               ...
               7 x 20 = 140
"""

print("=" * 45)
print("MULTIPLICATION TABLE GENERATOR")
print("=" * 45)

entry = input("Enter a number : ")

try:
    n = int(entry)                    # convert text to a whole number
except ValueError:
    print("'" + entry + "' is not a valid whole number.")
    raise SystemExit

print()
print(f"Multiplication table of {n}, from 1 to 20")
print("-" * 45)

for i in range(1, 21):                # 1 to 20 inclusive
    product = n * i
    print(f"   {n} x {i:>2} = {product}")

print("-" * 45)
print("Rows printed :", 20)
print()

# --- Why int() is needed ---------------------------------------------------
print("Why int() is necessary:")
print(f"   input() gave  '{entry}'  which is a {type(entry).__name__}")
print(f"   int() made it  {n}      which is an {type(n).__name__}")
print(f"   '{entry}' * 3 would give  '{entry * 3}'   (text repeated)")
print(f"   {n} * 3 gives  {n * 3}   (real multiplication)")
