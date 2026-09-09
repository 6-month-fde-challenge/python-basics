"""
auth.py - the Login and Logout activities
=========================================
Holds the session state (who is logged in) and the two activities that
change it. Every path through this module produces a log record, because
"who was using the application, and when" is the first question anyone
asks of an activity log.

WHICH LEVEL FOR WHICH EVENT
    DEBUG    the username being checked            (developer detail)
    INFO     a successful login or logout          (normal activity)
    WARNING  a wrong password, or logging out
             when nobody is logged in              (odd, not fatal)

A wrong password is deliberately WARNING and not ERROR. Nothing broke -
the application did exactly what it should. ERROR is reserved for an
operation that could not be completed at all.
"""
from logger_config import get_logger

log = get_logger("auth")

# A tiny in-memory user store. A real application would query a database;
# the logging behaviour would be identical.
USERS = {
    "admin": "python123",
    "rahul": "learner2026",
}

# Module-level session state. `current_user` is None when nobody is
# logged in, and holds the username otherwise.
current_user = None


def is_logged_in():
    """Return True when a session is open."""
    return current_user is not None


def login(username, password):
    """
    Try to open a session. Return True on success, False otherwise.

    Note the two failure branches log DIFFERENT messages - "unknown user"
    and "wrong password". A log that says only "login failed" cannot tell
    you whether someone mistyped their own password or is guessing at
    accounts that do not exist.
    """
    global current_user

    log.debug("Login attempt for username=%r", username)

    if is_logged_in():
        log.warning("Login refused: %r is already logged in", current_user)
        return False

    if not username:
        log.warning("Login refused: empty username submitted")
        return False

    if username not in USERS:
        log.warning("Login failed: unknown user %r", username)
        return False

    if USERS[username] != password:
        log.warning("Login failed: wrong password for %r", username)
        return False

    current_user = username
    log.info("User logged in: %s", username)
    return True


def logout():
    """
    Close the session. Return True if there was one to close.

    Logging out when nobody is logged in is not an error - it is a user
    pressing 5 twice. WARNING records it without pretending the
    application failed.
    """
    global current_user

    if not is_logged_in():
        log.warning("Logout requested but no user is logged in")
        return False

    log.info("User logged out: %s", current_user)
    log.debug("Session cleared, current_user set back to None")
    current_user = None
    return True


def require_login(activity):
    """
    Guard used by the menu before Calculate, Read and Write.

    Returns True when the activity may proceed. When it may not, the
    refusal is logged as WARNING - an unauthenticated user reaching for a
    protected activity is exactly the kind of thing an activity log
    exists to record.
    """
    if is_logged_in():
        return True
    log.warning("Activity %r blocked: no user is logged in", activity)
    return False
