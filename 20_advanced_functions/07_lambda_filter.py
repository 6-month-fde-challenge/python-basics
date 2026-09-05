"""
Question 7 - lambda With filter() to Extract Even Numbers
==========================================================
filter(function, iterable) keeps only the items for which the function
returns True.

    filter(lambda n: n % 2 == 0, [1, 2, 3, 4])   ->   2, 4

THE KEY DIFFERENCE FROM map()
    map()    TRANSFORMS -> output length ALWAYS equals input length
    filter() SELECTS    -> output length is USUALLY SHORTER

The function handed to filter() must return True or False. Such a
function is called a PREDICATE - it answers a yes/no question about each
item. Like map(), filter() is lazy, so list() is needed to see the values.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("=" * 55)
print("EXTRACTING EVEN NUMBERS WITH filter()")
print("=" * 55)
print("Original list :", numbers)
print()

even_filter = filter(lambda n: n % 2 == 0, numbers)
print("filter(lambda n: n % 2 == 0, numbers) ->", even_filter)
print("   Lazy again - list() is what produces the values.")
print()

evens = list(even_filter)
print("list(...) ->", evens)
print()
print("Original :", numbers, "->", len(numbers), "items")
print("Evens    :", evens, "->", len(evens), "items")
print("filter() SELECTS, so items can be dropped.")
print()

# --- The yes/no decision on each item --------------------------------------
print("=" * 55)
print("THE TRUE/FALSE TEST ON EACH ITEM")
print("=" * 55)
for n in numbers:
    verdict = n % 2 == 0
    if verdict:
        print(f"   {n:>3}  ->  {n} % 2 == 0  is  True   -> KEPT")
    else:
        print(f"   {n:>3}  ->  {n} % 2 == 0  is  False  -> dropped")
print()

# --- map() and filter() side by side ---------------------------------------
print("=" * 55)
print("map() vs filter() ON THE SAME LIST")
print("=" * 55)

mapped = list(map(lambda n: n ** 2, numbers))
filtered = list(filter(lambda n: n % 2 == 0, numbers))

print("Input           :", numbers, "->", len(numbers), "items")
print("map(square)     :", mapped, "->", len(mapped), "items (same count)")
print("filter(is even) :", filtered, "->", len(filtered), "items (fewer)")
print()
print("map    changes the VALUES and keeps the COUNT.")
print("filter keeps the VALUES and changes the COUNT.")
print()

# --- The loop filter() replaces --------------------------------------------
print("=" * 55)
print("THE LOOP filter() REPLACES")
print("=" * 55)

manual = []
for n in numbers:
    if n % 2 == 0:
        manual.append(n)

print("Loop version   :", manual)
print("filter version :", evens)
print("Identical      :", manual == evens)
print()

# --- Other filters ---------------------------------------------------------
print("=" * 55)
print("OTHER USES OF filter()")
print("=" * 55)

print("Odd numbers    :", list(filter(lambda n: n % 2 != 0, numbers)))
print("Greater than 5 :", list(filter(lambda n: n > 5, numbers)))
print("Divisible by 3 :", list(filter(lambda n: n % 3 == 0, numbers)))

words = ["python", "go", "java", "c", "javascript"]
print("Words          :", words)
print("Longer than 3  :", list(filter(lambda w: len(w) > 3, words)))
print()

# --- Combining the two -----------------------------------------------------
print("=" * 55)
print("COMBINING filter() AND map()")
print("=" * 55)

combined = list(map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers)))
print("Square only the even numbers:", combined)
print()
print("Read it from the INSIDE OUT:")
print("   1. filter picks the evens      ->", list(filter(lambda n: n % 2 == 0, numbers)))
print("   2. map squares what survived   ->", combined)
