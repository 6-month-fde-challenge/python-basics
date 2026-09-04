"""
Question 3 - Print All Even Numbers Between 1 and 100
======================================================
TWO WAYS, and they differ in which part of the loop does the work.

METHOD 1 - update by 1, and filter with an if
    the loop visits all 100 numbers and skips the odd ones

METHOD 2 - start at 2 and update by 2
    the loop only ever lands on even numbers, so no if is needed

Method 2 is better: it does half the passes and has no condition to
evaluate inside the body. The "filter" has been moved into the UPDATE
step itself.
"""

print("=" * 60)
print("METHOD 1 - visit every number, filter with an if")
print("=" * 60)

# INITIALIZATION : start at the first number in the range
n = 1
count = 0

# CONDITION : keep going while n has not passed 100
while n <= 100:
    if n % 2 == 0:                 # only even numbers get printed
        print(n, end="  ")
        count += 1

    # UPDATE / TERMINATION : step by 1, so all 100 numbers are visited
    n += 1

print()
print("Even numbers found :", count)
print("Numbers visited    : 100")
print()

print("=" * 60)
print("METHOD 2 - start at 2 and step by 2")
print("=" * 60)

# INITIALIZATION : start at the first EVEN number
n = 2
count = 0

# CONDITION : keep going while n has not passed 100
while n <= 100:
    print(n, end="  ")
    count += 1

    # UPDATE / TERMINATION : stepping by 2 means every value of n is
    # already even, so no if-check is needed inside the loop at all.
    n += 2

print()
print("Even numbers found :", count)
print("Numbers visited    :", count, "<- half the work, identical output")
print()

# --- Why n % 2 == 0 means "even" -------------------------------------------
print("=" * 60)
print("WHY  n % 2 == 0  MEANS EVEN")
print("=" * 60)

# INITIALIZATION
n = 1
# CONDITION : just the first eight numbers, to show the pattern
while n <= 8:
    if n % 2 == 0:
        print(f"   {n} % 2 = {n % 2}  ->  EVEN")
    else:
        print(f"   {n} % 2 = {n % 2}  ->  odd")
    # UPDATE
    n += 1

print()

# --- The running total of the even numbers ---------------------------------
print("=" * 60)
print("SUM OF ALL EVEN NUMBERS FROM 1 TO 100")
print("=" * 60)

# INITIALIZATION : the counter and the accumulator both start before the loop
n = 2
total = 0

# CONDITION
while n <= 100:
    total += n
    # UPDATE
    n += 2

print("   Total :", total)
