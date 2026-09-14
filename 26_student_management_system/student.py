"""
student.py - the Student class
===============================
One class, one job: hold everything known about a student and answer questions
about them.

    from student import Student

    aarav = Student("Aarav Sharma", "aarav@example.com", "S101", "Python")
    aarav.update_marks("Python", 88)
    aarav.average_marks()          # 88.0
    Student.get_total_students()   # 1

Nothing here prints except display_details(), which exists to print. Everything
else returns a value, so main.py decides what to do with it - the rule from
exercise 19.
"""


class Student:
    """A student on a course, with marks per subject."""

    # ---------------------------------------------------------------- class
    # One copy of each of these exists, shared by every Student object.

    total_students = 0        # how many Student objects have been built
    institute = "Nova Institute of Technology"
    PASS_MARK = 40
    MAX_MARK = 100

    GRADE_BANDS = (           # (lowest average that earns it, grade)
        (90, "A+"),
        (80, "A"),
        (70, "B"),
        (60, "C"),
        (50, "D"),
        (40, "E"),
    )

    # ------------------------------------------------------------ construct

    def __init__(self, name, email, student_id, course, marks=None):
        """Build one student. Called by Student(...) - never by hand.

        marks is optional: a dict of {subject: score}. It is copied, because a
        dict passed in is a shared object and a student who edits their marks
        should not edit somebody else's.
        """
        self.name = name
        self.email = email
        self.student_id = student_id
        self.course = course
        self.marks = {}

        if marks:
            for subject, score in marks.items():
                self.update_marks(subject, score)   # validated on the way in

        Student.total_students += 1                 # the class, not self

    # ------------------------------------------------------------- instance

    def update_marks(self, subject, score):
        """Set or replace the score for one subject. Returns the old score."""
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("subject must be a non-empty string")
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            raise ValueError(f"score for {subject!r} must be a number, got {score!r}")
        if not 0 <= score <= self.MAX_MARK:
            raise ValueError(
                f"score for {subject!r} must be between 0 and {self.MAX_MARK}, got {score}"
            )

        subject = subject.strip()
        previous = self.marks.get(subject)
        self.marks[subject] = score
        return previous

    def average_marks(self):
        """Mean of every recorded score. 0.0 for a student with no marks yet."""
        if not self.marks:
            return 0.0
        # the accumulator pattern from exercise 18, rather than sum()
        total = 0
        for score in self.marks.values():
            total += score
        return round(total / len(self.marks), 2)

    def highest_subject(self):
        """(subject, score) of the best result, or None if there are no marks."""
        if not self.marks:
            return None
        # the champion pattern from exercise 18, rather than max()
        best_subject, best_score = None, -1
        for subject, score in self.marks.items():
            if score > best_score:
                best_subject, best_score = subject, score
        return best_subject, best_score

    def grade(self):
        """Letter grade for the average, or 'F' below the pass mark."""
        average = self.average_marks()
        for lowest, letter in self.GRADE_BANDS:
            if average >= lowest:
                return letter
        return "F"

    def has_passed(self):
        """True when every recorded subject is at or above the pass mark."""
        if not self.marks:
            return False
        for score in self.marks.values():
            if score < self.PASS_MARK:
                return False
        return True

    def display_details(self):
        """Print the student as a block. The only method here that prints."""
        print(f"    {self.name}  ({self.student_id})")
        print(f"      email    : {self.email}")
        print(f"      course   : {self.course}")
        if self.marks:
            for subject, score in self.marks.items():
                flag = "" if score >= self.PASS_MARK else "   <- below pass mark"
                print(f"      {subject:<14} {score:>3}{flag}")
            top_subject, top_score = self.highest_subject()
            print(f"      average  : {self.average_marks():.2f}   grade {self.grade()}")
            print(f"      best     : {top_subject} ({top_score})")
            print(f"      result   : {'PASS' if self.has_passed() else 'FAIL'}")
        else:
            print("      marks    : none recorded yet")

    # ---------------------------------------------------------------- class

    @classmethod
    def get_total_students(cls):
        """How many Student objects exist. Asked of the class, not a student."""
        return cls.total_students

    @classmethod
    def set_institute(cls, name):
        """Rename the institute for every student at once."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("institute name must be a non-empty string")
        cls.institute = name.strip()
        return cls.institute

    # --------------------------------------------------------------- static

    @staticmethod
    def is_valid_email(email):
        """A deliberately simple check: one @, something either side, one dot."""
        if not isinstance(email, str) or email.count("@") != 1:
            return False
        user, _, domain = email.partition("@")
        return bool(user) and "." in domain and not domain.startswith(".")

    # -------------------------------------------------------------- dunders

    def __repr__(self):
        return f"Student({self.name!r}, {self.student_id!r}, {self.course!r})"


if __name__ == "__main__":
    # A module self-test, the pattern from exercise 24: this block runs only
    # when the file is executed directly, never when main.py imports it.
    demo = Student("Test Student", "test@example.com", "S000", "Python",
                   {"Python": 80, "Maths": 70})
    demo.display_details()
    print()
    print("total students:", Student.get_total_students())
