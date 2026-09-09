"""
exceptions.py - the vocabulary this application uses for failure
================================================================
Every error this program can hit gets its own class, all of them
descended from one base. That base is what makes the design work:

    except StudentDataError as error:      <- catches ALL of them
    except InvalidMarksError as error:     <- catches exactly one

so `main.py` can say "any problem with this student, skip them and carry
on" in a single clause, while a module that cares about one specific
problem can still single it out.

WHY NOT JUST RAISE ValueError?
    `raise ValueError("bad marks")` works, and then every caller has to
    read the message string to find out what went wrong. A class carries
    that meaning in its *type*, so the code can branch on it, and the
    exception can hold structured fields - which student, which subject,
    which value - instead of one flattened sentence.

THE HIERARCHY
    Exception
     └── StudentDataError            base for everything below
          ├── MissingStudentInfoError    no roll number, or no name
          ├── InvalidMarksError          not a number at all
          │    └── MarksOutOfRangeError  a number, but not 0-100
          ├── SubjectCountError          not exactly 5 subjects
          └── ResultCalculationError     the arithmetic itself failed

MarksOutOfRangeError inherits from InvalidMarksError on purpose: 105 IS
invalid marks, just invalid in a more specific way. Catching
InvalidMarksError therefore catches both, which is what a caller that
only cares "were the marks usable?" wants.
"""


class StudentDataError(Exception):
    """
    Base class for every error raised by this application.

    Subclassing this rather than Exception directly is what lets one
    `except StudentDataError` clause in main.py skip a bad record without
    also swallowing genuine bugs like a typo in a variable name.
    """

    def __init__(self, message, roll=None):
        # Passing the message up to Exception is what makes str(error)
        # and the traceback show something useful.
        super().__init__(message)
        self.message = message
        self.roll = roll        # which student, when we know

    def __str__(self):
        if self.roll:
            return f"[roll {self.roll}] {self.message}"
        return self.message


class MissingStudentInfoError(StudentDataError):
    """
    Raised when a required detail is absent - roll number or name.

    A result sheet with no name on it is not a result sheet, so this is
    refused before any arithmetic is attempted.
    """

    def __init__(self, field, roll=None):
        super().__init__(f"Missing student information: {field!r} is empty",
                         roll)
        self.field = field


class InvalidMarksError(StudentDataError):
    """
    Raised when a mark cannot be used as a number.

    This is the custom exception the assignment asks for. It carries the
    subject and the offending raw value, so the log line can say exactly
    what was typed rather than just "invalid input".
    """

    def __init__(self, subject, value, roll=None, reason="not a number"):
        super().__init__(
            f"Invalid marks for {subject}: {value!r} ({reason})", roll)
        self.subject = subject
        self.value = value
        self.reason = reason


class MarksOutOfRangeError(InvalidMarksError):
    """
    Raised when a mark parses as a number but falls outside 0-100.

    A subclass of InvalidMarksError, because 105 and "abc" are both
    unusable marks - one is simply unusable for a different reason.
    """

    def __init__(self, subject, value, roll=None, low=0, high=100):
        super().__init__(subject, value, roll,
                         reason=f"outside the valid range {low}-{high}")
        self.low = low
        self.high = high


class SubjectCountError(StudentDataError):
    """
    Raised when a record does not carry exactly the expected 5 subjects.

    Four marks would still divide and still produce a percentage - a
    wrong one. Refusing the record is safer than quietly reporting a
    number nobody can reproduce.
    """

    def __init__(self, found, expected, roll=None):
        super().__init__(
            f"Expected {expected} subject marks, found {found}", roll)
        self.found = found
        self.expected = expected


class ResultCalculationError(StudentDataError):
    """
    Raised when the arithmetic itself cannot be completed.

    In practice this wraps a ZeroDivisionError: a percentage needs a
    non-zero maximum to divide by, and an empty subject list gives zero.
    Wrapping it converts a low-level Python error into one that names the
    student it belongs to.
    """
