"""
logger_config.py - one place that decides where log messages go
===============================================================
Every other module in this application asks THIS module for a logger.
Nothing else touches `logging.basicConfig`, opens a log file, or decides
a format. That is the whole point of a configuration module: the wiring
lives in one file, so changing it changes the entire application.

THE FIVE LEVELS, FROM QUIETEST TO LOUDEST
    DEBUG    10  detail only a developer wants  (values, arguments, flow)
    INFO     20  something normal happened      (user logged in)
    WARNING  30  odd, but the app carries on    (file was empty)
    ERROR    40  this operation failed          (file could not be opened)
    CRITICAL 50  the application itself is hurt (unexpected failure)

THREE DESTINATIONS, EACH WITH ITS OWN THRESHOLD
    logs/application.log   DEBUG and above  - the full story
    logs/error.log         ERROR and above  - only what went wrong
    the console            WARNING and above - so the menu stays readable

A handler never sees a record its LOGGER blocked first, so the logger is
set to DEBUG (the lowest) and each handler filters down from there. Set
the logger to INFO and no handler would ever receive a DEBUG record, no
matter what the handler's own level says.
"""
import logging
import os
import sys

# logs/ sits next to this file, not next to whatever directory the user
# happened to run `python main.py` from. __file__ makes that reliable.
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")

APP_LOG = os.path.join(LOG_DIR, "application.log")
ERROR_LOG = os.path.join(LOG_DIR, "error.log")

# asctime  - when            levelname - how serious
# name     - which module    funcName:lineno - exactly where
LINE_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)-14s | %(funcName)s:%(lineno)-3d | %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# The one parent logger. Every module logger is a child of it ("app.auth",
# "app.calculator", ...) and records travel UP to the parent's handlers,
# so the handlers are attached here exactly once.
ROOT_NAME = "app"


def setup_logging(console_level=logging.WARNING):
    """
    Attach the three handlers to the "app" logger and return it.

    Safe to call more than once: if the handlers are already attached the
    function returns immediately. Without that guard, a second call would
    add a second copy of every handler and each message would be written
    twice.
    """
    logger = logging.getLogger(ROOT_NAME)

    if logger.handlers:            # already configured
        return logger

    os.makedirs(LOG_DIR, exist_ok=True)

    # The logger's own level is the first gate. DEBUG = let everything past
    # and leave the filtering to the handlers.
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(LINE_FORMAT, datefmt=DATE_FORMAT)

    # 1. The full log - every level, appended across runs
    app_handler = logging.FileHandler(APP_LOG, mode="a", encoding="utf-8")
    app_handler.setLevel(logging.DEBUG)
    app_handler.setFormatter(formatter)

    # 2. The problem log - ERROR and CRITICAL only, so it stays short
    #    enough to actually read
    error_handler = logging.FileHandler(ERROR_LOG, mode="a", encoding="utf-8")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    # 3. The console - warnings and worse, in a shorter format, because
    #    timestamps and line numbers are noise while using a menu
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_level)
    console_handler.setFormatter(logging.Formatter("   [%(levelname)s] %(message)s"))

    logger.addHandler(app_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)

    logger.debug("Logging configured -> %s and %s",
                 os.path.relpath(APP_LOG, os.path.dirname(LOG_DIR)),
                 os.path.relpath(ERROR_LOG, os.path.dirname(LOG_DIR)))
    return logger


def get_logger(module_name):
    """
    Return the child logger for one module, e.g. get_logger("auth").

    The dot in "app.auth" is what makes it a child: it inherits the
    parent's handlers and level, so this function never configures
    anything itself. The name is what prints in the `name` column, which
    is how a log line tells you which module produced it.
    """
    return logging.getLogger(f"{ROOT_NAME}.{module_name}")
