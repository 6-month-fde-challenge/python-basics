"""
organizer.logger_config - where the package writes its record
=============================================================
"Every successful and failed file operation should be recorded in a log
file." That sentence is the reason this module exists, and it is why the
log here is more detailed than in the two previous exercises: moving a
file is destructive. If the organizer put report.pdf somewhere
unexpected, the log is the only way to find it again.

So every move records BOTH ends:

    2026-09-09 08:12:04 | INFO | MOVED  photo.jpg -> Images/photo (1).jpg

WHAT EACH LEVEL MEANS HERE
    DEBUG    each candidate examined, each name tried
    INFO     a file actually moved, and the run summary
    WARNING  handled and continued - unsupported type, renamed duplicate,
             destination folder had to be created
    ERROR    this file could not be moved (locked, vanished, refused)
    CRITICAL the run cannot start at all (source folder missing)

TWO FILES
    logs/organizer.log   DEBUG and above - every operation, good and bad
    logs/errors.log      ERROR and above - only what failed
"""
import logging
import os
import sys

# The package lives in organizer/, so the project root is one level up.
PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(PACKAGE_DIR)
LOG_DIR = os.path.join(PROJECT_DIR, "logs")

MAIN_LOG = os.path.join(LOG_DIR, "organizer.log")
ERROR_LOG = os.path.join(LOG_DIR, "errors.log")

LINE_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

ROOT_NAME = "organizer"


def setup_logging(console_level=logging.WARNING):
    """
    Attach the three handlers to the "organizer" logger and return it.

    Idempotent: the `if logger.handlers` guard means a second call is a
    no-op rather than a second copy of every line.
    """
    logger = logging.getLogger(ROOT_NAME)

    if logger.handlers:
        return logger

    os.makedirs(LOG_DIR, exist_ok=True)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(LINE_FORMAT, datefmt=DATE_FORMAT)

    main_handler = logging.FileHandler(MAIN_LOG, mode="a", encoding="utf-8")
    main_handler.setLevel(logging.DEBUG)
    main_handler.setFormatter(formatter)

    error_handler = logging.FileHandler(ERROR_LOG, mode="a", encoding="utf-8")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_level)
    console_handler.setFormatter(logging.Formatter("   [%(levelname)s] %(message)s"))

    logger.addHandler(main_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)

    return logger


def get_logger(module_name):
    """Return the child logger for one module of the package."""
    return logging.getLogger(f"{ROOT_NAME}.{module_name}")


def start_run(logger, source, destination):
    """
    Write the banner that separates this run from the previous one.

    Both files append, so without this a log that has grown over five
    runs reads as one baffling run.
    """
    logger.info("=" * 62)
    logger.info("RUN STARTED   source=%s  destination=%s",
                source, destination)
