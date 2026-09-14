"""
exceptions.py - everything this package raises
===============================================
One base class, four subclasses. A caller that does not care which went wrong
writes one clause:

    except PlatformError as error:
        print(error)

Nothing in this module imports anything of ours, which is what makes it the first
file in the package's import order.
"""


class PlatformError(Exception):
    """Base class for every error the platform raises."""


class ValidationError(PlatformError):
    """A value that cannot be used - a blank name, a malformed email."""

    def __init__(self, field, value, reason):
        self.field = field
        self.value = value
        self.reason = reason
        super().__init__(f"{field} {value!r} is not usable: {reason}")


class DuplicateUserError(PlatformError):
    """Someone with that email is already registered."""

    def __init__(self, email, existing_id):
        self.email = email
        self.existing_id = existing_id
        super().__init__(f"{email} is already registered as {existing_id}")


class UnknownUserError(PlatformError):
    """No user with that id."""

    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(f"no user with id {user_id!r}")


class MentorFullError(PlatformError):
    """A mentor who already has as many students as they can take."""

    def __init__(self, mentor, limit):
        self.mentor = mentor
        self.limit = limit
        super().__init__(
            f"{mentor.name} already has {limit} students, which is the maximum"
        )
