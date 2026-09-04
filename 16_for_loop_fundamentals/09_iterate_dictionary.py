"""
Question 9 - Print Every Key and Value of a Dictionary
=======================================================
Concept: the three ways to loop over a dictionary.

    for key in student:                      -> keys only (the default)
    for value in student.values():           -> values only
    for key, value in student.items():       -> BOTH at once

.items() is the one to use here, because we need every key AND its
value together. It hands back a (key, value) TUPLE on each pass,
which the two loop variables unpack automatically.

Sample output: name -> Rahul
               age -> 22
               course -> Data Science
               city -> Bangalore
"""

student = {
    "name": "Rahul",
    "age": 22,
    "course": "Data Science",
    "city": "Bangalore"
}

print("The dictionary :", student)
print("Number of pairs:", len(student))
print()

# --- The required output, using .items() -----------------------------------
print("=" * 45)
print("EVERY KEY AND VALUE  (using .items())")
print("=" * 45)

for key, value in student.items():
    print(f"   {key} -> {value}")

print()

# --- Neatly aligned, with the type of each value ---------------------------
print("=" * 45)
print("THE SAME DATA, WITH TYPES")
print("=" * 45)

for key, value in student.items():
    print(f"   {key:<10} : {str(value):<15} ({type(value).__name__})")

print()

# --- The other two ways of looping over a dictionary -----------------------
print("=" * 45)
print("THE OTHER TWO WAYS TO LOOP")
print("=" * 45)

print("A) Looping the dictionary directly gives KEYS ONLY:")
for key in student:
    print("     ", key)

print()
print("B) Looping .values() gives VALUES ONLY:")
for value in student.values():
    print("     ", value)

print()
print("C) Keys only, but fetching the value by hand:")
for key in student:
    print(f"      {key} -> {student[key]}")
print("   This works, but .items() is cleaner and does the lookup for you.")
print()

# --- What .items() actually produces ---------------------------------------
print("=" * 45)
print("WHAT .items() PRODUCES")
print("=" * 45)
print("list(student.items()) =")
for pair in student.items():
    print("   ", pair, "<- a", type(pair).__name__)
print()
print("The loop line  'for key, value in student.items()'  unpacks each")
print("tuple into two separate variables on every pass.")
