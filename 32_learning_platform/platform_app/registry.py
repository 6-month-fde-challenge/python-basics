"""
registry.py - the platform itself
==================================
`LearningPlatform` owns the users; it does not inherit from them. That is the
other half of object-oriented design: `Student` and `Mentor` are **kinds of**
`User` (inheritance), and a platform **has** users (composition).

    from platform_app import LearningPlatform

    site = LearningPlatform("Nova Learn")
    aarav = site.register_student("Aarav Sharma", "aarav@example.com", "Python")
    site.submit_assignment(aarav.user_id, "Loops and conditionals")
"""

from .exceptions import DuplicateUserError, UnknownUserError, ValidationError
from .users import Mentor, Student, User


class LearningPlatform:
    """One place that knows about every user, and nothing about how they work."""

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValidationError("platform name", name, "must be a non-empty string")

        self.name = name.strip()
        self.users = {}                    # user_id -> User
        User.set_platform_name(self.name)  # one class variable, set once

    # ---------------------------------------------------------- registering

    def _register(self, user):
        """Shared by both register_* methods: refuse a duplicate email, then store."""
        for existing in self.users.values():
            if existing.email == user.email:
                raise DuplicateUserError(user.email, existing.user_id)
        self.users[user.user_id] = user
        return user

    def register_student(self, name, email, course=None):
        """Build a Student and put them on the platform."""
        return self._register(Student(name, email, course))

    def register_mentor(self, name, email, expertise):
        """Build a Mentor and put them on the platform."""
        return self._register(Mentor(name, email, expertise))

    # -------------------------------------------------------------- finding

    def find(self, user_id):
        """The user with that id, or UnknownUserError."""
        try:
            return self.users[user_id]
        except KeyError:
            raise UnknownUserError(user_id) from None

    def students(self):
        return [u for u in self.users.values() if isinstance(u, Student)]

    def mentors(self):
        return [u for u in self.users.values() if isinstance(u, Mentor)]

    # ---------------------------------------------------------------- doing

    def assign_course(self, student_id, course):
        """Put a registered student on a course."""
        student = self.find(student_id)
        if not isinstance(student, Student):
            raise ValidationError("user", student_id, "is not a student")
        student.assign_course(course)
        return student

    def assign_mentor(self, student_id, mentor_id):
        """Give a student a mentor, if the mentor has room."""
        student, mentor = self.find(student_id), self.find(mentor_id)
        if not isinstance(student, Student):
            raise ValidationError("user", student_id, "is not a student")
        if not isinstance(mentor, Mentor):
            raise ValidationError("user", mentor_id, "is not a mentor")
        mentor.assign_student(student)
        return mentor

    def submit_assignment(self, student_id, title):
        """Record one assignment for one student."""
        student = self.find(student_id)
        if not isinstance(student, Student):
            raise ValidationError("user", student_id, "is not a student")
        return student.submit_assignment(title)

    # -------------------------------------------------------------- showing

    def display_user(self, user_id):
        """Print whichever kind of user that id belongs to."""
        self.find(user_id).display_details()

    def total_users(self):
        """How many users this platform holds."""
        return len(self.users)

    def report(self):
        """A one-line-per-user summary of the whole platform."""
        print(f"    {self.name}: {self.total_users()} users "
              f"({len(self.students())} students, {len(self.mentors())} mentors)")
        print()
        print(f"    {'id':<7}{'name':<18}{'role':<10}{'detail':<22}{'progress':>9}")
        print(f"    {'-' * 66}")
        for user in self.users.values():
            if isinstance(user, Student):
                detail = user.course or "no course"
                progress = f"{user.progress():.0f}%"
            else:
                detail = user.expertise
                progress = f"{user.student_count()}/{user.MAX_STUDENTS}"
            print(f"    {user.user_id:<7}{user.name:<18}{user.role():<10}"
                  f"{detail:<22}{progress:>9}")

    def __repr__(self):
        return f"LearningPlatform({self.name!r}, users={len(self.users)})"
