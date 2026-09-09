"""
organizer.errors - the exception vocabulary of the package
==========================================================
One base class, five specific ones. The base is what lets main.py write

    except FileOrganizerError as error:     <- any problem with this file
        log.error(...); continue            <- skip it, keep organizing

while `detector` and `mover` can still raise something precise enough to
act on.

THE HIERARCHY
    Exception
     └── FileOrganizerError          base for everything this package raises
          ├── UnsupportedFileError       extension not in the category map
          ├── SourceNotFoundError        the file or folder is not there
          ├── DestinationError           the target folder cannot be used
          ├── DuplicateFileError         a unique name could not be found
          └── FileAccessError            the OS refused (permissions, locks)

FileAccessError WRAPS PermissionError RATHER THAN REPLACING IT
    The original is kept on `.cause`, so the log can print the OS message
    ("used by another process") alongside our own. Losing that detail is
    the usual mistake when wrapping exceptions - the new type is clearer
    but the reason disappears.
"""


class FileOrganizerError(Exception):
    """
    Base class for every error this package raises.

    `path` is carried on the exception rather than baked into the message,
    so a caller can log the message and still use the path.
    """

    def __init__(self, message, path=None):
        super().__init__(message)
        self.message = message
        self.path = path

    def __str__(self):
        if self.path:
            return f"{self.message} [{self.path}]"
        return self.message


class UnsupportedFileError(FileOrganizerError):
    """
    Raised when a file's extension has no category.

    This is the custom exception the assignment names. It is deliberately
    NOT a hard failure at the top level: main.py catches it, counts the
    file as skipped, logs a WARNING and moves to the next one. An unknown
    extension is a gap in the category map, not a broken program.
    """

    def __init__(self, path, extension):
        shown = extension or "(no extension)"
        super().__init__(f"Unsupported file type {shown}", path)
        self.extension = extension


class SourceNotFoundError(FileOrganizerError):
    """Raised when the file or folder to organize does not exist."""

    def __init__(self, path):
        super().__init__("Source does not exist", path)


class DestinationError(FileOrganizerError):
    """
    Raised when the destination folder cannot be created or used.

    Covers the missing-folder case the assignment asks about, and the
    nastier one where a *file* already sits at the path a folder needs.
    """

    def __init__(self, message, path=None):
        super().__init__(message, path)


class DuplicateFileError(FileOrganizerError):
    """
    Raised when a non-clashing name could not be produced.

    Duplicates are normally solved silently by renaming - photo.jpg
    becomes "photo (1).jpg". This fires only when even that fails, which
    in practice means a thousand copies already exist.
    """

    def __init__(self, path, attempts):
        super().__init__(f"No free filename after {attempts} attempts", path)
        self.attempts = attempts


class FileAccessError(FileOrganizerError):
    """
    Raised when the operating system refuses the operation.

    On Windows this is what an open file handle produces: the file
    exists, the destination is fine, and the move still fails because
    something else is holding it.
    """

    def __init__(self, path, cause=None):
        # str(PermissionError) repeats the whole absolute path inside the
        # message, which then appears twice on every line. `.strerror` is
        # the OS explanation on its own - "The process cannot access the
        # file because it is being used by another process" - which is
        # the only part the reader did not already know.
        detail = getattr(cause, "strerror", None) or (str(cause) if cause else "")
        super().__init__(
            f"Access denied by the operating system: {detail}".rstrip(": "),
            path)
        self.cause = cause
