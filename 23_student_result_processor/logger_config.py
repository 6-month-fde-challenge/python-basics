"""
logger_config.py - one place that decides where log messages go
===============================================================
Same job as in exercise 22, and deliberately the same shape: a batch
processor that skips bad records is only trustworthy if every skip is
written down somewhere.

WHAT EACH LEVEL MEANS IN THIS APPLICATION
    DEBUG    each field as it is parsed          (raw value -> number)
    INFO     a student processed successfully    (name, %, grade)
    WARNING  a record repaired or skipped for a
             reason that is the data's fault     (blank name, 105 marks)
    ERROR    a record that could not be processed
             at all, or arithmetic that failed
    CRITICAL the run itself cannot continue      (data file unreadable)

TWO FILES
    logs/application.log   DEBUG and above - the full processing trace
    logs/error.log         ERROR and above - the rejected records alone

The second file is the useful one here. After a run over 200 students,
"which ones failed and why" should not require reading 2,000 lines.
"""
import logging
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")

APP_LOG = os.path.join(LOG_DIR, "application.log")
ERROR_LOG = os.path.join(LOG_DIR, "error.log")

LINE_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)-18s | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

ROOT_NAME = "results"


def setup_logging(console_level=logging.WARNING):
    """
    Attach the three handlers to the "results" logger and return it.

    The `if logger.handlers` guard makes the call idempotent. Without it,
    importing this module twice would double every line in both files.
    """
    logger = logging.getLogger(ROOT_NAME)

    if logger.handlers:
        return logger

    os.makedirs(LOG_DIR, exist_ok=True)

    # The logger is the first gate and is set to the LOWEST level, so the
    # handlers below are free to filter upwards from there.
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(LINE_FORMAT, datefmt=DATE_FORMAT)

    app_handler = logging.FileHandler(APP_LOG, mode="a", encoding="utf-8")
    app_handler.setLevel(logging.DEBUG)
    app_handler.setFormatter(formatter)

    error_handler = logging.FileHandler(ERROR_LOG, mode="a", encoding="utf-8")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_level)
    console_handler.setFormatter(logging.Formatter("   [%(levelname)s] %(message)s"))

    logger.addHandler(app_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)

    return logger


def get_logger(module_name):
    """Return the child logger for one module, e.g. get_logger("student_ops")."""
    return logging.getLogger(f"{ROOT_NAME}.{module_name}")


def start_run(logger, source):
    """
    Write the banner that separates one run from the previous one.

    Both log files are opened in append mode, so without a marker like
    this a file that has been added to five times reads as one enormous
    confusing run.
    """
    logger.info("=" * 60)
    logger.info("RUN STARTED - source: %s", source)
