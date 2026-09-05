"""
Question 8 - A Function That Sums a List WITHOUT sum()
=======================================================
The accumulator pattern, wrapped in a function.

    total = 0                 <- start OUTSIDE the loop
    for value in numbers:
        total += value        <- grow it on every pass
    return total

WHY total = 0 MUST BE OUTSIDE THE LOOP: if it were inside, it would reset
on every pass and the answer would just be the last element.

The built-in sum() is not used to solve the problem. It appears once at
the very end only to VERIFY that the hand-written loop is correct.

AN EMPTY LIST correctly returns 0, because the loop simply never runs.
"""


def list_sum(numbers):
    """Return the total of all numbers in a list, without using sum()."""
    total = 0
    for value in numbers:
        total += value
    return total


def list_average(numbers):
    """Return the average of a list, or None if the list is empty."""
    if len(numbers) == 0:
        return None                    # avoid dividing by zero
    return list_sum(numbers) / len(numbers)


print("=" * 55)
print("SUMMING LISTS")
print("=" * 55)

tests = [
    [10, 20, 30, 40, 50],
    [1, 2, 3],
    [100],
    [],
    [-5, 10, -3, 8],
    [1.5, 2.5, 3.0],
]

for numbers in tests:
    print(f"   list_sum({str(numbers):<22}) = {list_sum(numbers)}")

print()
print("   The empty list gives 0 because the loop body never runs.")
print()

print("=" * 55)
print("A VERSION THAT SHOWS ITS WORKING")
print("=" * 55)


def list_sum_verbose(numbers):
    """Return the total of a list, printing the running total each step."""
    total = 0
    print("      start: total = 0")
    for value in numbers:
        total += value
        print(f"      + {value:<5} -> total = {total}")
    return total


print("   list_sum_verbose([10, 20, 30, 40, 50])")
print("   RESULT:", list_sum_verbose([10, 20, 30, 40, 50]))
print()

print("=" * 55)
print("REUSING list_sum() INSIDE ANOTHER FUNCTION")
print("=" * 55)

marks = [78, 92, 45, 67, 88]
print("   Marks   :", marks)
print("   Total   :", list_sum(marks))
print("   Average :", round(list_average(marks), 2))
print("   Empty list average :", list_average([]), " <- None, not a crash")
print()
print("   list_average() calls list_sum() instead of repeating the loop.")
print("   That reuse is the main reason to write functions at all.")
print()

print("=" * 55)
print("VERIFICATION AGAINST THE BUILT-IN sum()")
print("=" * 55)
for numbers in tests:
    print(f"   {str(numbers):<22} loop: {list_sum(numbers):<8} "
          f"sum(): {sum(numbers):<8} match: {list_sum(numbers) == sum(numbers)}")
