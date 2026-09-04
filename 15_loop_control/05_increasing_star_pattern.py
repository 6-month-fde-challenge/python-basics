"""
Question 5 - Increasing Star Pattern
=====================================
Required output:
    *
    **
    ***
    ****
    *****

Concept: NESTED LOOPS.
    OUTER loop -> controls the ROWS    (how many lines are printed)
    INNER loop -> controls the COLUMNS (how many stars are on that line)

The trick is that the inner loop's length DEPENDS on the outer counter:
row 1 prints 1 star, row 4 prints 4 stars -> range(row).

print("*", end="") stops print() from starting a new line, so the stars
build up across one row. The bare print() afterwards ends the row.
"""

ROWS = 5

print("=" * 35)
print("REQUIRED PATTERN")
print("=" * 35)

for row in range(1, ROWS + 1):            # outer: rows 1,2,3,4,5
    for star in range(row):               # inner: runs 'row' times
        print("*", end="")                # stay on the same line
    print()                               # end this row

print()

# --- How each row is built -------------------------------------------------
print("=" * 35)
print("HOW EACH ROW IS BUILT")
print("=" * 35)
for row in range(1, ROWS + 1):
    print(f"   row {row}: inner loop runs {row} time(s) -> {'*' * row}")

print()
print("Total stars printed :", 1 + 2 + 3 + 4 + 5)
print()

# --- Related shapes from the same skeleton ---------------------------------
print("=" * 35)
print("SAME SKELETON, OTHER SHAPES")
print("=" * 35)

print("\nA) Right aligned:")
for row in range(1, ROWS + 1):
    for space in range(ROWS - row):
        print(" ", end="")
    for star in range(row):
        print("*", end="")
    print()

print("\nB) Pyramid:")
for row in range(1, ROWS + 1):
    for space in range(ROWS - row):
        print(" ", end="")
    for star in range(2 * row - 1):
        print("*", end="")
    print()
