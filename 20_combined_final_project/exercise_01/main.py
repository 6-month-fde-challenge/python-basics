"""
Exercise 01 - Student Result Management System
==============================================
Accepts marks for a student across several subjects, then calculates the
total, percentage, grade and pass/fail status, and displays a result card.

FUNCTIONS
    accept_marks()        - collect validated marks for each subject
    calculate_total()     - add all marks without using sum()
    calculate_percentage()- total as a percentage of the maximum
    assign_grade()        - map a percentage to a letter grade
    determine_pass_fail() - a student fails if ANY subject is below the pass mark
    display_result()      - print the formatted result card

LOOPS USED
    for   - over a known list of subjects (the count is fixed)
    while - to re-ask for a mark until valid input is given (count unknown)

SAMPLE INPUT / OUTPUT
    Student name: Rahul
    Mathematics : 88
    Physics     : 92
    Chemistry   : 76
    English     : 65
    Computer Sci: 95

    Total       : 416 / 500
    Percentage  : 83.20%
    Grade       : A
    Result      : PASS
"""

SUBJECTS = ["Mathematics", "Physics", "Chemistry", "English", "Computer Science"]
MAX_MARKS_PER_SUBJECT = 100
PASS_MARK = 35


def accept_marks(subjects):
    """
    Ask the user for a mark in each subject and return them as a dictionary.

    Keeps re-asking for any subject until a valid mark (0-100) is entered.
    """
    marks = {}

    for subject in subjects:
        # while: the number of retries depends on how often the user mistypes
        valid = False
        while not valid:
            entry = input(f"   {subject:<18}: ")
            try:
                mark = int(entry)
            except ValueError:
                print(f"      '{entry}' is not a whole number. Please try again.")
                continue

            if mark < 0 or mark > MAX_MARKS_PER_SUBJECT:
                print(f"      Marks must be between 0 and {MAX_MARKS_PER_SUBJECT}.")
                continue

            marks[subject] = mark
            valid = True

    return marks


def calculate_total(marks):
    """Return the total of all marks, without using sum()."""
    total = 0
    for mark in marks.values():
        total += mark
    return total


def calculate_percentage(total, subject_count):
    """Return the percentage scored out of the maximum possible marks."""
    maximum = subject_count * MAX_MARKS_PER_SUBJECT
    if maximum == 0:
        return 0.0
    return (total / maximum) * 100


def assign_grade(percentage):
    """Return the letter grade for a percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 35:
        return "E"
    return "F"


def determine_pass_fail(marks):
    """
    Return 'PASS' or 'FAIL'.

    A student fails if ANY single subject is below the pass mark, even when
    the overall percentage is high.
    """
    for mark in marks.values():
        if mark < PASS_MARK:
            return "FAIL"
    return "PASS"


def failed_subjects(marks):
    """Return a list of subjects scored below the pass mark."""
    failed = []
    for subject, mark in marks.items():
        if mark < PASS_MARK:
            failed.append(subject)
    return failed


def display_result(name, marks):
    """Print a formatted result card for one student."""
    total = calculate_total(marks)
    subject_count = len(marks)
    percentage = calculate_percentage(total, subject_count)
    grade = assign_grade(percentage)
    result = determine_pass_fail(marks)

    print()
    print("=" * 46)
    print("            STUDENT RESULT CARD")
    print("=" * 46)
    print(f"   Name : {name}")
    print("   " + "-" * 40)
    print(f"   {'SUBJECT':<20}{'MARKS':>8}{'STATUS':>10}")
    print("   " + "-" * 40)

    for subject, mark in marks.items():
        status = "Pass" if mark >= PASS_MARK else "Fail"
        print(f"   {subject:<20}{mark:>8}{status:>10}")

    print("   " + "-" * 40)
    print(f"   {'TOTAL':<20}{total:>8} / {subject_count * MAX_MARKS_PER_SUBJECT}")
    print(f"   {'PERCENTAGE':<20}{percentage:>7.2f}%")
    print(f"   {'GRADE':<20}{grade:>8}")
    print(f"   {'RESULT':<20}{result:>8}")

    if result == "FAIL":
        print()
        print("   Failed in:", ", ".join(failed_subjects(marks)))

    print("=" * 46)


def main():
    """Run the student result management system."""
    print("=" * 46)
    print("      STUDENT RESULT MANAGEMENT SYSTEM")
    print("=" * 46)
    print(f"   Subjects: {len(SUBJECTS)}   Max per subject: {MAX_MARKS_PER_SUBJECT}"
          f"   Pass mark: {PASS_MARK}")
    print()

    name = input("   Student name : ").strip()
    if name == "":
        name = "Unnamed Student"

    print()
    print("   Enter the marks:")
    marks = accept_marks(SUBJECTS)

    display_result(name, marks)


if __name__ == "__main__":
    main()
