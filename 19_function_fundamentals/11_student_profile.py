"""
Question 11 - A Formatted Student Profile
==========================================
The function takes three parameters and RETURNS a formatted string. It is
then called using POSITIONAL and KEYWORD arguments.

POSITIONAL ARGUMENTS are matched BY POSITION:
    student_profile("Rahul", 22, "Python")
    The 1st value fills name, the 2nd fills age, the 3rd fills course.
    Their ORDER IS FIXED - swap two and the data lands in the wrong slot.

KEYWORD ARGUMENTS are matched BY NAME:
    student_profile(name="Rahul", age=22, course="Python")
    Their ORDER DOES NOT MATTER, because each value states its target.

MIXING THEM IS ALLOWED, but every positional argument must come FIRST:
    student_profile("Rahul", course="Python", age=22)   -> valid
    student_profile(name="Rahul", 22, "Python")         -> SyntaxError
Once a keyword argument appears, Python can no longer count positions.
"""


def student_profile(name, age, course):
    """Return a formatted student profile as a single string."""
    line = "   +" + "-" * 38 + "+"
    title = "   |" + "STUDENT PROFILE".center(38) + "|"

    profile = "\n"
    profile += line + "\n"
    profile += title + "\n"
    profile += line + "\n"
    profile += "   | Name   : " + str(name).ljust(27) + " |\n"
    profile += "   | Age    : " + str(age).ljust(27) + " |\n"
    profile += "   | Course : " + str(course).ljust(27) + " |\n"
    profile += line
    return profile


def profile_summary(name, age, course):
    """Return a one-line summary of a student."""
    return str(name) + " (" + str(age) + ") is studying " + str(course) + "."


print("=" * 55)
print("1. ALL POSITIONAL ARGUMENTS")
print("=" * 55)
print("   student_profile('Rahul', 22, 'Python')")
print(student_profile("Rahul", 22, "Python"))
print()

print("=" * 55)
print("2. ALL KEYWORD ARGUMENTS")
print("=" * 55)
print("   student_profile(name='Priya', age=24, course='Data Science')")
print(student_profile(name="Priya", age=24, course="Data Science"))
print()

print("=" * 55)
print("3. KEYWORD ARGUMENTS IN A DIFFERENT ORDER")
print("=" * 55)
print("   student_profile(course='Machine Learning', name='Aman', age=21)")
print(student_profile(course="Machine Learning", name="Aman", age=21))
print("   The order was scrambled, but every value still landed correctly,")
print("   because keywords are matched by NAME and not by position.")
print()

print("=" * 55)
print("4. MIXING POSITIONAL AND KEYWORD ARGUMENTS")
print("=" * 55)
print("   student_profile('Sneha', course='Web Development', age=23)")
print(student_profile("Sneha", course="Web Development", age=23))
print("   'Sneha' was positional and filled the first parameter.")
print("   The other two were keywords, so their order did not matter.")
print()

print("=" * 55)
print("WHY POSITIONAL ORDER MATTERS")
print("=" * 55)
print("   Correct : student_profile('Rahul', 22, 'Python')")
print("      ->", profile_summary("Rahul", 22, "Python"))
print()
print("   Swapped : student_profile(22, 'Rahul', 'Python')")
print("      ->", profile_summary(22, "Rahul", "Python"))
print()
print("   No error is raised. Python simply filled the slots in order, and")
print("   the nonsense output is the only clue that anything went wrong.")
print("   Keyword arguments make that mistake impossible.")
print()

print("=" * 55)
print("A MISSING ARGUMENT IS AN ERROR")
print("=" * 55)

try:
    student_profile("Rahul", 22)
except TypeError as error:
    print("   student_profile('Rahul', 22) -> TypeError:", error)
    print("   All three parameters are required - none has a default value.")
print()

print("=" * 55)
print("SEVERAL STUDENTS")
print("=" * 55)

students = [
    ("Rahul", 22, "Python"),
    ("Priya", 24, "Data Science"),
    ("Aman", 21, "Machine Learning"),
]

for name, age, course in students:
    print("   " + profile_summary(name, age, course))
