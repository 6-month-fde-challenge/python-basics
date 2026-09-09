"""
menu.py - the screen, the choices, and the dispatcher
=====================================================
This module knows HOW the user interacts. It knows nothing about
passwords, arithmetic or files - it hands each choice to the module that
does, and makes sure that module's failure never reaches the outer loop.

WHY THE dispatch() TRY/EXCEPT EXISTS
    auth, calculator and file_handler each handle the errors they can
    predict. dispatch() is the net underneath them: if one of those
    modules raises something nobody anticipated, it is logged CRITICAL
    with a traceback and the menu is redrawn. The application does not
    terminate.

That is the requirement "an error in one operation does not terminate
the entire application", implemented in exactly one place.
"""
import auth
import calculator
import file_handler
from logger_config import get_logger

log = get_logger("menu")

LINE = "=" * 56


def show_menu():
    """Print the menu, with the current session in the header."""
    who = auth.current_user if auth.is_logged_in() else "not logged in"
    print()
    print(LINE)
    print(f"   APPLICATION ACTIVITY LOGGER      [ {who} ]")
    print(LINE)
    print("   1. Login")
    print("   2. Calculate")
    print("   3. Read a File")
    print("   4. Write a File")
    print("   5. Logout")
    print("   " + "-" * 50)
    print("   6. Simulate an unexpected failure   (CRITICAL demo)")
    print("   0. Exit")
    print(LINE)


def do_login():
    """Activity 1."""
    username = input("   Username : ").strip()
    password = input("   Password : ").strip()
    if auth.login(username, password):
        print(f"   Welcome, {username}.")
    else:
        print("   Login failed.")


def do_calculate():
    """Activity 2 - protected."""
    if auth.require_login("Calculate"):
        calculator.run()
    else:
        print("   Log in first.")


def do_read():
    """Activity 3 - protected."""
    if auth.require_login("Read a File"):
        file_handler.run_read()
    else:
        print("   Log in first.")


def do_write():
    """Activity 4 - protected."""
    if auth.require_login("Write a File"):
        if file_handler.run_write():
            print("   Saved.")
    else:
        print("   Log in first.")


def do_logout():
    """Activity 5."""
    if auth.logout():
        print("   Logged out.")
    else:
        print("   Nobody is logged in.")


def do_simulated_failure():
    """
    Deliberately raise an exception nothing below expects.

    Every other CRITICAL in this application needs a genuine bug to
    appear. This option makes the fifth log level demonstrable on demand,
    which matters when the log file is the deliverable.
    """
    log.debug("Simulating an unexpected failure on purpose")
    broken = {"a": 1}
    return broken["this key does not exist"]      # KeyError


# Choice -> handler. Same dictionary-dispatch idea as the calculator:
# the routing table IS the menu, so the two can never drift apart.
ACTIONS = {
    "1": ("Login", do_login),
    "2": ("Calculate", do_calculate),
    "3": ("Read a File", do_read),
    "4": ("Write a File", do_write),
    "5": ("Logout", do_logout),
    "6": ("Simulate failure", do_simulated_failure),
}


def dispatch(choice):
    """
    Run one activity. Return False when the application should stop.

    The broad `except Exception` here is normally bad practice - it is
    correct in exactly this position, the top of a menu loop, because the
    alternative is a traceback on screen and a dead application.
    """
    if choice == "0":
        log.info("Exit selected - shutting down")
        return False

    if choice not in ACTIONS:
        log.warning("Invalid menu choice: %r", choice)
        print("   That is not one of the options.")
        return True

    name, action = ACTIONS[choice]
    log.debug("Activity selected: %s", name)

    try:
        action()

    except KeyboardInterrupt:
        # Ctrl+C inside an activity cancels the activity, not the app.
        log.warning("Activity %r cancelled by the user (Ctrl+C)", name)
        print("\n   Cancelled.")

    except Exception:
        # Nothing below handled it, so it is a defect. CRITICAL, with the
        # traceback, and the loop continues.
        log.critical("Unexpected application failure during %r", name,
                     exc_info=True)
        print("   Unexpected application failure - see logs/error.log")

    finally:
        log.debug("Activity %r finished", name)

    return True
