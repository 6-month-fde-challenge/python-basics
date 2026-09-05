"""
Question 11 - Number Pattern
============================
Required output:
    1
    12
    123
    1234
    12345

Concept: NESTED LOOPS.
    the OUTER loop controls the ROWS      (how many lines)
    the INNER loop controls the COLUMNS   (what goes on each line)

The key is that the inner loop's length DEPENDS on the outer loop's
counter - row 1 prints 1 number, row 4 prints 4 numbers.

print(x, end="") stops print() from moving to a new line, so the
numbers stay on the same row. The empty print() after the inner loop
then ends the row.
"""

ROWS = 5

print("=" * 40)
print("THE REQUIRED PATTERN")
print("=" * 40)

for row in range(1, ROWS + 1):            # outer loop: rows 1,2,3,4,5
    for col in range(1, row + 1):         # inner loop: 1 up to the row number
        print(col, end="")                # stay on the same line
    print()                               # end of the row -> move to the next line

print()

# --- The same pattern, with the working shown ------------------------------
print("=" * 40)
print("HOW EACH ROW IS BUILT")
print("=" * 40)

for row in range(1, ROWS + 1):
    line = ""
    for col in range(1, row + 1):
        line += str(col)
    print(f"   row {row}: inner loop runs {row} time(s) -> prints {line}")

print()

# --- Related patterns built from the same nested-loop skeleton -------------
print("=" * 40)
print("BONUS - SAME SKELETON, DIFFERENT PATTERNS")
print("=" * 40)

print("\nA) Repeated row number:")
for row in range(1, ROWS + 1):
    for col in range(1, row + 1):
        print(row, end="")
    print()

print("\nB) Star triangle:")
for row in range(1, ROWS + 1):
    for col in range(1, row + 1):
        print("*", end="")
    print()

print("\nC) Reversed (counting down):")
for row in range(ROWS, 0, -1):
    for col in range(1, row + 1):
        print(col, end="")
    print()

print("\nD) Right aligned:")
for row in range(1, ROWS + 1):
    for space in range(ROWS - row):
        print(" ", end="")
    for col in range(1, row + 1):
        print(col, end="")
    print()
