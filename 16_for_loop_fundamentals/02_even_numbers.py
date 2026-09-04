"""
Question 2 - Print All Even Numbers From 1 to 100
==================================================
An EVEN number divides by 2 with no remainder:  n % 2 == 0

TWO WAYS TO DO THIS
   Method 1 - check every number and filter with an if
   Method 2 - use range()'s STEP so only even numbers are produced

Method 2 is better: it never even looks at the odd numbers, so it does
half the work. Method 1 is shown first because it is easier to read.

Sample output: 2 4 6 8 10 ... 96 98 100   (50 numbers)
"""

print("METHOD 1 - check every number with an if")
print("=" * 60)

count = 0
for n in range(1, 101):
    if n % 2 == 0:                    # remainder is 0 -> even
        print(n, end="  ")
        count += 1

print()
print("Even numbers found :", count)
print("Numbers examined   : 100")
print()

print("METHOD 2 - let range() do the work with a step of 2")
print("=" * 60)

count = 0
for n in range(2, 101, 2):            # start at 2, jump 2 at a time
    print(n, end="  ")
    count += 1

print()
print("Even numbers found :", count)
print("Numbers examined   :", count, "<- half the work, same answer")
print()

# --- Why the remainder test works ------------------------------------------
print("Why  n % 2 == 0  means 'even':")
for n in range(1, 9):
    print(f"   {n} % 2 = {n % 2}  ->", "EVEN" if n % 2 == 0 else "odd")

print()
print("Sum of all even numbers from 1 to 100 :", sum(range(2, 101, 2)))
