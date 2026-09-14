"""
main.py - the student management demonstration
===============================================
Builds five students from one class, prints them, updates marks, and asks the
class - not any student - how many students exist.

    python main.py

All of the logic lives in student.py. This file only creates objects, calls
methods and prints what came back.
"""

from student import Student

LINE = "=" * 62


def title(number, text):
    print()
    print(LINE)
    print(f"  {number}. {text}")
    print(LINE)


# ---------------------------------------------------------------- 1

def demo_1_building_objects():
    title(1, "One class, five objects")

    print(f"    Student.get_total_students()  -> {Student.get_total_students()}")
    print("    (the class exists, no student does)")
    print()

    students = [
        Student("Aarav Sharma", "aarav@example.com", "S101", "Python",
                {"Python": 88, "Maths": 92, "English": 76}),
        Student("Diya Menon", "diya@example.com", "S102", "Data Science",
                {"Python": 95, "Statistics": 89, "English": 81}),
        Student("Kabir Rao", "kabir@example.com", "S103", "Python",
                {"Python": 64, "Maths": 58, "English": 71}),
        Student("Meera Nair", "meera@example.com", "S104", "Web Development",
                {"HTML": 84, "CSS": 79, "JavaScript": 33}),
        Student("Rohan Iyer", "rohan@example.com", "S105", "Data Science"),
    ]

    print(f"    Student.get_total_students()  -> {Student.get_total_students()}")
    print()
    for student in students:
        print(f"      {student!r}")

    print()
    print("    Five objects. Each has its own name, email, id, course and")
    print("    marks; all five share Student.institute and the counter.")
    return students


# ---------------------------------------------------------------- 2

def demo_2_display(students):
    title(2, "display_details() - an instance method")

    for student in students:
        student.display_details()
        print()

    print("    Rohan has no marks yet, so his average is 0.00 and his")
    print("    result is FAIL rather than a crash on an empty dictionary.")


# ---------------------------------------------------------------- 3

def demo_3_updating(students):
    title(3, "update_marks() - changing one object")

    meera = students[3]
    rohan = students[4]

    print(f"    before: Meera JavaScript = {meera.marks['JavaScript']}"
          f"   average {meera.average_marks():.2f}  grade {meera.grade()}"
          f"  {'PASS' if meera.has_passed() else 'FAIL'}")

    previous = meera.update_marks("JavaScript", 68)      # re-sat the paper

    print(f"    meera.update_marks('JavaScript', 68)   (was {previous})")
    print(f"    after : Meera JavaScript = {meera.marks['JavaScript']}"
          f"   average {meera.average_marks():.2f}  grade {meera.grade()}"
          f"  {'PASS' if meera.has_passed() else 'FAIL'}")

    print()
    print("    A new subject for a student who had none:")
    rohan.update_marks("Python", 77)
    rohan.update_marks("Statistics", 69)
    print(f"    rohan.marks           -> {rohan.marks}")
    print(f"    rohan.average_marks() -> {rohan.average_marks()}")

    print()
    print("    Updating Meera changed Meera. Nobody else moved:")
    for student in students[:2]:
        print(f"      {student.name:<14} average {student.average_marks():>6.2f}")


# ---------------------------------------------------------------- 4

def demo_4_averages(students):
    title(4, "average_marks() across every object")

    print(f"    {'student':<14}{'course':<18}{'average':>9}{'grade':>7}{'result':>9}")
    print(f"    {'-' * 57}")
    for student in students:
        print(f"    {student.name:<14}{student.course:<18}"
              f"{student.average_marks():>9.2f}{student.grade():>7}"
              f"{'PASS' if student.has_passed() else 'FAIL':>9}")

    # the accumulator and champion patterns again, this time over objects
    total, best = 0, students[0]
    for student in students:
        total += student.average_marks()
        if student.average_marks() > best.average_marks():
            best = student

    print(f"    {'-' * 57}")
    print(f"    {'class average':<32}{total / len(students):>9.2f}")
    print(f"    {'top student':<32}{best.name:>9}")


# ---------------------------------------------------------------- 5

def demo_5_class_members(students):
    title(5, "The class variable and the class method")

    print(f"    Student.total_students        -> {Student.total_students}")
    print(f"    Student.get_total_students()  -> {Student.get_total_students()}")
    print()
    print("    Every student agrees, because there is only one counter:")
    for student in students[:3]:
        print(f"      {student.name:<14} sees {student.get_total_students()}")

    print()
    print(f"    Student.institute             -> {Student.institute}")
    Student.set_institute("Nova Institute of Engineering")
    print("    Student.set_institute('Nova Institute of Engineering')")
    print(f"    Student.institute             -> {Student.institute}")
    print()
    print("    One call, and every student's institute changed - none of")
    print("    the five objects was touched:")
    for student in students[:3]:
        print(f"      {student.name:<14} {student.institute}")


# ---------------------------------------------------------------- 6

def demo_6_validation():
    title(6, "Validation - what the class refuses")

    victim = Student("Temp Student", "temp@example.com", "S999", "Python")

    cases = [
        ("mark above 100", lambda: victim.update_marks("Python", 120)),
        ("negative mark", lambda: victim.update_marks("Python", -5)),
        ("mark is a string", lambda: victim.update_marks("Python", "eighty")),
        ("mark is True", lambda: victim.update_marks("Python", True)),
        ("empty subject", lambda: victim.update_marks("   ", 50)),
    ]

    for label, call in cases:
        try:
            call()
        except ValueError as error:
            print(f"    {label:<18} ValueError: {error}")

    print()
    print("    True is rejected on purpose. bool subclasses int in Python, so")
    print("    isinstance(True, int) is True and a score of True would become")
    print("    1 - a silently wrong mark instead of a loud error.")

    print()
    print("    is_valid_email() is a static method: it needs no student.")
    for email in ["aarav@example.com", "no-at-sign", "two@@example.com",
                  "nodot@example", "@example.com"]:
        print(f"      Student.is_valid_email({email!r:<22}) -> "
              f"{Student.is_valid_email(email)}")


def main():
    print()
    print(LINE)
    print("  EXERCISE 26 - Student Management System")
    print("  Classes, objects, __init__, instance methods, class members")
    print(LINE)

    students = demo_1_building_objects()
    demo_2_display(students)
    demo_3_updating(students)
    demo_4_averages(students)
    demo_5_class_members(students)
    demo_6_validation()

    print()
    print(LINE)
    print(f"  Student.get_total_students() -> {Student.get_total_students()}")
    print("  Six, not five: section 6 built one more student to break.")
    print("  The counter cannot be fooled - it lives in __init__.")
    print(LINE)
    print()


if __name__ == "__main__":
    main()
