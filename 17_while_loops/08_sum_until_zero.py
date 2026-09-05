"""
Question 8 - Keep Asking for Numbers Until the User Enters 0
=============================================================
THIS IS THE CLEAREST CASE FOR while OVER for.

A for loop must be told how many passes to make. Here nobody knows -
the user might enter three numbers or thirty, and they decide when to
stop by typing 0. The loop is controlled by a CONDITION, not a count.
That is the definition of condition-controlled iteration.

0 is called a SENTINEL VALUE: a special input whose only job is to
signal "stop". It is not added to the total.

SAMPLE RUN
    Enter a number: 10
    Enter a number: 25
    Enter a number: 5
    Enter a number: 0
    Sum of all entered numbers: 40
"""

print("=" * 55)
print("NUMBER TOTALLER")
print("=" * 55)
print("Enter numbers one at a time. Enter 0 when you are finished.")
print()

# INITIALIZATION : the accumulator and the counter both start before the loop.
# `number` is set to a non-zero value so the loop is guaranteed to run once.
total = 0
count = 0
number = None

# CONDITION : keep looping until the sentinel value 0 is entered.
# Because `number` starts as None, this is True on the first check.
while number != 0:
    entry = input("   Enter a number (0 to finish) : ")

    # Reject anything that is not a number, without ending the loop
    try:
        number = int(entry)
    except ValueError:
        print(f"      '{entry}' is not a whole number. Try again.")
        number = None              # keep the loop alive
        continue

    # UPDATE / TERMINATION : the loop ends when the user types 0.
    # The user controls termination, which is why a for loop cannot be used.
    if number == 0:
        print("      0 entered - stopping.")
    else:
        total += number
        count += 1
        print(f"      added {number}  ->  running total = {total}")

print()
print("=" * 55)
print("RESULT")
print("=" * 55)
print("   Numbers entered :", count)
print("   SUM OF ALL NUMBERS :", total)

if count > 0:
    print("   Average         :", round(total / count, 2))
else:
    print("   Average         : not available - no numbers were entered")

print()
print("=" * 55)
print("WHY while AND NOT for")
print("=" * 55)
print("""
   A for loop needs the pass count up front:
       for i in range(???):     <- how many? Nobody knows.

   The number of passes here is decided by the PERSON TYPING, at run time.
   Only a condition-controlled loop can express that. The sentinel value 0
   is what turns the condition False and ends the program.
""")
