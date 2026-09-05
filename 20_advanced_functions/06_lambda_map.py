"""
Question 6 - lambda With map() to Square a List
================================================
map(function, iterable) applies the FUNCTION to EVERY item and gives back
the transformed results.

    map(lambda n: n ** 2, [1, 2, 3])   ->   1, 4, 9

THE KEY IDEA: map() TRANSFORMS. Every input produces exactly one output,
so the result is ALWAYS THE SAME LENGTH as the input. (Compare with
filter() in Question 7, which SELECTS and usually returns fewer items.)

map() returns a lazy MAP OBJECT, not a list. Wrapping it in list() is what
actually makes it produce the values.
"""

numbers = [1, 2, 3, 4, 5, 6]

print("=" * 55)
print("SQUARING A LIST WITH map()")
print("=" * 55)
print("Original list :", numbers)
print()

# The map object on its own is lazy - it has computed nothing yet
squared_map = map(lambda n: n ** 2, numbers)
print("map(lambda n: n ** 2, numbers) ->", squared_map)
print("   A lazy map object. list() is what makes it produce values.")
print()

squared = list(squared_map)
print("list(...) ->", squared)
print()
print("Original   :", numbers)
print("Squared    :", squared)
print("Same length:", len(numbers), "==", len(squared), "->", len(numbers) == len(squared))
print("map() TRANSFORMS every item, so nothing is ever dropped.")
print()

# --- What map() does on each item ------------------------------------------
print("=" * 55)
print("WHAT map() DOES ON EACH ITEM")
print("=" * 55)
for n in numbers:
    print(f"   {n} -> lambda n: n ** 2 -> {n ** 2}")
print()

# --- The manual loop that map() replaces -----------------------------------
print("=" * 55)
print("THE LOOP map() REPLACES")
print("=" * 55)

manual = []
for n in numbers:
    manual.append(n ** 2)

print("Loop version  :", manual)
print("map() version :", squared)
print("Identical     :", manual == squared)
print("map() is the same work expressed in one line.")
print()

# --- A map object can only be consumed once --------------------------------
print("=" * 55)
print("A MAP OBJECT IS USED UP AFTER ONE PASS")
print("=" * 55)

once = map(lambda n: n ** 2, numbers)
print("First  list(once) ->", list(once))
print("Second list(once) ->", list(once), " <- empty, it was already consumed")
print("This is why the result is normally stored in a list straight away.")
print()

# --- Other transformations -------------------------------------------------
print("=" * 55)
print("OTHER USES OF map()")
print("=" * 55)

print("Cubes      :", list(map(lambda n: n ** 3, numbers)))
print("Doubled    :", list(map(lambda n: n * 2, numbers)))
print("As strings :", list(map(lambda n: str(n), numbers)))

words = ["python", "java", "go"]
print("Words      :", words)
print("Uppercased :", list(map(lambda w: w.upper(), words)))
print("Lengths    :", list(map(lambda w: len(w), words)))
print()


# map() accepts any function, not only a lambda
def square_it(n):
    """Return n squared."""
    return n ** 2


print("With a def instead of a lambda:", list(map(square_it, numbers)))
print("map() accepts ANY function - the lambda is just convenient here.")
