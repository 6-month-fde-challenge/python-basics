"""
Question 6 - Count the Number of Digits in an Integer
======================================================
The same peel-a-digit loop again, but now the accumulator is a simple
COUNTER - we do not care what the digits are, only how many there were.

    while number > 0:
        count += 1
        number //= 10

THE EDGE CASE THAT CATCHES PEOPLE: the number 0.
0 > 0 is False, so the loop never runs and the count comes out as 0.
But 0 clearly has ONE digit, so it needs handling before the loop.

This is a good reminder that a while loop can run ZERO times. Its
condition is tested BEFORE the first pass, not after.
"""


def count_digits(number):
    """Return how many digits a whole number has."""
    number = abs(number)

    # EDGE CASE : 0 has one digit, but the loop below would never run for it
    if number == 0:
        return 1

    # INITIALIZATION : nothing counted yet
    count = 0

    # CONDITION : keep going while there are digits left to remove
    while number > 0:
        count += 1

        # UPDATE / TERMINATION : remove one digit per pass, so the number
        # shrinks towards 0 and the loop is guaranteed to end
        number //= 10

    return count


print("=" * 55)
print("COUNTING THE DIGITS OF 5832 - STEP BY STEP")
print("=" * 55)

number = 5832
working = number
count = 0

# CONDITION
while working > 0:
    count += 1
    print(f"   pass {count}: {working} has digits left "
          f"-> count = {count}, remaining = {working // 10}")
    # UPDATE
    working //= 10

print()
print(f"   RESULT: {number} has {count} digits")
print()

print("=" * 55)
print("MORE EXAMPLES")
print("=" * 55)

for value in [5832, 12345, 7, 0, 100, 999999, -4567]:
    print(f"   count_digits({value:>8}) = {count_digits(value)}")

print()
print("   0 is handled before the loop, because 0 > 0 is False and the")
print("   loop body would never run - giving a wrong answer of 0.")
print()

print("=" * 55)
print("A while LOOP CAN RUN ZERO TIMES")
print("=" * 55)
print("""
   The condition is tested BEFORE the first pass, not after. So:

       n = 0
       while n > 0:      <- False immediately
           ...           <- this body never executes once

   That is exactly why count_digits(0) needs its own line above the loop.
""")

print("=" * 55)
print("USING THE COUNT - THE LARGEST NUMBER WITH THAT MANY DIGITS")
print("=" * 55)

for value in [7, 42, 856, 9999]:
    digits = count_digits(value)
    print(f"   {value:>6} has {digits} digit(s)")
