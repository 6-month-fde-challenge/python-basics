"""
main.py - the learning platform demonstration
==============================================
The last exercise of the module, and the one that uses all of it: a package
(exercise 24), custom exceptions (23), and every piece of OOP from 26 to 31.

    python main.py

main.py is not part of the package. It sits next to it and imports it.
"""

from platform_app import (LearningPlatform, Mentor, MentorFullError,
                          PlatformError, Student, User)

LINE = "=" * 62


def title(number, text):
    print()
    print(LINE)
    print(f"  {number}. {text}")
    print(LINE)


# ---------------------------------------------------------------- 1

def demo_1_registering():
    title(1, "Registering users")

    print(f"    User.get_total_users()  -> {User.get_total_users()}")
    print("    Before that, a static method, with no user in existence:")
    for email in ["aarav@example.com", "not-an-email", "two@@example.com"]:
        print(f"      User.is_valid_email({email!r:<20}) -> "
              f"{User.is_valid_email(email)}")
    print()

    site = LearningPlatform("Nova Learn")

    students = [
        site.register_student("Aarav Sharma", "aarav@example.com", "Python Basics"),
        site.register_student("Diya Menon", "diya@example.com", "Data Science"),
        site.register_student("Kabir Rao", "kabir@example.com"),
        site.register_student("Meera Nair", "meera@example.com", "Web Development"),
        site.register_student("Rohan Iyer", "rohan@example.com", "Python Basics"),
    ]
    mentors = [
        site.register_mentor("V. Krishnan", "krishnan@example.com", "Python, Backend"),
        site.register_mentor("R. Banerjee", "banerjee@example.com", "Data, Analytics"),
    ]

    for user in list(students) + list(mentors):
        print(f"      {user!r}")

    print()
    print(f"    site.total_users()      -> {site.total_users()}")
    print(f"    User.get_total_users()  -> {User.get_total_users()}")
    print()
    print("    The ids were not passed in. _new_id() is a class method:")
    print("      cls._sequence += 1")
    print("      return f'{cls.ID_PREFIX}{cls._sequence:03d}'")
    print()
    print("    cls is Student for a student and Mentor for a mentor, so one")
    print("    method produces S001..S005 and M001..M002 from two counters:")
    print(f"      Student.ID_PREFIX / _sequence  -> "
          f"{Student.ID_PREFIX} / {Student._sequence}")
    print(f"      Mentor.ID_PREFIX  / _sequence  -> "
          f"{Mentor.ID_PREFIX} / {Mentor._sequence}")
    print(f"      User.ID_PREFIX    / _sequence  -> "
          f"{User.ID_PREFIX} / {User._sequence}   <- never used, never moved")
    return site


# ---------------------------------------------------------------- 2

def demo_2_courses_and_mentors(site):
    title(2, "Assigning a course, and assigning a mentor")

    kabir = site.find("S003")
    print(f"    {kabir.name} registered without a course: {kabir.course}")
    site.assign_course("S003", "Data Science")
    print(f"    site.assign_course('S003', 'Data Science')")
    print(f"    {kabir.name} is now on: {kabir.course}")

    print()
    pairs = [("S001", "M001"), ("S005", "M001"), ("S002", "M002"),
             ("S003", "M002"), ("S004", "M001")]
    for student_id, mentor_id in pairs:
        mentor = site.assign_mentor(student_id, mentor_id)
        student = site.find(student_id)
        print(f"      {student.name:<16} -> {mentor.name:<14}"
              f"({mentor.student_count()}/{mentor.MAX_STUDENTS})")

    print()
    print("    assign_student() sets both sides of the link in one place:")
    aarav = site.find("S001")
    print(f"      aarav.mentor.name          -> {aarav.mentor.name}")
    print(f"      krishnan.students[0].name  -> "
          f"{site.find('M001').students[0].name}")


# ---------------------------------------------------------------- 3

def demo_3_assignments(site):
    title(3, "Submitting assignments")

    work = [
        ("S001", ["Variables and types", "Loops and conditionals",
                  "Functions", "File handling", "Mini project"]),
        ("S002", ["Pandas basics", "Cleaning a dataset", "Plotting"]),
        ("S003", ["Pandas basics"]),
        ("S004", ["HTML and CSS", "JavaScript basics", "A first page",
                  "Forms and validation"]),
        ("S005", ["Variables and types", "Loops and conditionals"]),
    ]

    for student_id, titles in work:
        student = site.find(student_id)
        for one in titles:
            count = site.submit_assignment(student_id, one)
        print(f"      {student.name:<16}{count} submitted, "
              f"{student.progress():>5.0f}%   "
              f"{'COMPLETED' if student.has_finished() else 'in progress'}")

    print()
    print("    Each student has their own list, created in Student.__init__:")
    print(f"      aarav.completed_assignments is rohan.completed_assignments"
          f"  -> {site.find('S001').completed_assignments is site.find('S005').completed_assignments}")
    print()
    print("    Aarav and Rohan submitted two identically titled assignments and")
    print("    the lists are still separate objects - the aliasing trap from")
    print("    exercise 06, avoided by building the list inside __init__.")


# ---------------------------------------------------------------- 4

def demo_4_display(site):
    title(4, "Displaying a student and a mentor")

    site.display_user("S001")
    print()
    site.display_user("M001")
    print()
    print("    display_details() is defined in all three classes. Both children")
    print("    call super().display_details() first, so the four lines every")
    print("    user has are written once in User.")
    print()
    print("    And the parent's own method prints self.role(), which both")
    print("    children override - User never learns that mentors exist.")


# ---------------------------------------------------------------- 5

def demo_5_report(site):
    title(5, "The whole platform")

    site.report()

    print()
    print("    One dictionary, two kinds of object, one loop. report() asks")
    print("    isinstance() once, to choose which detail column to print.")

    print()
    for mentor in site.mentors():
        print(f"      {mentor.name:<14}{mentor.student_count()} students, "
              f"average progress {mentor.average_progress():>5.1f}%")

    # the accumulator and champion patterns from exercise 18, over objects
    total, best = 0, site.students()[0]
    for student in site.students():
        total += student.completed_count()
        if student.progress() > best.progress():
            best = student
    print()
    print(f"      {'assignments submitted':<28}{total}")
    print(f"      {'furthest along':<28}{best.name} ({best.progress():.0f}%)")


# ---------------------------------------------------------------- 6

def demo_6_refusals(site):
    title(6, "What the platform refuses")

    cases = [
        ("a duplicate email",
         lambda: site.register_student("Someone Else", "aarav@example.com")),
        ("a malformed email",
         lambda: site.register_student("Bad Email", "nope")),
        ("a blank name",
         lambda: site.register_student("   ", "blank@example.com")),
        ("an unknown id", lambda: site.find("S999")),
        ("a course for a mentor",
         lambda: site.assign_course("M001", "Python Basics")),
        ("an assignment before a course",
         lambda: site.register_student("No Course", "nc@example.com")
                 .submit_assignment("Anything")),
        ("the same assignment twice",
         lambda: site.submit_assignment("S001", "Functions")),
        ("a fourth student for a full mentor",
         lambda: site.assign_mentor("S002", "M001")),
    ]

    for label, call in cases:
        try:
            call()
        except PlatformError as error:
            print(f"      {label:<36}{type(error).__name__}")
            print(f"      {'':<36}  {error}")

    print()
    print("    Eight different failures, one except clause. Every class above")
    print("    inherits from PlatformError:")
    print()
    print("        PlatformError")
    print("         |-- ValidationError")
    print("         |-- DuplicateUserError")
    print("         |-- UnknownUserError")
    print("         +-- MentorFullError")

    print()
    print("    MentorFullError carries the mentor and the limit, not just a")
    print("    sentence, so a caller can act on it:")
    try:
        site.assign_mentor("S002", "M001")
    except MentorFullError as error:
        print(f"      error.mentor.name -> {error.mentor.name}")
        print(f"      error.limit       -> {error.limit}")


# ---------------------------------------------------------------- 7

def demo_7_class_members(site):
    title(7, "The class variable and the class method, once more")

    print(f"    User.platform_name    -> {User.platform_name}")
    print(f"    Student.platform_name -> {Student.platform_name}"
          f"   <- inherited, not copied")
    print(f"    Mentor.platform_name  -> {Mentor.platform_name}")
    print()
    User.set_platform_name("Nova Learn Academy")
    print("    User.set_platform_name('Nova Learn Academy')")
    for user in list(site.students())[:2] + list(site.mentors())[:1]:
        print(f"      {user.user_id}  {user.name:<16}{user.platform_name}")

    print()
    print(f"    User.total_users            -> {User.total_users}")
    print(f"    Student.total_users         -> {Student.total_users}")
    print(f"    User.get_total_users()      -> {User.get_total_users()}")
    print(f"    site.total_users()          -> {site.total_users()}")
    print()
    print("    The two numbers differ on purpose, and the gap is exact:")
    print("      7 registered in section 1")
    print("      +1 'No Course', registered in section 6 and never given a course")
    print("      +1 'Someone Else', built and then refused for a duplicate email")
    print("    User.total_users counts every User object __init__ ever finished.")
    print("    site.total_users() counts the ones the platform actually kept.")
    print("    A class variable and a dictionary answer two different questions.")


def main():
    print()
    print(LINE)
    print("  EXERCISE 32 - Learning Platform")
    print("  Inheritance, class and static methods, a package, and exceptions")
    print(LINE)

    site = demo_1_registering()
    demo_2_courses_and_mentors(site)
    demo_3_assignments(site)
    demo_4_display(site)
    demo_5_report(site)
    demo_6_refusals(site)
    demo_7_class_members(site)

    print()
    print(LINE)
    print("  Three classes in one hierarchy, one class that owns them, and")
    print("  five exception classes - in a package main.py only imports.")
    print(LINE)
    print()


if __name__ == "__main__":
    main()
