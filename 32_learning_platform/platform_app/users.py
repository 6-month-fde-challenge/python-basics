"""
users.py - User, and the two kinds of user
===========================================
    User
      |
      +---- Student    (course, completed assignments)
      |
      +---- Mentor     (expertise, students assigned)

Every requirement of the exercise is visible in this one file:

    class variable      User.total_users, User.platform_name, ID_PREFIX
    class method        User.get_total_users(), User.set_platform_name(), _new_id()
    static method       User.is_valid_email()
    inheritance         Student(User), Mentor(User)
    constructor         __init__ in all three, children calling super()
    instance methods    assign_course(), submit_assignment(), assign_student(), ...

`registry.py` builds these; it does not define them.
"""

from .exceptions import MentorFullError, ValidationError


class User:
    """Anybody with an account: the four lines every user has."""

    # ---------------------------------------------------------------- class
    total_users = 0                   # counts every user, of every kind
    platform_name = "Nova Learn"

    ID_PREFIX = "U"                   # overridden by both children
    _sequence = 0                     # each class keeps its own - see _new_id

    # ------------------------------------------------------------ construct

    def __init__(self, name, email, user_id=None):
        if not isinstance(name, str) or not name.strip():
            raise ValidationError("name", name, "must be a non-empty string")
        if not self.is_valid_email(email):
            raise ValidationError("email", email, "must look like name@example.com")

        self.name = name.strip()
        self.email = email.strip().lower()
        self.user_id = user_id or self._new_id()

        User.total_users += 1         # the base class, so both children count here

    # --------------------------------------------------------------- static

    @staticmethod
    def is_valid_email(email):
        """True when `email` has one @, something before it, and a dot after.

        Needs neither the user nor the class, so it is a static method - and
        that is what lets __init__ call it before the object exists.
        """
        if not isinstance(email, str) or email.count("@") != 1:
            return False
        user, _, domain = email.strip().partition("@")
        if not user or not domain or domain.startswith(".") or domain.endswith("."):
            return False
        return "." in domain

    # ---------------------------------------------------------------- class

    @classmethod
    def _new_id(cls):
        """S001, M002, ... - the prefix and the counter both come from cls.

        `cls._sequence += 1` reads User._sequence the first time it runs for a
        subclass and then assigns to the subclass, so Student and Mentor end up
        with a counter each. Declaring `_sequence = 0` in both children makes
        that explicit rather than accidental.
        """
        cls._sequence += 1
        return f"{cls.ID_PREFIX}{cls._sequence:03d}"

    @classmethod
    def get_total_users(cls):
        """How many users exist, of any kind."""
        return cls.total_users

    @classmethod
    def set_platform_name(cls, name):
        """Rename the platform for every user at once."""
        if not isinstance(name, str) or not name.strip():
            raise ValidationError("platform name", name, "must be a non-empty string")
        User.platform_name = name.strip()
        return User.platform_name

    # ------------------------------------------------------------- instance

    def role(self):
        """Overridden by both children."""
        return "User"

    def display_details(self):
        """The four lines every user has. Children extend this."""
        print(f"    {self.name}  ({self.user_id})")
        print(f"      role      : {self.role()}")
        print(f"      email     : {self.email}")
        print(f"      platform  : {self.platform_name}")

    # -------------------------------------------------------------- dunders

    def __repr__(self):
        return f"{type(self).__name__}({self.user_id!r}, {self.name!r}, {self.email!r})"


class Student(User):
    """A learner: one course, and a list of assignments handed in."""

    ID_PREFIX = "S"
    _sequence = 0                     # its own counter, not User's
    REQUIRED_ASSIGNMENTS = 5

    def __init__(self, name, email, course=None, user_id=None):
        super().__init__(name, email, user_id)

        self.course = None
        self.completed_assignments = []      # its own list, one per student
        self.mentor = None

        if course:
            self.assign_course(course)

    # ------------------------------------------------------------ overrides

    def role(self):
        return "Student"

    def display_details(self):
        super().display_details()
        print(f"      course    : {self.course or 'not assigned yet'}")
        print(f"      mentor    : {self.mentor.name if self.mentor else 'none'}")
        print(f"      submitted : {self.completed_count()} of "
              f"{self.REQUIRED_ASSIGNMENTS}  ({self.progress():.0f}%)")
        if self.completed_assignments:
            for number, title in enumerate(self.completed_assignments, 1):
                print(f"        {number}. {title}")
        print(f"      status    : {'COMPLETED' if self.has_finished() else 'in progress'}")

    # ------------------------------------------------------------- its own

    def assign_course(self, course):
        """Put this student on a course. Returns the previous one, or None."""
        if not isinstance(course, str) or not course.strip():
            raise ValidationError("course", course, "must be a non-empty string")
        previous, self.course = self.course, course.strip()
        return previous

    def submit_assignment(self, title):
        """Hand in one assignment. Returns how many have been handed in."""
        if not isinstance(title, str) or not title.strip():
            raise ValidationError("assignment", title, "must be a non-empty string")
        if self.course is None:
            raise ValidationError("assignment", title,
                                  "the student is not on a course yet")

        title = title.strip()
        if title in self.completed_assignments:
            raise ValidationError("assignment", title, "has already been submitted")

        self.completed_assignments.append(title)
        return len(self.completed_assignments)

    def completed_count(self):
        return len(self.completed_assignments)

    def progress(self):
        """Percentage of the required assignments handed in, capped at 100."""
        done = self.completed_count() / self.REQUIRED_ASSIGNMENTS * 100
        return round(min(done, 100.0), 2)

    def has_finished(self):
        return self.completed_count() >= self.REQUIRED_ASSIGNMENTS


class Mentor(User):
    """A mentor: an area of expertise, and the students assigned to them."""

    ID_PREFIX = "M"
    _sequence = 0
    MAX_STUDENTS = 3

    def __init__(self, name, email, expertise, user_id=None):
        if not isinstance(expertise, str) or not expertise.strip():
            raise ValidationError("expertise", expertise, "must be a non-empty string")

        super().__init__(name, email, user_id)

        self.expertise = expertise.strip()
        self.students = []                   # its own list, one per mentor

    # ------------------------------------------------------------ overrides

    def role(self):
        return "Mentor"

    def display_details(self):
        super().display_details()
        print(f"      expertise : {self.expertise}")
        print(f"      students  : {self.student_count()} of {self.MAX_STUDENTS}")
        for student in self.students:
            print(f"        {student.user_id}  {student.name:<16}"
                  f"{student.course or '-':<18}{student.progress():>6.0f}%")
        print(f"      capacity  : {'full' if self.is_full() else 'taking students'}")

    # ------------------------------------------------------------- its own

    def assign_student(self, student):
        """Take on one student. Returns how many this mentor now has."""
        if not isinstance(student, Student):
            raise ValidationError("student", student, "is not a Student")
        # membership before capacity: adding the same student twice would pass a
        # capacity check and still be wrong
        if student in self.students:
            raise ValidationError("student", student.user_id,
                                  f"is already assigned to {self.name}")
        if self.is_full():
            raise MentorFullError(self, self.MAX_STUDENTS)

        self.students.append(student)
        student.mentor = self
        return len(self.students)

    def student_count(self):
        return len(self.students)

    def is_full(self):
        return len(self.students) >= self.MAX_STUDENTS

    def average_progress(self):
        """Mean progress across this mentor's students. 0.0 with none."""
        if not self.students:
            return 0.0
        # the accumulator pattern from exercise 18, rather than sum()
        total = 0
        for student in self.students:
            total += student.progress()
        return round(total / len(self.students), 2)
