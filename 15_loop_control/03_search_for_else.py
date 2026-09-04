"""
Question 3 - Search a List Using for-else
==========================================
Concept: the `else` block attached to a `for` loop.

THIS IS THE MOST MISUNDERSTOOD FEATURE IN PYTHON. The rule is simple:

    the for-else block runs ONLY IF the loop finished WITHOUT hitting break

So it does not mean "otherwise". A better name would be "no-break".

    for item in data:
        if item == target:
            print("Number Found")
            break                 <- break SKIPS the else
    else:
        print("Number Not Found") <- runs only when break never happened

WHY IT IS USEFUL: without for-else you need an extra flag variable
(found = False ... found = True ... if not found:). The else block
removes the need for that flag entirely.
"""

numbers = [12, 45, 7, 89, 23, 56, 91, 34, 68, 5]

print("=" * 55)
print("NUMBER SEARCH")
print("=" * 55)
print("List :", numbers)
print()

entry = input("Enter a number to search for : ")

try:
    target = int(entry)
except ValueError:
    print(f"'{entry}' is not a valid number.")
    raise SystemExit

print()
print("Searching...")

for index, value in enumerate(numbers):
    print(f"   position {index}: is {value} == {target}?", value == target)
    if value == target:
        print()
        print("Number Found")
        print(f"   {target} is at index {index} (position {index + 1} in the list)")
        break
else:
    # reached only when the for loop ran all the way through with no break
    print()
    print("Number Not Found")
    print(f"   {target} does not appear anywhere in the list")

print()

# --- The same logic, demonstrated on several values ------------------------
print("=" * 55)
print("AUTOMATIC TESTS - found and not-found cases")
print("=" * 55)

for test in [7, 91, 100, 5, 42]:
    for value in numbers:
        if value == test:
            print(f"   Searching {test:>4} -> Number Found")
            break
    else:
        print(f"   Searching {test:>4} -> Number Not Found")
