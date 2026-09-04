"""
Exercise 04 - Python Data Type Laboratory
=========================================
Part A : 16 variables covering all 8 core data types
Part B : type() on every single one of them
Part C : type conversion (type casting) with an explanation of each result

THE BIG IDEA: Python is DYNAMICALLY TYPED. You never declare the type -
Python decides it from the value you assign. type() shows what it decided.
"""

# ===========================================================================
# PART A - CREATE 16 VARIABLES (2 examples of each of the 8 data types)
# ===========================================================================

# --- int : whole numbers, positive or negative, no decimal point -----------
age = 25
temperature = -8

# --- float : numbers WITH a decimal point ----------------------------------
price = 199.99
pi_value = 3.14159

# --- str : text, written inside quotes --------------------------------------
name = "Veerandra"
course = "Python Programming"

# --- bool : only two possible values, True or False (capital first letter) --
is_student = True
has_certificate = False

# --- list : ORDERED, CHANGEABLE, allows duplicates -> square brackets [] ----
skills = ["python", "sql", "excel", "python"]
marks = [88, 92, 75, 64, 99]

# --- tuple : ORDERED, UNCHANGEABLE, allows duplicates -> parentheses () -----
coordinates = (12.97, 77.59)
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")

# --- set : UNORDERED, no duplicates allowed -> curly braces {} --------------
unique_numbers = {1, 2, 3, 3, 2, 1}       # duplicates are dropped automatically
programming_languages = {"python", "java", "c++"}

# --- dict : KEY-VALUE pairs -> curly braces with key: value -----------------
student_details = {"name": "Veerandra", "age": 25, "city": "Hyderabad"}
subject_marks = {"maths": 95, "science": 88, "english": 79}


# ===========================================================================
# PART B - USE type() ON EVERY VARIABLE
# ===========================================================================

print("=" * 60)
print("PART B : DATA TYPE OF EACH VARIABLE")
print("=" * 60)

print("age                   =", age, "->", type(age))
print("temperature           =", temperature, "->", type(temperature))
print("price                 =", price, "->", type(price))
print("pi_value              =", pi_value, "->", type(pi_value))
print("name                  =", name, "->", type(name))
print("course                =", course, "->", type(course))
print("is_student            =", is_student, "->", type(is_student))
print("has_certificate       =", has_certificate, "->", type(has_certificate))
print("skills                =", skills, "->", type(skills))
print("marks                 =", marks, "->", type(marks))
print("coordinates           =", coordinates, "->", type(coordinates))
print("weekdays              =", weekdays, "->", type(weekdays))
print("unique_numbers        =", unique_numbers, "->", type(unique_numbers))
print("programming_languages =", programming_languages, "->", type(programming_languages))
print("student_details       =", student_details, "->", type(student_details))
print("subject_marks         =", subject_marks, "->", type(subject_marks))

print()
print("Total variables created :", 16)


# ===========================================================================
# PART C - TYPE CONVERSION (TYPE CASTING)
# ===========================================================================

print()
print("=" * 60)
print("PART C : TYPE CONVERSION - WHAT HAPPENS EACH TIME")
print("=" * 60)

# --- 1. int("100") ---------------------------------------------------------
# The TEXT "100" is parsed and becomes the NUMBER 100.
# Before: you cannot do maths with it. After: you can.
a = int("100")
print("\n1. int(\"100\")")
print("   before :", "100", type("100"), "-> '100' + '100' would give '100100'")
print("   after  :", a, type(a), "-> 100 + 100 now gives", a + a)

# --- 2. float("45.67") -----------------------------------------------------
# The TEXT "45.67" becomes a real decimal number.
# int("45.67") would CRASH - int() cannot parse a decimal point in a string.
b = float("45.67")
print("\n2. float(\"45.67\")")
print("   before :", "45.67", type("45.67"))
print("   after  :", b, type(b), "-> can now be used in maths:", b * 2)

# --- 3. str(500) -----------------------------------------------------------
# The NUMBER 500 becomes the TEXT "500".
# It loses its maths ability but gains string abilities like joining.
c = str(500)
print("\n3. str(500)")
print("   before :", 500, type(500))
print("   after  :", c, type(c), "-> can now be joined to text:", "Rs." + c)

# --- 4. bool(1) ------------------------------------------------------------
# RULE: 0, 0.0, "", [], (), {} and None are FALSY -> become False.
#       EVERY other value is TRUTHY -> becomes True.
d = bool(1)
print("\n4. bool(1)")
print("   before :", 1, type(1))
print("   after  :", d, type(d), "-> any non-zero number is True")
print("   compare: bool(0) =", bool(0), "| bool(\"\") =", bool(""), "| bool(\"hi\") =", bool("hi"))

# --- 5. list((1, 2, 3)) ----------------------------------------------------
# An UNCHANGEABLE tuple becomes a CHANGEABLE list. Order and duplicates kept.
e = list((1, 2, 3))
print("\n5. list((1, 2, 3))")
print("   before :", (1, 2, 3), type((1, 2, 3)), "-> cannot be edited")
print("   after  :", e, type(e), "-> can be edited, e.g. append:")
e.append(4)
print("            after e.append(4) ->", e)

# --- 6. tuple([1, 2, 3]) ---------------------------------------------------
# A CHANGEABLE list becomes a LOCKED tuple. Used to protect data.
f = tuple([1, 2, 3])
print("\n6. tuple([1, 2, 3])")
print("   before :", [1, 2, 3], type([1, 2, 3]), "-> editable")
print("   after  :", f, type(f), "-> now frozen; f.append(4) would raise AttributeError")

# --- 7. set([1, 2, 2, 3]) --------------------------------------------------
# DUPLICATES ARE REMOVED and the ORDER IS NOT GUARANTEED.
# This is the conversion that actually LOSES data - the extra 2 is gone forever.
g = set([1, 2, 2, 3])
print("\n7. set([1, 2, 2, 3])")
print("   before :", [1, 2, 2, 3], type([1, 2, 2, 3]), "-> 4 items, duplicate 2 kept")
print("   after  :", g, type(g), "->", len(g), "items, duplicate 2 REMOVED")


# ===========================================================================
# BONUS - A CONVERSION THAT FAILS (why we must be careful)
# ===========================================================================

print()
print("=" * 60)
print("BONUS : NOT EVERY CONVERSION IS POSSIBLE")
print("=" * 60)

try:
    int("hello")
except ValueError as error:
    print("int(\"hello\") failed ->", error)
    print("Reason: 'hello' contains no digits, so Python cannot make a number from it.")
