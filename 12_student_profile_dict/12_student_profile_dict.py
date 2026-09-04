"""
Exercise 12 - Student Profile Using Dictionary
==============================================
Concepts practised: keys(), values(), items(), get(), update(), pop(), copy()

THE 7 METHODS SPLIT INTO 3 JOBS:
  LOOK AT the whole dictionary -> keys(), values(), items()
  READ one value safely        -> get()
  CHANGE the dictionary        -> update(), pop()
  DUPLICATE the dictionary     -> copy()
"""

# ---------------------------------------------------------------------------
# Create the student dictionary
# ---------------------------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 22,
    "course": "Python",
    "city": "Bangalore",
    "marks": 88
}


# ---------------------------------------------------------------------------
# 1. Print the complete dictionary
# ---------------------------------------------------------------------------
print("1. Complete dictionary :")
print("  ", student)
print("   Number of details   :", len(student))
print()


# ---------------------------------------------------------------------------
# 2, 3. Print individual values using their key
# ---------------------------------------------------------------------------
print("2. Name                :", student["name"])
print("3. Course              :", student["course"])
print()


# ===========================================================================
# THE THREE VIEW METHODS - keys(), values(), items()
# ===========================================================================

print("=" * 62)
print("keys() / values() / items()")
print("=" * 62)

# --- 4. keys() - the NAMES of the details ----------------------------------
print("4. All keys   :", student.keys())
print("   As a list  :", list(student.keys()))

# --- 5. values() - the ACTUAL data -----------------------------------------
print("5. All values :", student.values())
print("   As a list  :", list(student.values()))

# --- 6. items() - key and value TOGETHER, as (key, value) tuples -----------
print("6. All items  :", student.items())
print("   As a list  :", list(student.items()))
print("   One item   :", list(student.items())[0], "->", type(list(student.items())[0]))
print()


# ===========================================================================
# CHANGING THE DICTIONARY
# ===========================================================================

print("=" * 62)
print("UPDATING AND ADDING")
print("=" * 62)

# --- 7. Change marks from 88 to 92 -----------------------------------------
print("7. Marks before :", student["marks"])
student["marks"] = 92
print("   Marks after  :", student["marks"])

# --- 8. Add an email address (new key -> created) --------------------------
student["email"] = "rahul@example.com"
print("8. Email added  :", student["email"])

# --- 9. Add a phone number (new key -> created) ----------------------------
student["phone"] = "9876543210"
print("9. Phone added  :", student["phone"])
print()
print("   Dictionary now :", student)
print()

# --- update() - change and/or add SEVERAL keys in ONE call ------------------
print("update() - the multi-key shortcut:")
print("   before :", student)
student.update({"marks": 95, "city": "Hyderabad", "grade": "A"})
print("   after  :", student)
print("   In ONE call it UPDATED marks (92 -> 95) and city (Bangalore -> Hyderabad)")
print("   because those keys existed, and CREATED grade because it did not.")
print("   Same rule as [] = , but applied to several keys at once.")
print()


# ===========================================================================
# REMOVING A KEY
# ===========================================================================

print("=" * 62)
print("REMOVING WITH pop()")
print("=" * 62)

# --- 10. Remove "city" - pop() deletes the key AND returns its value -------
print("10. Keys before  :", list(student.keys()))
removed_city = student.pop("city")
print("    pop('city') returned :", removed_city)
print("    Keys after   :", list(student.keys()))
print("    'city' in student ->", "city" in student)
print()
print("    pop() on a MISSING key crashes unless you give a default:")
print("      student.pop('address', 'not found') ->",
      student.pop("address", "not found"))
print()


# ===========================================================================
# SAFE READING WITH get()
# ===========================================================================

print("=" * 62)
print("get() - reading without the risk of a crash")
print("=" * 62)

# --- 11. Use get() to retrieve the name ------------------------------------
print("11. student.get('name')          :", student.get("name"))
print("    student['name']              :", student["name"], "(same answer)")
print()
print("    The difference only appears when the key is MISSING:")

try:
    print(student["city"])
except KeyError as error:
    print("    student['city']              -> KeyError:", error, "(crashes)")

print("    student.get('city')          :", student.get("city"), "(None, no crash)")
print("    student.get('city','Unknown'):", student.get("city", "Unknown"), "(with a default)")
print()


# ===========================================================================
# COPYING THE DICTIONARY
# ===========================================================================

print("=" * 62)
print("copy() - making an INDEPENDENT duplicate")
print("=" * 62)

# --- 12. Create a copy -----------------------------------------------------
student_copy = student.copy()
print("12. Original :", student)
print("    Copy     :", student_copy)
print("    Same object in memory? ", student is student_copy, "<- False = independent")
print()

# Prove the copy is independent
student_copy["name"] = "Priya"
student_copy["marks"] = 78
print("    After editing ONLY the copy:")
print("      copy     :", student_copy)
print("      original :", student, "<- untouched")
print()

# The dangerous alternative
print("    WITHOUT copy() it behaves completely differently:")
alias = student                 # this is NOT a copy - just a second name
alias["name"] = "CHANGED"
print("      alias = student  then  alias['name'] = 'CHANGED'")
print("      alias    :", alias["name"])
print("      original :", student["name"], "<- the ORIGINAL changed too!")
print("      Both names point at the SAME dictionary. copy() avoids this.")
student["name"] = "Rahul"       # restore

# The one limitation of copy()
print()
print("    NOTE - copy() is a SHALLOW copy. Top level values are independent,")
print("    but a dictionary nested INSIDE would still be shared by both.")
print("    For those, use  import copy  and  copy.deepcopy(student).")
