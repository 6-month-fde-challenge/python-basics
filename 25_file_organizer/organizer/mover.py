"""
organizer.mover - actually moving the file, safely
==================================================
The only module in the package that changes anything on disk, which is
why it is the one with the most defensive code in it.

THREE THINGS IT GUARANTEES
    1. the destination folder exists before the move is attempted
    2. an existing file is NEVER overwritten - a free name is found first
    3. a FAILED move leaves nothing behind - see undo_partial()

WHO WRITES THE "MOVED" AND "FAILED" LINES
    Not this module. It raises an exception carrying the reason, and
    main.py writes exactly one line per file. The rule is: the PACKAGE
    describes what happened, the APPLICATION decides what it means and
    records it. Logging in both places is how a log ends up with two
    lines for one failure, which is worse than none - it makes the
    counts wrong.

    What this module does log is DEBUG detail nobody else can see: the
    names it tried, and the raw OSError text.

WHY NOT JUST shutil.move?
    shutil.move(src, dst) silently overwrites dst on most platforms. For
    a program whose whole job is relocating a user's files, "silently
    overwrites" is the one behaviour that must not happen: the duplicate
    photo.jpg would destroy the original photo.jpg and the log would
    cheerfully record a success.

THE DUPLICATE RULE
    photo.jpg exists      -> photo (1).jpg
    photo (1).jpg exists  -> photo (2).jpg
    ... up to 999, then DuplicateFileError
"""
import os
import shutil

from .errors import DestinationError, DuplicateFileError, FileAccessError, \
    SourceNotFoundError
from .logger_config import get_logger

log = get_logger("mover")

MAX_DUPLICATE_ATTEMPTS = 1000


def ensure_folder(path):
    """
    Make sure `path` is a usable folder, creating it if needed.

    Raises DestinationError when it cannot be - including the awkward
    case where a *file* already occupies the name the folder needs.
    """
    if os.path.isdir(path):
        return path

    if os.path.exists(path):
        # Something is there, and it is not a directory.
        raise DestinationError(
            "Destination name is already taken by a file", path)

    try:
        os.makedirs(path, exist_ok=True)
    except PermissionError as error:
        raise FileAccessError(path, error) from error
    except OSError as error:
        raise DestinationError(
            f"Could not create folder: {error.strerror or error}", path) from error

    # WARNING, not INFO: creating a folder is a side effect the user did
    # not explicitly ask for, and they should be able to see it happened.
    log.warning("Created destination folder: %s", os.path.basename(path))
    return path


def unique_destination(folder, filename):
    """
    Return a path inside `folder` that no file currently occupies.

    Returns (path, renamed) so the caller knows whether a duplicate was
    resolved - the rename is worth a WARNING, and only the caller has the
    context to phrase it.
    """
    candidate = os.path.join(folder, filename)
    if not os.path.exists(candidate):
        return candidate, False

    stem, extension = os.path.splitext(filename)

    for counter in range(1, MAX_DUPLICATE_ATTEMPTS):
        attempt = os.path.join(folder, f"{stem} ({counter}){extension}")
        log.debug("Name taken, trying %s", os.path.basename(attempt))
        if not os.path.exists(attempt):
            return attempt, True

    raise DuplicateFileError(candidate, MAX_DUPLICATE_ATTEMPTS)


def undo_partial(source, target):
    """
    Delete a half-finished copy left behind by a failed move.

    shutil.move() is not one operation. When the source and destination
    are on the same drive it renames, which either happens or does not.
    When the rename is refused it falls back to COPY-then-DELETE - and if
    the delete is the part that fails, the copy has already succeeded.

    That is exactly what a locked file does on Windows: the move reports
    PermissionError while the destination file now exists and the source
    is still there. Without this cleanup the next run finds a duplicate
    it created itself, and the user quietly ends up with two copies of a
    file the program said it had failed to move.

    Only ever called when the source still exists, and only on a target
    that unique_destination() proved was free moments earlier.
    """
    if not os.path.exists(target):
        return False
    if not os.path.exists(source):
        # The source is gone, so the move actually completed. Deleting
        # the target here would destroy the only remaining copy.
        return False

    try:
        os.remove(target)
    except OSError as error:
        log.error("Could not remove the half-finished copy %s: %s",
                  target, error)
        return False

    log.warning("Removed the half-finished copy left at %s/%s by a failed move",
                os.path.basename(os.path.dirname(target)),
                os.path.basename(target))
    return True


def move(source, destination_root, category):
    """
    Move one file into destination_root/category/. Return the new path.

    Raises SourceNotFoundError, DestinationError, DuplicateFileError or
    FileAccessError - all subclasses of FileOrganizerError, so one clause
    in main.py catches every one of them.
    """
    filename = os.path.basename(source)

    if not os.path.isfile(source):
        # Checked again here, not only in detector: files can disappear
        # between being listed and being moved.
        raise SourceNotFoundError(source)

    target_folder = ensure_folder(os.path.join(destination_root, category))
    target, renamed = unique_destination(target_folder, filename)

    if renamed:
        log.warning("Duplicate name in %s: %s -> %s",
                    category, filename, os.path.basename(target))

    try:
        shutil.move(source, target)

    except PermissionError as error:
        # On Windows this is what an open file handle produces: the file
        # is there, the folder is fine, and the OS still says no. The
        # copy half of shutil.move may already have run, so clean up
        # before reporting the failure.
        log.debug("shutil.move refused %s: %s", filename, error)
        undo_partial(source, target)
        raise FileAccessError(source, error) from error

    except FileNotFoundError as error:
        log.debug("shutil.move lost %s: %s", filename, error)
        raise SourceNotFoundError(source) from error

    except OSError as error:
        log.debug("shutil.move failed on %s: %s", filename, error)
        undo_partial(source, target)
        raise DestinationError(
            f"Move failed: {error.strerror or error}", source) from error

    log.debug("shutil.move done: %s -> %s", filename, target)
    return target
