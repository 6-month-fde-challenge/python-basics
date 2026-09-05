"""
Question 6 - Factorial WITHOUT a Built-in Factorial Function
=============================================================
The factorial of n (written n!) is every whole number from 1 to n
multiplied together.

    5! = 1 x 2 x 3 x 4 x 5 = 120

Concept: the accumulator pattern again, but MULTIPLYING instead of adding.

THE CRITICAL DIFFERENCE FROM A SUM:
    a sum starts at         0    (adding 0 changes nothing)
    a factorial starts at   1    (multiplying by 1 changes nothing)
Starting a factorial at 0 would make every answer 0, because anything
multiplied by 0 is 0.

SPECIAL CASE: 0! is defined as 1, not 0.

Sample input : 5
Sample output: 120
"""

print("=" * 45)
print("FACTORIAL CALCULATOR")
print("=" * 45)

entry = input("Enter a number : ")

try:
    n = int(entry)
except ValueError:
    print("'" + entry + "' is not a valid whole number.")
    raise SystemExit

if n < 0:
    print("Factorial is not defined for negative numbers.")
    raise SystemExit

# The accumulator starts at 1, NOT 0
factorial = 1

print()
if n == 0:
    print("0! is defined as 1 by convention.")
else:
    print("Multiplying one number at a time:")
    for i in range(1, n + 1):
        factorial *= i
        print(f"   x {i:>3}  ->  running product = {factorial}")

print()
print("=" * 45)
print(f"{n}! = {factorial}")
print("=" * 45)
print()

# --- Show the full expression ----------------------------------------------
if n > 0:
    expression = ""
    for i in range(1, n + 1):
        expression += str(i)
        if i < n:
            expression += " x "
    print(f"Working: {n}! = {expression} = {factorial}")
print()

# --- Why the accumulator starts at 1 ---------------------------------------
print("Why the accumulator starts at 1 and not 0:")
wrong = 0
for i in range(1, 6):
    wrong *= i
print("   Starting at 0 -> 5! comes out as", wrong, "(everything x 0 is 0)")
print("   Starting at 1 -> 5! comes out as 120 (correct)")
print()

# --- A small factorial table -----------------------------------------------
print("Factorials from 0 to 10:")
running = 1
print("   0! = 1")
for i in range(1, 11):
    running *= i
    print(f"   {i}! = {running}")
