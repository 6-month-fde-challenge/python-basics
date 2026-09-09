"""
organizer.detector - deciding WHERE a file belongs
==================================================
This module answers exactly one question: given a filename, which folder
should it go to? It never touches the disk beyond asking whether a path
exists, and it never moves anything - that is mover.py's job.

    photo.jpg    -> Images
    notes.txt    -> Text
    report.pdf   -> Documents
    data.csv     -> Data
    mystery.xyz  -> UnsupportedFileError

THE MAP IS WRITTEN CATEGORY-FIRST, THEN INVERTED
    CATEGORIES is easy for a human to read and edit - one line per
    destination folder. EXTENSION_MAP is what the lookup actually needs -
    one entry per extension. Building the second from the first means the
    two can never disagree, and adding ".webp" to Images is a one-word
    change.

CASE AND DOTS
    os.path.splitext("Photo.JPG") -> ("Photo", ".JPG"), so the extension
    is lower-cased before the lookup.

    Dotfiles are the case worth checking rather than assuming. It is
    tempting to think ".editorconfig" splits into ("", ".editorconfig")
    and needs special handling - it does not:

        splitext("photo.jpg")      -> ("photo", ".jpg")
        splitext("README")         -> ("README", "")
        splitext(".editorconfig")  -> (".editorconfig", "")   <- no ext
        splitext("archive.tar.gz") -> ("archive.tar", ".gz")

    splitext ignores a leading period, so a dotfile already comes back
    with an EMPTY extension - the same answer as a file with no
    extension at all. One `if not extension` covers both, and the
    special case is unnecessary.
"""
import os

from .errors import SourceNotFoundError, UnsupportedFileError
from .logger_config import get_logger

log = get_logger("detector")

# Category -> the extensions that belong in it. Edit this, nothing else.
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico"],
    "Text": [".txt", ".md", ".rtf", ".log"],
    "Documents": [".pdf", ".doc", ".docx", ".odt", ".ppt", ".pptx"],
    "Data": [".csv", ".xlsx", ".xls", ".json", ".xml", ".yaml", ".yml", ".db"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a", ".ogg"],
    "Video": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".sh"],
}

# Inverted once, at import time: ".jpg" -> "Images", ".png" -> "Images", ...
# A dictionary lookup is one step regardless of how many categories exist;
# scanning the lists on every file would be eight.
EXTENSION_MAP = {}
for _category, _extensions in CATEGORIES.items():
    for _extension in _extensions:
        EXTENSION_MAP[_extension] = _category


def get_extension(filename):
    """
    Return the lower-case extension of a filename, or "" if it has none.

    Both "README" and ".editorconfig" return "", because splitext
    ignores a leading period - see the note at the top of this module.
    """
    _stem, extension = os.path.splitext(filename)
    return extension.lower()


def detect(path):
    """
    Return the category folder name for one file.

    Raises SourceNotFoundError if the path is not a file, and
    UnsupportedFileError if the extension has no category. Raising rather
    than returning None is what lets the caller distinguish the two - and
    the caller does care: one is a missing file, the other is a gap in
    the map.
    """
    filename = os.path.basename(path)
    log.debug("Detecting category for %s", filename)

    if not os.path.exists(path):
        raise SourceNotFoundError(path)

    if not os.path.isfile(path):
        # A folder is not an unsupported file type; it is not a file.
        raise SourceNotFoundError(path)

    extension = get_extension(filename)

    if not extension:
        raise UnsupportedFileError(path, extension)

    if extension not in EXTENSION_MAP:
        raise UnsupportedFileError(path, extension)

    category = EXTENSION_MAP[extension]
    log.debug("%s -> %s (%s)", filename, category, extension)
    return category


def scan(folder):
    """
    Return the sorted list of file paths directly inside a folder.

    Sub-folders are listed but not descended into: the assignment is
    "organize a folder", and recursing would happily walk into the
    Images/ folder this program just created and organize it again.
    """
    if not os.path.exists(folder):
        raise SourceNotFoundError(folder)

    if not os.path.isdir(folder):
        raise SourceNotFoundError(folder)

    entries = sorted(os.listdir(folder))
    files = []

    for entry in entries:
        full = os.path.join(folder, entry)
        if os.path.isfile(full):
            files.append(full)
        else:
            log.debug("Skipping sub-folder %s", entry)

    log.info("Scanned %s - %d file(s), %d sub-folder(s)",
             os.path.basename(folder) or folder,
             len(files), len(entries) - len(files))
    return files


def summarise_categories():
    """Return "Images: 8, Text: 4, ..." for the run header."""
    return ", ".join(f"{name}: {len(exts)}"
                     for name, exts in CATEGORIES.items())
