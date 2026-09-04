"""
Question 2 - Print Numbers From 100 Down to 1
==============================================
Counting DOWN changes two of the three parts of the loop:

    INITIALIZATION - start at the TOP (100) instead of the bottom
    CONDITION      - keep going while n is still ABOVE OR EQUAL TO 1
    UPDATE         - SUBTRACT 1 each pass instead of adding

THE CLASSIC BUG: writing  n += 1  by habit while counting down. The
counter then runs away from the condition instead of towards it, and
the loop never ends. The update must always move the counter TOWARDS
making the condition False.
"""

print("Numbers from 100 down to 1 using while")
print("=" * 60)

# INITIALIZATION : start at the highest value
n = 100

# CONDITION : keep looping while n has not yet dropped below 1.
#             When n reaches 0 this becomes False and the loop stops.
while n >= 1:
    print(n, end="  ")

    # UPDATE / TERMINATION : n shrinks by 1 each pass, moving towards 0.
    # Using n += 1 here would move away from the condition forever.
    n -= 1

print()
print("=" * 60)
print("Loop finished. n is now", n, "which failed the condition n >= 1.")
print()

# --- Counting down in steps ------------------------------------------------
print("=" * 60)
print("COUNTING DOWN IN TENS")
print("=" * 60)

# INITIALIZATION
n = 100
# CONDITION
while n >= 10:
    print(n, end="  ")
    # UPDATE : drop by 10 each pass
    n -= 10
print()
print()

# --- A countdown, the most natural use of counting down --------------------
print("=" * 60)
print("A ROCKET COUNTDOWN")
print("=" * 60)

# INITIALIZATION
count = 10
# CONDITION : keep counting while there is something left to count
while count > 0:
    print("   T minus", count)
    # UPDATE : move towards zero
    count -= 1
print("   LIFT OFF!")
print()

# --- Why the update direction matters --------------------------------------
print("=" * 60)
print("WHY THE UPDATE DIRECTION MATTERS")
print("=" * 60)
print("""
   BROKEN (an infinite loop):
       n = 100
       while n >= 1:
           print(n)
           n += 1        <- n grows: 101, 102, 103 ... never below 1

   CORRECT:
       n = 100
       while n >= 1:
           print(n)
           n -= 1        <- n shrinks towards 0, so the loop ends

   The update must always push the counter TOWARDS failing the condition.
""")
