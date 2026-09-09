"""
main.py - the entry point, and nothing else
===========================================
The assignment asks for the application to be split across modules
"instead of writing everything in main.py". So this file does three
things and stops:

    1. configure logging      (logger_config)
    2. run the menu loop      (menu)
    3. log the shutdown

FIVE MODULES, FIVE JOBS
    logger_config.py   where log records go
    auth.py            Login / Logout, and the session
    calculator.py      Calculate
    file_handler.py    Read a File / Write a File
    menu.py            the screen and the dispatcher

RUN IT
    python main.py

WHERE THE LOGS GO
    logs/application.log   every level, DEBUG upwards
    logs/error.log         ERROR and CRITICAL only
"""
import logging

import auth
import menu
from logger_config import setup_logging

# Configure logging BEFORE anything logs. The modules imported above only
# call get_logger() at import time - they do not emit records yet - so
# the ordering works, but this call still belongs at the very top.
log = setup_logging(console_level=logging.WARNING)


def main():
    """Run the menu until the user chooses 0, then shut down cleanly."""
    log.info("Application started")

    running = True
    try:
        while running:
            menu.show_menu()
            try:
                choice = input("   Choose an activity : ").strip()
            except EOFError:
                # stdin ran out - happens when input is piped from a file
                log.warning("Input stream ended, shutting down")
                break

            running = menu.dispatch(choice)

    except KeyboardInterrupt:
        # Ctrl+C at the menu prompt itself ends the application, and is
        # recorded rather than crashing out with a traceback.
        log.warning("Application interrupted by the user (Ctrl+C)")
        print("\n   Interrupted.")

    except Exception:
        # The last net. If even the dispatcher's own handling fails, the
        # application still exits with a logged reason.
        log.critical("Unexpected application failure in the main loop",
                     exc_info=True)
        print("   Fatal error - see logs/error.log")

    finally:
        # Runs on every route out: normal exit, Ctrl+C, or fatal error.
        # A log with a start line and no stop line means a crash, so this
        # line is worth guaranteeing.
        if auth.is_logged_in():
            log.warning("Shutting down with %r still logged in",
                        auth.current_user)
        log.info("Application stopped")
        print("\n   Goodbye. Logs written to logs/")


if __name__ == "__main__":
    main()
