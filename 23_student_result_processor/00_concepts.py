"""
00_concepts.py - the basics behind exercise 23
==============================================
Run this first:

    python 00_concepts.py

A plain top-to-bottom script - no functions, nothing clever. Read it
from the first line to the last and you will know enough to read the
application in this folder.

    1  without try/except the program stops
    2  try / except
    3  try / except / else / finally
    4  raise, and your own exception class
    5  the try goes INSIDE the loop
"""

marks = ["88", "92", "seventy", "65"]


# ===========================================================
print()
print("1. Without try/except the program stops")
print("=" * 50)

print("marks =", marks)
print()
print("total = 0")
print("for m in marks:")
print("    total += int(m)")
print()

total = 0
try:
    for mark in marks:
        total += int(mark)
except ValueError as error:
    print("ValueError:", error)

print()
print("It stopped on 'seventy'. total is", total, "- the 65 was never added,")
print("and nothing after the loop would run.")


# ===========================================================
print()
print("2. try / except")
print("=" * 50)

print("for m in marks:")
print("    try:")
print("        total += int(m)")
print("    except ValueError:")
print("        skipped.append(m)")
print()

total = 0
skipped = []

for mark in marks:
    try:
        total += int(mark)
    except ValueError:
        skipped.append(mark)

print("total   =", total)
print("skipped =", skipped)
print()
print("The bad item is handled, the loop keeps going, and we know what")
print("was skipped instead of quietly getting a wrong answer.")


# ===========================================================
print()
print("3. try / except / else / finally")
print("=" * 50)

print("with a good value, '42':")
try:
    number = int("42")
except ValueError:
    print("   except ran")
else:
    print("   else ran    (no error happened)")
finally:
    print("   finally ran")

print()
print("with a bad value, 'oops':")
try:
    number = int("oops")
except ValueError:
    print("   except ran  (an error happened)")
else:
    print("   else ran")
finally:
    print("   finally ran")

print()
print("   try      always")
print("   except   an error happened")
print("   else     NO error happened")
print("   finally  always - the place for cleanup you cannot skip")


# ===========================================================
print()
print("4. raise, and your own exception class")
print("=" * 50)


class InvalidMarksError(Exception):
    """Our own error - the one the assignment asks for."""


mark = 105

try:
    if mark < 0 or mark > 100:
        raise InvalidMarksError(str(mark) + " is not between 0 and 100")
    print("mark accepted:", mark)
except InvalidMarksError as error:
    print("InvalidMarksError:", error)

print()
print("105 is a valid number, so Python will not complain about it.")
print("Only our rules know it is wrong - so we `raise`.")
print()
print("   class InvalidMarksError(Exception):")
print("       pass")
print()
print("Our own class lets us catch OUR errors by name, so a real bug in")
print("our code is not mistaken for bad student data.")


# ===========================================================
print()
print("5. The try goes INSIDE the loop")
print("=" * 50)

rows = ["88", "92", "seventy", "65", "95"]
print("rows =", rows)
print()

# try around the WHOLE loop - the first bad row ends everything
done = []
try:
    for raw in rows:
        done.append(float(raw))
except ValueError:
    pass
print("try OUTSIDE the loop ->", len(done), "of 5 done ", done)

# try around ONE item - a bad row costs one row
done = []
for raw in rows:
    try:
        done.append(float(raw))
    except ValueError:
        continue
print("try INSIDE  the loop ->", len(done), "of 5 done ", done)

print()
print("Same loop, one line moved. This is the whole point of exercise 23:")
print("log the error and carry on with the remaining students.")

print()
print("Next: read exceptions.py, then run `python main.py`.")
print()
