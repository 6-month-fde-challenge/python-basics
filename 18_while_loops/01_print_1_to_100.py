"""
Question 1 - Print Numbers From 1 to 100 Using while
=====================================================
EVERY while LOOP HAS THREE PARTS. Get one wrong and the loop either
never runs or never stops.

    1. INITIALIZATION - create the counter BEFORE the loop
    2. CONDITION      - the test at the top; while it is True, the loop runs
    3. UPDATE         - change the counter INSIDE the loop, so the
                        condition eventually becomes False

A `for` loop hides all three inside range(). A `while` loop makes you
write them yourself - which is why while is the right tool when the
number of passes is NOT known in advance.
"""

print("Numbers from 1 to 100 using while")
print("=" * 60)

# INITIALIZATION : the counter starts at 1, before the loop begins
n = 1

# CONDITION : keep looping while n is 100 or less.
#             The moment n becomes 101 this is False and the loop ends.
while n <= 100:
    print(n, end="  ")

    # UPDATE / TERMINATION : n grows by 1 on every pass.
    # This line is what guarantees the loop ends. Remove it and n stays
    # at 1 forever, the condition stays True, and the program hangs.
    n += 1

print()
print("=" * 60)
print("Loop finished. n is now", n, "which failed the condition n <= 100.")
print()

# --- The same job with a for loop, for comparison --------------------------
print("=" * 60)
print("THE SAME THING WITH for")
print("=" * 60)
print("for n in range(1, 101):  ->  range() handles all three parts for you")
print()
print("   for   is better here: the count is known in advance (exactly 100).")
print("   while is better when you do NOT know how many passes are needed -")
print("         waiting for correct input, or for a user to choose Exit.")
print()

# --- What an infinite loop looks like (described, not run) -----------------
print("=" * 60)
print("HOW ACCIDENTAL INFINITE LOOPS HAPPEN")
print("=" * 60)
print("""
   n = 1
   while n <= 100:
       print(n)        <- no update line!

   n never changes, so n <= 100 stays True forever.
   The three-part checklist exists to prevent exactly this.
""")

# --- Counting in tens, to show the update need not be +1 -------------------
print("=" * 60)
print("THE UPDATE STEP DOES NOT HAVE TO BE 1")
print("=" * 60)

# INITIALIZATION
n = 10
# CONDITION : run while n has not passed 100
while n <= 100:
    print(n, end="  ")
    # UPDATE : jump by 10 instead of 1 - still guaranteed to terminate
    n += 10
print()
