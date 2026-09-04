"""
Exercise 08 - Set Operations Challenge
======================================
Concepts practised: union(), intersection(), difference(),
                    symmetric_difference(), add(), remove(), discard()

TWO GROUPS OF METHODS - this is the whole lesson:
  * COMPARING sets  -> union / intersection / difference / symmetric_difference
                       These RETURN A NEW SET. The originals are untouched.
  * CHANGING a set  -> add / remove / discard
                       These MODIFY THE SET IN PLACE and return None.

NOTE ON OUTPUT ORDER: sets are UNORDERED, so the order of names can differ
each time you run the file. sorted() is used for a stable, readable display.
"""

# ---------------------------------------------------------------------------
# Create the two sets
# ---------------------------------------------------------------------------

python_students = {"Rahul", "Aman", "Priya", "Karan", "Neha"}
java_students = {"Priya", "Karan", "Rohit", "Simran"}


# ---------------------------------------------------------------------------
# 1. Print both sets
# ---------------------------------------------------------------------------
print("1. Python students :", sorted(python_students), "| count:", len(python_students))
print("   Java students   :", sorted(java_students), "| count:", len(java_students))
print()


# ===========================================================================
# PART A - COMPARING THE TWO SETS (these do NOT change the originals)
# ===========================================================================

print("=" * 62)
print("PART A : COMPARING SETS")
print("=" * 62)

# --- 2. union() : EITHER Python OR Java (everyone, no duplicates) ----------
either_course = python_students.union(java_students)
print("2. union()  - learning EITHER course :")
print("   ", sorted(either_course), "| count:", len(either_course))
print("    Priya and Karan are in both lists but appear only ONCE.")
print("    Same thing with the | operator     :", sorted(python_students | java_students))
print()

# --- 3. intersection() : BOTH Python AND Java (the overlap) ----------------
both_courses = python_students.intersection(java_students)
print("3. intersection() - learning BOTH courses :")
print("   ", sorted(both_courses), "| count:", len(both_courses))
print("    Same thing with the & operator     :", sorted(python_students & java_students))
print()

# --- 4. difference() : ONLY Python (in the first set, not the second) ------
only_python = python_students.difference(java_students)
print("4. difference() - learning ONLY Python :")
print("   ", sorted(only_python), "| count:", len(only_python))
print("    Same thing with the - operator     :", sorted(python_students - java_students))
print()

# --- 5. difference() the other way round : ONLY Java -----------------------
#     ORDER MATTERS. A.difference(B) is NOT the same as B.difference(A).
only_java = java_students.difference(python_students)
print("5. difference() reversed - learning ONLY Java :")
print("   ", sorted(only_java), "| count:", len(only_java))
print("    Notice: python-java gives", sorted(only_python))
print("            java-python gives", sorted(only_java), "-> ORDER MATTERS")
print()

# --- 6. symmetric_difference() : in EXACTLY ONE group ----------------------
exactly_one = python_students.symmetric_difference(java_students)
print("6. symmetric_difference() - in EXACTLY ONE group :")
print("   ", sorted(exactly_one), "| count:", len(exactly_one))
print("    This is the union MINUS the intersection - everyone except the overlap.")
print("    Proof:", len(either_course), "(union) -", len(both_courses), "(both) =",
      len(either_course) - len(both_courses), "= ", len(exactly_one))
print("    Same thing with the ^ operator     :", sorted(python_students ^ java_students))
print()

# Confirm nothing above changed the original sets
print("Originals are unchanged :", sorted(python_students), "and", sorted(java_students))


# ===========================================================================
# PART B - CHANGING A SET (these DO modify it in place)
# ===========================================================================

print()
print("=" * 62)
print("PART B : CHANGING A SET")
print("=" * 62)

# --- 7. add() : insert ONE new element -------------------------------------
print("7. add('Sneha')")
print("   before :", sorted(python_students))
python_students.add("Sneha")
print("   after  :", sorted(python_students), "| count:", len(python_students))
# Adding something that already exists does nothing at all - no error, no change
python_students.add("Rahul")
print("   add('Rahul') again ->", sorted(python_students))
print("   Rahul was already there, so nothing changed (sets never duplicate).")
print()

# --- 8. remove() : delete an element, ERROR if it does not exist -----------
print("8. remove('Aman')")
print("   before :", sorted(python_students))
python_students.remove("Aman")
print("   after  :", sorted(python_students), "| count:", len(python_students))
print()

# --- 9. discard() : delete an element, SILENT if it does not exist ---------
print("9. discard() - the safe version of remove()")
print("   before :", sorted(python_students))
python_students.discard("Neha")          # Neha exists -> she is removed
print("   discard('Neha')  ->", sorted(python_students), "(Neha existed, so she was removed)")
python_students.discard("Vikram")        # Vikram does NOT exist -> nothing happens
print("   discard('Vikram')->", sorted(python_students), "(Vikram was never there - NO ERROR)")
print()


# ===========================================================================
# THE KEY DIFFERENCE : remove() vs discard()
# ===========================================================================

print("=" * 62)
print("remove() vs discard() ON A MISSING NAME")
print("=" * 62)

try:
    python_students.remove("Vikram")
except KeyError as error:
    print("remove('Vikram')  -> CRASHED with KeyError:", error)

python_students.discard("Vikram")
print("discard('Vikram') -> ran quietly, no error, set unchanged:", sorted(python_students))
print()
print("Use remove()  when the item MUST be there and a mistake should be reported.")
print("Use discard() when you just want it gone and do not care if it was missing.")

print()
print("Final Python set :", sorted(python_students))
print("Final Java set   :", sorted(java_students))
