"""
platform_app - the learning platform package
=============================================
The front door. A caller writes

    from platform_app import LearningPlatform, Student, Mentor

and never has to know which module each name lives in.

Import order is dependency order, so there are no circular imports:

    exceptions   imports nothing of ours
    users        imports exceptions
    registry     imports exceptions and users
"""

from .exceptions import (DuplicateUserError, MentorFullError, PlatformError,
                         UnknownUserError, ValidationError)
from .registry import LearningPlatform
from .users import Mentor, Student, User

__all__ = [
    "LearningPlatform",
    "User", "Student", "Mentor",
    "PlatformError", "ValidationError", "DuplicateUserError",
    "UnknownUserError", "MentorFullError",
]

__version__ = "1.0"
