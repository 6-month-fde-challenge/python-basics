"""
file_handler.py - the Read a File and Write a File activities
=============================================================
Two activities, and the four things the filesystem does to you.

    FileNotFoundError    the path is wrong                    -> ERROR
    PermissionError      the OS said no                       -> ERROR
    IsADirectoryError    the path is a folder, not a file     -> ERROR
    UnicodeDecodeError   it is not text (a .png, say)         -> ERROR

plus one thing that is not an error at all:

    the file opened, and it was empty                         -> WARNING

That distinction is the point of this module. "File was empty" and "file
could not be opened" look similar on screen and are completely different
in a log: one means check the data, the other means check the path.

`with open(...)` closes the file whether the block ends normally or
raises - it is `try/finally` written by the language.
"""
import os

from logger_config import get_logger

log = get_logger("file_handler")

# Sample files live in data/, next to this module.
APP_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(APP_DIR, "data")


def display(path):
    """
    Shorten a path for the log: data/notes.txt rather than the whole
    C:/Users/... prefix. A log is read by a person, and the part of the
    path that varies is the part worth printing.
    """
    try:
        relative = os.path.relpath(path, APP_DIR)
    except ValueError:          # different drive on Windows
        return path
    return path if relative.startswith("..") else relative


def resolve(path):
    """
    Turn what the user typed into a real path.

    A bare name like "notes.txt" is looked for in data/ first, so the
    menu is pleasant to use; anything else is treated as given.
    """
    if os.path.isabs(path) or os.sep in path or "/" in path:
        return path
    return os.path.join(DATA_DIR, path)


def read_file(path):
    """
    Return the contents of a text file, or None if it could not be read.

    Every exception is caught and logged rather than allowed to escape,
    because the menu behind this call must survive a bad filename.
    """
    full = resolve(path)
    log.debug("Read requested: %r -> %s", path, display(full))

    try:
        with open(full, "r", encoding="utf-8") as handle:
            content = handle.read()

    except FileNotFoundError:
        log.error("File could not be opened - not found: %s", display(full))
        print("   No such file.")
        return None

    except PermissionError:
        log.error("File could not be opened - permission denied: %s", display(full))
        print("   Permission denied.")
        return None

    except IsADirectoryError:
        log.error("File could not be opened - path is a directory: %s", display(full))
        print("   That path is a folder, not a file.")
        return None

    except UnicodeDecodeError:
        log.error("File could not be decoded as UTF-8 text: %s", display(full))
        print("   That file is not readable text.")
        return None

    except OSError:
        # The parent of the four above - anything else the OS refuses.
        log.exception("Unexpected OS error while reading %s", display(full))
        print("   The file could not be read.")
        return None

    # Opened successfully. An empty file is a WARNING, not a failure.
    if not content.strip():
        log.warning("File was empty: %s", display(full))
        print("   The file opened but contains nothing.")
        return ""

    log.info("File read successfully: %s (%d characters, %d lines)",
             display(full), len(content), len(content.splitlines()))
    return content


def write_file(path, text):
    """
    Write text to a file. Return True on success, False on failure.

    Mode "w" replaces the whole file, so the mode is logged: "the file
    lost its contents" is a question the log should be able to answer.
    """
    full = resolve(path)
    log.debug("Write requested: %r -> %s (mode='w', %d characters)",
              path, display(full), len(text))

    if not text.strip():
        log.warning("Writing empty content to %s", display(full))

    try:
        folder = os.path.dirname(full)
        if folder and not os.path.isdir(folder):
            log.warning("Destination folder missing, creating it: %s", display(folder))
            os.makedirs(folder, exist_ok=True)

        with open(full, "w", encoding="utf-8") as handle:
            handle.write(text)
            if not text.endswith("\n"):
                handle.write("\n")

    except PermissionError:
        log.error("File could not be written - permission denied: %s", display(full))
        print("   Permission denied.")
        return False

    except OSError:
        log.exception("Unexpected OS error while writing %s", display(full))
        print("   The file could not be written.")
        return False

    log.info("File written successfully: %s (mode='w')", display(full))
    return True


def run_read():
    """The Read a File activity as the menu sees it."""
    path = input("   File to read  : ").strip()
    if not path:
        log.warning("Read cancelled: no filename given")
        return None

    content = read_file(path)
    if content:
        print("   ---------------- contents ----------------")
        for line in content.splitlines():
            print(f"   {line}")
        print("   ------------------------------------------")
    return content


def run_write():
    """The Write a File activity as the menu sees it."""
    path = input("   File to write : ").strip()
    if not path:
        log.warning("Write cancelled: no filename given")
        return False

    text = input("   Text to store : ")
    return write_file(path, text)
