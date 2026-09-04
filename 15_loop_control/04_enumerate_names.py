"""
Question 4 - Numbered List of Names Using enumerate()
======================================================
Concept: enumerate() gives you the POSITION and the VALUE together.

WITHOUT enumerate you need a manual counter:
    count = 1
    for name in names:
        print(count, name)
        count += 1              <- easy to forget, easy to misplace

WITH enumerate Python keeps the counter for you:
    for index, name in enumerate(names, start=1):
        print(index, name)

start=1 is the important detail here. By default enumerate() begins at 0
(matching list indexes), but humans number lists from 1, and the required
output starts at 1 Aman.
"""

names = ["Aman", "Ravi", "Sudhanshu", "Priya", "Anjali"]

print("=" * 45)
print("REQUIRED OUTPUT")
print("=" * 45)

for index, name in enumerate(names, start=1):
    print(index, name)

print()

# --- What enumerate() actually produces ------------------------------------
print("=" * 45)
print("WHAT enumerate() PRODUCES")
print("=" * 45)
print("enumerate(names)          ->", list(enumerate(names)))
print("enumerate(names, start=1) ->", list(enumerate(names, start=1)))
print()
print("Each item is a (index, value) TUPLE, e.g.", list(enumerate(names))[0])
print("The loop line  'for index, name in ...'  unpacks that tuple into")
print("two separate variables on every pass.")
print()

# --- Default start (0) versus start=1 --------------------------------------
print("=" * 45)
print("start=0 (default) vs start=1")
print("=" * 45)
print(f"{'DEFAULT (0)':<20}{'start=1':<20}")
print("-" * 40)
for (i0, n0), (i1, n1) in zip(enumerate(names), enumerate(names, start=1)):
    print(f"{i0} {n0:<18}{i1} {n1:<18}")
print()

# --- The manual alternative, to show what enumerate saves you --------------
print("=" * 45)
print("THE MANUAL WAY (what enumerate replaces)")
print("=" * 45)
count = 1
for name in names:
    print(count, name)
    count += 1
print("Same output, but with an extra variable to create and remember to increase.")
print()

# --- A practical use: numbering with extra detail --------------------------
print("=" * 45)
print("A PRACTICAL USE")
print("=" * 45)
for position, name in enumerate(names, start=1):
    print(f"   {position}. {name:<12} ({len(name)} letters, index {position - 1})")
