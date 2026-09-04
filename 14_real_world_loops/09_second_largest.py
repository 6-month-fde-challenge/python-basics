"""
Question 9 - Find the Second-Largest Number WITHOUT sort()
===========================================================
Concept: tracking TWO champions at the same time.

THE LOGIC on each number:
    if it beats the largest        -> the old largest becomes second, this becomes largest
    elif it beats the second only  -> this becomes second (largest is unchanged)
    else                           -> ignore it

THE ORDER OF THOSE TWO LINES MATTERS. The old largest must be pushed
down into second BEFORE largest is overwritten, or it is lost forever.

DUPLICATES: a value equal to the largest is skipped, so the answer is the
second-largest DISTINCT value. In [99, 99, 88] the answer is 88, not 99.
"""

numbers = [45, 88, 12, 99, 67, 99, 23]

print("Numbers :", numbers)
print()

# Start both champions at the first value
largest = numbers[0]
second = None                     # None means "not found yet"

print("Checking each number:")
for n in numbers:
    if n > largest:
        second = largest          # push the old winner down FIRST
        largest = n               # then crown the new winner
        print(f"   {n} is a new LARGEST (old largest {second} becomes second)")
    elif n < largest and (second is None or n > second):
        second = n
        print(f"   {n} is the new SECOND largest")
    else:
        print(f"   {n} changes nothing")

print()
print("Largest number        :", largest)
print("SECOND LARGEST number :", second)
print()

# --- Edge case: what if every number is the same? --------------------------
print("=" * 50)
print("EDGE CASE - all values identical")
print("=" * 50)

same = [50, 50, 50]
big = same[0]
second_big = None
for n in same:
    if n > big:
        second_big = big
        big = n
    elif n < big and (second_big is None or n > second_big):
        second_big = n

print("List :", same)
print("Largest :", big)
if second_big is None:
    print("Second largest : does not exist - every value is the same.")
else:
    print("Second largest :", second_big)
