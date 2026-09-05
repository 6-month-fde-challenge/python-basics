"""
Question 3 - Print All Odd Numbers From 1 to 100
=================================================
An ODD number leaves a remainder of 1 when divided by 2:  n % 2 == 1

This is the mirror image of Question 2. The only changes are
   the test      n % 2 == 1   instead of   n % 2 == 0
   the start     range(1, ...) instead of  range(2, ...)

Sample output: 1 3 5 7 9 ... 95 97 99   (50 numbers)
"""

print("METHOD 1 - check every number with an if")
print("=" * 60)

count = 0
for n in range(1, 101):
    if n % 2 == 1:                    # remainder is 1 -> odd
        print(n, end="  ")
        count += 1

print()
print("Odd numbers found :", count)
print()

print("METHOD 2 - start at 1 and step by 2")
print("=" * 60)

count = 0
for n in range(1, 101, 2):            # start at 1, jump 2 at a time
    print(n, end="  ")
    count += 1

print()
print("Odd numbers found :", count)
print()

# --- The two tests that both mean 'odd' ------------------------------------
print("Two ways to write the odd test:")
print("   n % 2 == 1   -> remainder is exactly 1")
print("   n % 2 != 0   -> remainder is NOT 0")
print("Both give the same result for positive numbers.")
print()

print("Comparing even and odd across 1 to 100:")
print("   Even count :", len(range(2, 101, 2)))
print("   Odd count  :", len(range(1, 101, 2)))
print("   Together   :", len(range(2, 101, 2)) + len(range(1, 101, 2)), "= all 100 numbers")
print("   Sum of odds:", sum(range(1, 101, 2)))
