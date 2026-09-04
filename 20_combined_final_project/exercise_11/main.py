"""
Exercise 11 - Mini Authentication System
========================================
A small login application with a predefined user, an attempt limit, a
logged-in session, logout, and retry logic.

FUNCTIONS
    verify_credentials()  - check a username and password pair
    attempt_login()       - the login loop, capped at MAX_ATTEMPTS
    show_dashboard()      - the menu shown only to a logged-in user
    logout()              - end the session and return to the login screen
    main()                - the outer loop allowing a retry after logout

TWO NESTED LOOPS, EACH WITH A DIFFERENT JOB
    OUTER while - keeps the application alive across logins and logouts,
                  so a user can log out and someone else can log in
    INNER while - the login attempts, which must stop after 3 tries

THE ATTEMPT LOOP HAS TWO EXITS
    success  -> break out immediately, without using the remaining tries
    3 failures -> the condition `attempts < MAX_ATTEMPTS` becomes False

A plain `while True` would let someone guess forever, which is exactly
what an authentication system must prevent.

SAMPLE INPUT / OUTPUT
    Username: admin   Password: wrong      -> Incorrect. 2 attempts left.
    Username: admin   Password: python123  -> LOGIN SUCCESSFUL (attempt 2)
    Dashboard -> option 3 -> Logged out
    Retry? n -> Application closed
"""

# Predefined credentials
USERS = {
    "admin": "python123",
    "rahul": "learner2026",
}

MAX_ATTEMPTS = 3


def verify_credentials(username, password):
    """Return True if the username exists and the password matches it."""
    if username not in USERS:
        return False
    return USERS[username] == password


def attempt_login():
    """
    Run the login process, allowing at most MAX_ATTEMPTS tries.

    Returns the username on success, or None when every attempt is used.
    """
    print()
    print("=" * 48)
    print("                 LOGIN")
    print("=" * 48)
    print(f"   You have {MAX_ATTEMPTS} attempts.")
    print()

    # INITIALIZATION : no attempts used yet
    attempts = 0

    # CONDITION : keep trying while attempts remain.
    # This is the FIRST of the two ways out of the loop.
    while attempts < MAX_ATTEMPTS:
        username = input("   Username : ").strip()
        password = input("   Password : ").strip()

        # UPDATE / TERMINATION : every try consumes one attempt, so the
        # condition above must eventually become False.
        attempts += 1

        if verify_credentials(username, password):
            print()
            print(f"   LOGIN SUCCESSFUL on attempt {attempts}.")
            # The SECOND way out - return immediately, leaving any
            # remaining attempts unused.
            return username

        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"   Incorrect username or password. "
                  f"{remaining} attempt(s) remaining.")
            print()
        else:
            print("   Incorrect username or password. No attempts remaining.")

    # Reached only when the loop ran out of attempts
    print()
    print("=" * 48)
    print("   ACCESS DENIED - account locked for this session.")
    print("=" * 48)
    return None


def show_dashboard(username):
    """
    Show the menu available to a logged-in user.

    Returns "logout" when the user logs out, or "exit" to close the
    application entirely.
    """
    # INITIALIZATION
    in_session = True

    # CONDITION : stay on the dashboard until the user logs out or exits
    while in_session:
        print()
        print("=" * 48)
        print(f"        DASHBOARD - logged in as {username}")
        print("=" * 48)
        print("   1. View profile")
        print("   2. Change password (demo)")
        print("   3. Logout")
        print("   4. Exit application")
        print("=" * 48)

        choice = input("   Choose an option (1-4) : ").strip()

        if choice == "1":
            print()
            print("   USER PROFILE")
            print("   " + "-" * 32)
            print(f"   Username : {username}")
            print(f"   Role     : {'Administrator' if username == 'admin' else 'Standard user'}")
            print(f"   Status   : Active session")

        elif choice == "2":
            new_password = input("   Enter a new password : ").strip()
            if len(new_password) < 6:
                print("      ERROR: the password must be at least 6 characters.")
            else:
                USERS[username] = new_password
                print(f"   SUCCESS: password updated for {username}.")
                print("   (This change lasts only while the program is running.)")

        elif choice == "3":
            # UPDATE / TERMINATION for the dashboard loop
            in_session = False
            print()
            print(f"   {username} has been logged out.")
            return "logout"

        elif choice == "4":
            in_session = False
            return "exit"

        else:
            print()
            print(f"   INVALID OPTION: '{choice}'. Please choose 1 to 4.")

    return "logout"


def main():
    """Run the authentication system, allowing retries after logout."""
    print("=" * 48)
    print("           MINI AUTHENTICATION SYSTEM")
    print("=" * 48)
    print("   Valid accounts for this demo:")
    for username in USERS:
        print(f"      {username}")
    print("   (Password for admin is 'python123')")

    # INITIALIZATION : the outer application flag
    application_running = True

    # CONDITION : the OUTER loop keeps the application alive across sessions,
    # so a user can log out and another can log in without restarting.
    while application_running:
        username = attempt_login()

        if username is None:
            # Login failed after every attempt - offer a retry
            retry = input("   Try logging in again? (y/n) : ").strip().lower()
            if retry != "y":
                # UPDATE / TERMINATION for the outer loop
                application_running = False
                print()
                print("   Application closed.")
            continue

        # Login succeeded, so hand control to the dashboard
        result = show_dashboard(username)

        if result == "exit":
            application_running = False
            print()
            print("   Application closed. Goodbye!")
        else:
            # Logged out - ask whether anyone else wants to log in
            again = input("   Log in as another user? (y/n) : ").strip().lower()
            if again != "y":
                application_running = False
                print()
                print("   Application closed. Goodbye!")


if __name__ == "__main__":
    main()
