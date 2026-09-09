"""
result_calc.py - total, percentage, grade, pass/fail
====================================================
The arithmetic, and nothing else. No input, no printing, no logging
decisions about whether to skip a student - this module is handed a
record that student_ops has already validated and returns numbers.

That is what makes it testable: `python result_calc.py` runs a self-test
of the maths on its own, with no CSV and no menu in the way.

THE RULES
    total       the five marks added up                      (0 - 500)
    percentage  total / (5 * 100) * 100                      (0 - 100)
    grade       A+ >=90, A >=80, B >=70, C >=60, D >=50,
                E >=40, F below 40
    pass/fail   percentage >= 40  AND  every subject >= 33

THE SECOND PASS CONDITION IS THE INTERESTING ONE
    95, 90, 88, 30, 85 averages 77.6% - a clear pass by percentage - but
    30 in English is below the subject minimum. Averaging hides a failed
    subject, so the per-subject check runs separately.

WHY THE DIVISION IS GUARDED
    percentage divides by len(marks) * 100. An empty marks dictionary
    makes that zero, and Python raises ZeroDivisionError. Rather than
    letting a bare ZeroDivisionError escape, it is caught and re-raised
    as ResultCalculationError, which carries the roll number - so the log
    line names the student instead of just the operation.
"""
from exceptions import ResultCalculationError
from logger_config import get_logger

log = get_logger("result_calc")

MAX_PER_SUBJECT = 100
PASS_PERCENTAGE = 40.0
PASS_PER_SUBJECT = 33.0

# Ordered high to low, so the first match wins and no upper bounds are
# needed. A list of pairs beats an if/elif chain: adding a band is one
# new tuple.
GRADE_BANDS = [
    (90.0, "A+"),
    (80.0, "A"),
    (70.0, "B"),
    (60.0, "C"),
    (50.0, "D"),
    (40.0, "E"),
]
FAIL_GRADE = "F"


def calculate_total(marks):
    """Return the sum of the marks. An empty dictionary totals 0."""
    total = 0.0
    for value in marks.values():
        total += value          # accumulator, the pattern from exercise 18
    return total


def calculate_percentage(total, subject_count, roll=None):
    """
    Return total as a percentage of the maximum obtainable.

    The try/except is not decoration. `subject_count` reaching this
    function as 0 is exactly the "division/calculation error" the
    assignment asks to be handled, and the wrap turns an anonymous
    ZeroDivisionError into an error that names a student.
    """
    try:
        maximum = subject_count * MAX_PER_SUBJECT
        percentage = (total / maximum) * 100

    except ZeroDivisionError:
        log.error("Percentage impossible for roll %s: no subjects to divide by",
                  roll)
        raise ResultCalculationError(
            "Cannot calculate a percentage from 0 subjects", roll) from None

    except TypeError:
        # A mark that slipped through as a string would land here.
        log.error("Percentage impossible for roll %s: non-numeric total %r",
                  roll, total)
        raise ResultCalculationError(
            f"Total {total!r} is not a number", roll) from None

    return round(percentage, 2)


def calculate_grade(percentage):
    """Return the grade letter for a percentage."""
    for threshold, letter in GRADE_BANDS:
        if percentage >= threshold:
            return letter
    return FAIL_GRADE


def failed_subjects(marks):
    """Return the subjects scored below the per-subject minimum."""
    return [subject for subject, value in marks.items()
            if value < PASS_PER_SUBJECT]


def decide_status(percentage, marks):
    """
    Return ("PASS"|"FAIL", reason).

    Two independent conditions, reported separately, so a result sheet
    can say WHY somebody failed rather than only that they did.
    """
    below = failed_subjects(marks)

    if percentage < PASS_PERCENTAGE and below:
        return "FAIL", (f"{percentage}% is below {PASS_PERCENTAGE}%, and "
                        f"{', '.join(below)} below {PASS_PER_SUBJECT:.0f}")
    if percentage < PASS_PERCENTAGE:
        return "FAIL", f"{percentage}% is below {PASS_PERCENTAGE}%"
    if below:
        return "FAIL", (f"{', '.join(below)} below the subject minimum of "
                        f"{PASS_PER_SUBJECT:.0f}")
    return "PASS", "all subjects cleared"


def process(student):
    """
    Turn a validated student record into a complete result.

    Returns the student dictionary with total, percentage, grade, status
    and reason added. Raises ResultCalculationError if the arithmetic
    cannot be completed.
    """
    marks = student["marks"]
    roll = student.get("roll")

    total = calculate_total(marks)
    percentage = calculate_percentage(total, len(marks), roll)
    grade = calculate_grade(percentage)
    status, reason = decide_status(percentage, marks)

    result = dict(student)
    result.update(total=total, percentage=percentage, grade=grade,
                  status=status, reason=reason,
                  maximum=len(marks) * MAX_PER_SUBJECT)

    log.info("Processed %s (%s): %.0f/%d = %.2f%% -> %s -> %s",
             student["name"], roll, total, result["maximum"], percentage,
             grade, status)
    return result


# Running this file directly tests the maths alone - no CSV, no menu.
# `__name__` is "result_calc" when main.py imports it, so this is skipped.
if __name__ == "__main__":
    from logger_config import setup_logging

    setup_logging()

    print("result_calc.py self-test")
    print("=" * 52)

    cases = [
        ("Clear pass", {"Maths": 88, "Physics": 92, "Chemistry": 76,
                        "English": 65, "Computer": 95}),
        ("Clear fail", {"Maths": 35, "Physics": 28, "Chemistry": 41,
                        "English": 30, "Computer": 39}),
        ("High average, one subject failed",
         {"Maths": 95, "Physics": 90, "Chemistry": 88, "English": 30,
          "Computer": 85}),
        ("Perfect", {"Maths": 100, "Physics": 100, "Chemistry": 100,
                     "English": 100, "Computer": 100}),
        ("Exactly on the pass line",
         {"Maths": 40, "Physics": 40, "Chemistry": 40, "English": 40,
          "Computer": 40}),
    ]

    for label, marks in cases:
        outcome = process({"roll": "T", "name": label, "marks": marks})
        print(f"{label:<34} {outcome['total']:5.0f}  "
              f"{outcome['percentage']:6.2f}%  {outcome['grade']:<2}  "
              f"{outcome['status']}")
        print(f"{'':<34} {outcome['reason']}")

    # The division guard, triggered on purpose.
    print("-" * 52)
    try:
        calculate_percentage(0, 0, roll="EMPTY")
    except ResultCalculationError as error:
        print(f"division guard   -> {type(error).__name__}: {error}")
