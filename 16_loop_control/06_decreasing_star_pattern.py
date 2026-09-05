"""
Question 6 - Decreasing Star Pattern
=====================================
Required output:
    *****
    ****
    ***
    **
    *

Concept: counting DOWN with range().

range(start, stop, step) accepts a NEGATIVE step:
    range(5, 0, -1)  ->  5, 4, 3, 2, 1

Read it as: start at 5, go down by 1 each time, STOP BEFORE 0.
The stop value is always excluded - that is why it is 0 and not 1.
Writing range(5, 1, -1) would give 5,4,3,2 and lose the final row.

This is the only difference from Question 5. The inner loop is identical.
"""

ROWS = 5

print("=" * 40)
print("REQUIRED PATTERN")
print("=" * 40)

for row in range(ROWS, 0, -1):            # outer: 5,4,3,2,1
    for star in range(row):               # inner: runs 'row' times
        print("*", end="")
    print()

print()

# --- How each row is built -------------------------------------------------
print("=" * 40)
print("HOW EACH ROW IS BUILT")
print("=" * 40)
print("range(5, 0, -1) produces :", list(range(ROWS, 0, -1)))
print()
for row in range(ROWS, 0, -1):
    print(f"   row value {row}: inner loop runs {row} time(s) -> {'*' * row}")

print()

# --- The same result WITHOUT a negative step -------------------------------
print("=" * 40)
print("AN ALTERNATIVE WAY (counting up, subtracting)")
print("=" * 40)
print("Instead of counting down, count up and subtract from the total:")
for row in range(ROWS):                   # 0,1,2,3,4
    stars = ROWS - row                    # 5,4,3,2,1
    for star in range(stars):
        print("*", end="")
    print()
print("Same output - the negative step is just clearer to read.")
print()

# --- Both patterns together ------------------------------------------------
print("=" * 40)
print("BONUS - INCREASING THEN DECREASING (diamond half)")
print("=" * 40)
for row in range(1, ROWS + 1):
    print("*" * row)
for row in range(ROWS - 1, 0, -1):
    print("*" * row)
