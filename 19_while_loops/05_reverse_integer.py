"""
Question 5 - Reverse an Integer Using a while Loop
===================================================
    Input : 12345
    Output: 54321

Same digit-peeling technique as Question 4, but instead of ADDING each
digit we BUILD A NEW NUMBER with it:

    reversed_number = reversed_number * 10 + digit

Read that line carefully. Multiplying by 10 shifts everything already
collected one place to the LEFT, which frees up the units column for the
new digit. That is what puts the digits back in the opposite order.

Building 12345 in reverse:
    take 5  ->    0 * 10 + 5 =     5
    take 4  ->    5 * 10 + 4 =    54
    take 3  ->   54 * 10 + 3 =   543
    take 2  ->  543 * 10 + 2 =  5432
    take 1  -> 5432 * 10 + 1 = 54321
"""


def reverse_integer(number):
    """Return the digits of a whole number in reverse order."""
    negative = number < 0          # remember the sign
    number = abs(number)

    # INITIALIZATION : the result starts at 0 and is built up digit by digit
    reversed_number = 0

    # CONDITION : keep going while digits remain to be peeled off
    while number > 0:
        digit = number % 10                          # take the last digit
        reversed_number = reversed_number * 10 + digit   # shift left, add it

        # UPDATE / TERMINATION : drop that digit, so number shrinks to 0
        number //= 10

    if negative:
        return -reversed_number
    return reversed_number


print("=" * 60)
print("REVERSING 12345 - STEP BY STEP")
print("=" * 60)

number = 12345
working = number
reversed_number = 0
step = 1

# INITIALIZATION done above: working copy and the result accumulator
# CONDITION : while digits remain
while working > 0:
    digit = working % 10
    new_value = reversed_number * 10 + digit
    print(f"   pass {step}: take {digit}  ->  {reversed_number} * 10 + {digit}"
          f" = {new_value}   (remaining: {working // 10})")
    reversed_number = new_value
    # UPDATE
    working //= 10
    step += 1

print()
print(f"   RESULT: {number} reversed is {reversed_number}")
print()

print("=" * 60)
print("MORE EXAMPLES")
print("=" * 60)

for value in [12345, 1000, 7, 90, 5832, -678, 0]:
    print(f"   reverse_integer({value:>7}) = {reverse_integer(value)}")

print()
print("   1000 reverses to 1 - the leading zeros of 0001 simply do not")
print("   exist in a number. That is correct arithmetic, not a bug.")
print()

print("=" * 60)
print("USING THE REVERSAL TO CHECK FOR A PALINDROME NUMBER")
print("=" * 60)


def is_palindrome_number(number):
    """Return True if the number reads the same forwards and backwards."""
    return number == reverse_integer(number)


for value in [121, 12321, 12345, 7, 1001]:
    if is_palindrome_number(value):
        print(f"   {value:>6} -> palindrome")
    else:
        print(f"   {value:>6} -> not a palindrome")
