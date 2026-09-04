"""
Question 4 - Sum of the Digits of a Number
===========================================
    Input : 5832
    Output: 18        (5 + 8 + 3 + 2)

THIS IS WHERE while BEATS for.
A for loop needs to know how many passes to make. Here the number of
passes is the number of DIGITS, which is not known until the work is
done. The while condition `number > 0` discovers it naturally.

THE TWO OPERATIONS THAT DO ALL THE WORK
    number % 10   -> the LAST digit          5832 % 10  = 2
    number // 10  -> everything EXCEPT it    5832 // 10 = 583

So each pass peels one digit off the right-hand end. When every digit
has been removed the number becomes 0, the condition fails, and the
loop ends by itself.
"""


def sum_of_digits(number):
    """Return the sum of the digits of a whole number."""
    # Negatives are handled by taking the absolute value first
    number = abs(number)

    # INITIALIZATION : the accumulator starts at 0, before the loop
    total = 0

    # CONDITION : keep peeling digits while any are left.
    #             When number reaches 0 there is nothing more to take.
    while number > 0:
        digit = number % 10        # take the last digit
        total += digit             # add it to the running total

        # UPDATE / TERMINATION : remove that digit with integer division.
        # The number shrinks every pass, so it must eventually reach 0.
        number //= 10

    return total


print("=" * 55)
print("SUM OF DIGITS - STEP BY STEP FOR 5832")
print("=" * 55)

number = 5832
total = 0
step = 1

# INITIALIZATION : working copy of the number, and the accumulator
working = number

# CONDITION : while digits remain
while working > 0:
    digit = working % 10
    total += digit
    print(f"   pass {step}: {working} % 10 = {digit}   "
          f"-> total = {total}   -> {working} // 10 = {working // 10}")
    # UPDATE
    working //= 10
    step += 1

print()
print(f"   RESULT: sum of the digits of {number} is {total}")
print()

print("=" * 55)
print("MORE EXAMPLES")
print("=" * 55)

for value in [5832, 12345, 999, 7, 1000, 0, -456]:
    print(f"   sum_of_digits({value:>7}) = {sum_of_digits(value)}")

print()
print("   0 gives 0 because the loop never runs - the condition is False")
print("   from the very start.")
print()

print("=" * 55)
print("WHY while AND NOT for")
print("=" * 55)
print("""
   A for loop needs a known number of passes. Here the pass count is the
   number of DIGITS, which nobody knows until the number has been taken
   apart. The condition `number > 0` finds the end on its own.

   You could convert the number to a string and use for char in str(n),
   but that sidesteps the arithmetic the question is testing.
""")
