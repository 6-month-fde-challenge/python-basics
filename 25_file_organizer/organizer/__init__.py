"""
organizer - a package for sorting files into folders by extension
=================================================================
This file is what makes the `organizer/` FOLDER a `organizer` PACKAGE.
Without it Python 3 would still import the directory (namespace
packages), but nothing would run at import time and there would be no
single place that says what the package offers.

WHAT A PACKAGE ADDS OVER FOUR LOOSE MODULES
    1. one name to import          `from organizer import detector`
    2. relative imports inside     `from .errors import ...`
       the package, so the modules refer to each other without caring
       what the package is called or where it sits
    3. a front door - this file - listing the public API, so a caller
       never has to know that `move` happens to live in mover.py
    4. a namespace: organizer.errors cannot collide with anyone else's
       errors.py

THE MODULES
    errors.py          the exception vocabulary   (imports nothing of ours)
    logger_config.py   where log records go       (imports nothing of ours)
    detector.py        which folder a file belongs to
    mover.py           moving it there, safely

The import order above is also the dependency order. errors and
logger_config sit at the bottom and depend on nothing, which is what
keeps the package free of circular imports.

USAGE
    from organizer import detect, move, setup_logging

    setup_logging()
    category = detect("photo.jpg")        # "Images"
    move("photo.jpg", "organized", category)
"""
from .detector import CATEGORIES, EXTENSION_MAP, detect, scan, \
    summarise_categories
from .errors import (
    DestinationError,
    DuplicateFileError,
    FileAccessError,
    FileOrganizerError,
    SourceNotFoundError,
    UnsupportedFileError,
)
from .logger_config import get_logger, setup_logging, start_run
from .mover import ensure_folder, move, unique_destination

__version__ = "1.0"

# `from organizer import *` imports exactly these names and nothing else.
# Being explicit here is what makes the package's surface a decision
# rather than an accident of which modules happen to exist.
__all__ = [
    # detection
    "detect", "scan", "CATEGORIES", "EXTENSION_MAP", "summarise_categories",
    # movement
    "move", "ensure_folder", "unique_destination",
    # logging
    "setup_logging", "get_logger", "start_run",
    # errors
    "FileOrganizerError", "UnsupportedFileError", "SourceNotFoundError",
    "DestinationError", "DuplicateFileError", "FileAccessError",
]
