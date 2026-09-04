"""
Exercise 09 - Tuple Challenge
=============================
Concepts practised: tuple creation, indexing, negative indexing, slicing,
                    count(), index(), len(), list() <-> tuple() conversion

WHAT IS A TUPLE?
A tuple is an ORDERED collection, written in ROUND brackets (),
that allows DUPLICATES but is IMMUTABLE - it can never be changed
after it is created.
"""

# ---------------------------------------------------------------------------
# Create the tuple
# ---------------------------------------------------------------------------

technologies = ("Python", "Java", "Python", "C++", "JavaScript", "Python")


# ---------------------------------------------------------------------------
# 1. Print the tuple
# ---------------------------------------------------------------------------
print("1.  The tuple           :", technologies)


# ---------------------------------------------------------------------------
# 2. Print its type
# ---------------------------------------------------------------------------
print("2.  Type                :", type(technologies))


# ---------------------------------------------------------------------------
# 3. First item -> index 0
# ---------------------------------------------------------------------------
print("3.  First item [0]      :", technologies[0])


# ---------------------------------------------------------------------------
# 4. Last item -> index -1
# ---------------------------------------------------------------------------
print("4.  Last item  [-1]     :", technologies[-1])


# ---------------------------------------------------------------------------
# 5. Slice the tuple - [start:stop], stop is EXCLUDED.
#    Slicing a tuple returns a NEW TUPLE (the original is not touched).
# ---------------------------------------------------------------------------
print("5.  Slicing:")
print("    [1:4]  (items 1,2,3):", technologies[1:4])
print("    [:3]   (first three):", technologies[:3])
print("    [3:]   (from 3 on)  :", technologies[3:])
print("    [-2:]  (last two)   :", technologies[-2:])
print("    [::-1] (reversed)   :", technologies[::-1])
print("    Type of a slice     :", type(technologies[1:4]), "<- still a tuple")


# ---------------------------------------------------------------------------
# 6. count("Python") - tuples allow duplicates, so this is 3
# ---------------------------------------------------------------------------
print("6.  Count of 'Python'   :", technologies.count("Python"))


# ---------------------------------------------------------------------------
# 7. index("C++") - position of the FIRST match
# ---------------------------------------------------------------------------
print("7.  Index of 'C++'      :", technologies.index("C++"))
print("    Index of 'Python'   :", technologies.index("Python"),
      "<- only the FIRST one, even though it appears 3 times")


# ---------------------------------------------------------------------------
# 8. Length of the tuple
# ---------------------------------------------------------------------------
print("8.  Length              :", len(technologies))


# ===========================================================================
# 9-11. THE WORKAROUND: tuple -> list -> edit -> tuple
# ===========================================================================

print()
print("=" * 62)
print("ADDING TO A TUPLE (the convert-edit-convert trick)")
print("=" * 62)

# --- 9. Convert the tuple into a list --------------------------------------
tech_list = list(technologies)
print("9.  Converted to a list :", tech_list)
print("    Type                :", type(tech_list), "<- now editable")

# --- 10. Add "Go" (only possible because it is a list now) -----------------
tech_list.append("Go")
print("10. After append('Go')  :", tech_list)
print("    Length              :", len(tech_list))

# --- 11. Convert it back into a tuple --------------------------------------
updated_technologies = tuple(tech_list)
print("11. Back to a tuple     :", updated_technologies)
print("    Type                :", type(updated_technologies), "<- locked again")

print()
print("    ORIGINAL tuple is still :", technologies)
print("    We did NOT change the original - we BUILT A NEW tuple from it.")


# ===========================================================================
# WHY TUPLES ARE CALLED IMMUTABLE
# ===========================================================================

print()
print("=" * 62)
print("WHY TUPLES ARE 'IMMUTABLE'")
print("=" * 62)

# --- Proof 1 : you cannot change an existing item ---------------------------
try:
    technologies[1] = "Ruby"
except TypeError as error:
    print("1. technologies[1] = 'Ruby' -> TypeError:", error)
    print("   A list would allow this. A tuple refuses it.")

# --- Proof 2 : there are no methods that add or delete ----------------------
tuple_methods = [m for m in dir(tuple) if not m.startswith("_")]
list_methods = [m for m in dir(list) if not m.startswith("_")]
print()
print("2. A tuple has only", len(tuple_methods), "methods:", tuple_methods)
print("   A list has", len(list_methods), "methods:", list_methods)
print("   append, insert, remove, pop, sort and clear simply DO NOT EXIST")
print("   on a tuple - there is no way to change it, by design.")

# --- Proof 3 : re-assigning the VARIABLE is not changing the TUPLE ----------
print()
print("3. A common confusion:")
sample = ("A", "B")
print("   sample = ('A','B') ->", sample)
sample = ("A", "B", "C")
print("   sample = ('A','B','C') ->", sample)
print("   This looks like a change, but it is NOT. The first tuple was never")
print("   edited - the NAME 'sample' was simply pointed at a brand new tuple.")

# --- The practical reason tuples exist --------------------------------------
print()
print("SO WHY USE A TUPLE AT ALL?")
print("   a) SAFETY   : fixed data such as (latitude, longitude) or weekdays")
print("                 cannot be changed by accident anywhere in the program.")
print("   b) SPEED    : tuples are lighter and faster than lists.")
print("   c) DICT KEYS: tuples can be dictionary keys or set members, lists cannot:")
location_scores = {(12.97, 77.59): "Bengaluru", (17.38, 78.48): "Hyderabad"}
print("                ", location_scores)
print("                 A list as a key would raise 'unhashable type: list'.")

# --- The single-item tuple trap ---------------------------------------------
print()
print("BONUS TRAP - a one-item tuple NEEDS a trailing comma:")
not_a_tuple = ("Python")
real_tuple = ("Python",)
print("   ('Python')  ->", type(not_a_tuple), "<- just a string in brackets!")
print("   ('Python',) ->", type(real_tuple), "<- the comma makes it a tuple")
