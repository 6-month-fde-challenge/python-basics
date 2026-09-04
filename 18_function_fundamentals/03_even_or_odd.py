"""
Question 3 - Determine Whether a Number Is Even or Odd
=======================================================
The whole decision lives INSIDE the function. The code outside only
supplies values and displays what comes back.

    n % 2 == 0  ->  even
    otherwise   ->  odd

Two versions are written, because they return DIFFERENT KINDS of answer:
    check_even_odd() returns a STRING  - good for displaying
    is_even()        returns a BOOLEAN - good for deciding
Which one to write depends on what the caller needs to do next.
"""


def check_even_odd(number):
    """Return the string 'Even' or 'Odd' for the given number."""
    if number % 2 == 0:
        return "Even"
    return "Odd"


def is_even(number):
    """Return True if the number is even, False if it is odd."""
    return number % 2 == 0


print("=" * 50)
print("check_even_odd() - returns a word")
print("=" * 50)

for n in [10, 7, 0, -4, -9, 100, 33]:
    print(f"   {n:>5} -> {check_even_odd(n)}")

print()
print("=" * 50)
print("is_even() - returns True or False")
print("=" * 50)

for n in [10, 7, 0, -4]:
    print(f"   is_even({n:>3}) -> {is_even(n)}")

print()
print("=" * 50)
print("WHY A BOOLEAN VERSION IS USEFUL")
print("=" * 50)
print("A boolean can be used directly in an if, or to filter a list:")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
odds = []
for n in numbers:
    if is_even(n):
        evens.append(n)
    else:
        odds.append(n)

print("   All numbers :", numbers)
print("   Evens       :", evens)
print("   Odds        :", odds)
print()

print("=" * 50)
print("HOW THE TEST WORKS")
print("=" * 50)
for n in range(1, 7):
    print(f"   {n} % 2 = {n % 2}  ->  {check_even_odd(n)}")
print()
print("Zero is even: 0 % 2 =", 0 % 2, "->", check_even_odd(0))
print("Negatives work too: -4 % 2 =", -4 % 2, "->", check_even_odd(-4))
