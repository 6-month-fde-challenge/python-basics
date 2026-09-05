"""
Question 9 - Build a List of Unique Elements WITHOUT set()
===========================================================
Concept: the "check before you add" pattern.

    for item in original:
        if item not in unique:      <- have we already stored it?
            unique.append(item)     <- no, so store it now

set(data) would solve this in one call, but that bypasses the technique
being practised, so it is not used here.

A BONUS ADVANTAGE OF DOING IT MANUALLY: this keeps the ORIGINAL ORDER.
set() would remove duplicates but scramble the order, and could not be
used on unhashable items at all.
"""

numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60, 10]

print("Original list :", numbers)
print("Length        :", len(numbers))
print()

unique = []                            # start empty

print("Deciding on each element:")
for item in numbers:
    if item not in unique:
        unique.append(item)
        print(f"   {item:>3} -> not seen before -> ADDED   (list is now {unique})")
    else:
        print(f"   {item:>3} -> already present -> skipped")

print()
print("=" * 50)
print("RESULT")
print("=" * 50)
print("Unique list      :", unique)
print("Original length  :", len(numbers))
print("Unique length    :", len(unique))
print("Duplicates removed:", len(numbers) - len(unique))
print()

# --- The same technique on a list of names ---------------------------------
print("=" * 50)
print("SECOND EXAMPLE - names")
print("=" * 50)

names = ["Rahul", "Priya", "Aman", "Priya", "Rahul", "Sneha", "Aman"]
unique_names = []

for name in names:
    if name not in unique_names:
        unique_names.append(name)

print("Original :", names)
print("Unique   :", unique_names)
print()

# --- Why order is preserved, unlike set() ----------------------------------
print("=" * 50)
print("THE ADVANTAGE OVER set()")
print("=" * 50)
print("Our loop result  :", unique, "<- original order kept")
print("set() would give :", set(numbers), "<- order not guaranteed")
print()
print("The loop visits elements in order and appends the first time each")
print("one appears, so the first-seen order is preserved exactly.")
