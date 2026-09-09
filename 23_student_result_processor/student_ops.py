"""
student_ops.py - getting student records IN and validating them
===============================================================
Everything about a student BEFORE any arithmetic happens: reading the
CSV and checking that what arrived is usable.

THE DIVIDING LINE BETWEEN THIS MODULE AND result_calc.py
    student_ops.py    is this record trustworthy?
    result_calc.py    given a trustworthy record, what is the result?

Keeping them apart means the calculator never has to ask "what if marks
is a string?" - by the time a record reaches it, that cannot be true.

VALIDATION RAISES, IT DOES NOT PRINT
    Every check here raises one of the classes from exceptions.py. It
    does not print, and it does not decide whether to skip the student -
    that decision belongs to main.py, which is the only place that knows
    there are more students waiting.
"""
import csv
import os

from exceptions import (
    InvalidMarksError,
    MarksOutOfRangeError,
    MissingStudentInfoError,
    SubjectCountError,
)
from logger_config import get_logger

log = get_logger("student_ops")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "students.csv")

SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer"]
SUBJECT_COUNT = len(SUBJECTS)

MIN_MARK = 0
MAX_MARK = 100


def validate_text(value, field, roll=None):
    """
    Return a cleaned required text field, or raise.

    `None`, "" and "   " are all treated as missing - a name of three
    spaces is not a name.

    Surrounding whitespace is stripped rather than refused - a padded
    name is still a name.
    """
    cleaned = (value or "").strip()

    if not cleaned:
        raise MissingStudentInfoError(field, roll)

    return cleaned


def validate_mark(value, subject, roll=None):
    """
    Turn one raw mark into a float, or raise.

    Two failures, two exception types:
        "abc"  -> InvalidMarksError      (cannot be a number)
        105    -> MarksOutOfRangeError   (is a number, wrong one)

    The second is a subclass of the first, so a caller that only cares
    "were the marks usable?" catches InvalidMarksError and gets both.
    """
    raw = (value or "").strip() if isinstance(value, str) else value

    if raw == "" or raw is None:
        raise InvalidMarksError(subject, value, roll, reason="no value given")

    try:
        mark = float(raw)
    except (TypeError, ValueError):
        # float("abc") -> ValueError,  float(None) -> TypeError
        raise InvalidMarksError(subject, value, roll) from None

    if mark != mark:                       # NaN is the only value != itself
        raise InvalidMarksError(subject, value, roll, reason="not a real number")

    if mark < MIN_MARK or mark > MAX_MARK:
        raise MarksOutOfRangeError(subject, mark, roll, MIN_MARK, MAX_MARK)

    log.debug("Parsed mark %r for %s as %s", value, subject, mark)
    return mark


def build_student(row, roll_key="roll", name_key="name"):
    """
    Turn one raw dictionary of strings into a validated student record.

    Returns {"roll": str, "name": str, "marks": {subject: float}}.
    Raises the first problem it finds - there is no point range-checking
    marks that belong to a record with no name on it.
    """
    roll = (row.get(roll_key) or "").strip()

    # Roll first, so every later error can quote it.
    roll = validate_text(roll, "roll", roll or None)
    name = validate_text(row.get(name_key), "name", roll)

    marks = {}
    missing_subjects = []

    for subject in SUBJECTS:
        # The CSV header is lower case; the display names are not.
        raw = row.get(subject.lower())
        if raw is None:
            missing_subjects.append(subject)
            continue
        marks[subject] = validate_mark(raw, subject, roll)

    if missing_subjects:
        # A short record is a structural problem, not a bad value, so it
        # gets its own exception type.
        raise SubjectCountError(SUBJECT_COUNT - len(missing_subjects),
                                SUBJECT_COUNT, roll)

    log.debug("Built record for %s (%s) with %d subjects",
              name, roll, len(marks))
    return {"roll": roll, "name": name, "marks": marks}


def load_rows(path=DATA_FILE):
    """
    Read the CSV and return a list of raw dictionaries - no validation.

    Failures here are CRITICAL rather than ERROR: one bad student is a
    record to skip, but an unreadable data file means there is nothing to
    process at all. The exception is re-raised so main.py can stop.
    """
    log.info("Loading student records from %s", os.path.relpath(path, BASE_DIR))

    try:
        with open(path, newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)

    except FileNotFoundError:
        log.critical("Data file not found: %s - nothing to process", path)
        raise
    except PermissionError:
        log.critical("Data file could not be opened (permission): %s", path)
        raise
    except OSError:
        log.critical("Data file could not be read: %s", path, exc_info=True)
        raise

    if not rows:
        log.warning("Data file %s contains a header but no student rows",
                    os.path.basename(path))

    log.info("Loaded %d raw record(s)", len(rows))
    return rows
