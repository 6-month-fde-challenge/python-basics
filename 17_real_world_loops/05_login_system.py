"""
Question 5 - Login System with a Maximum of 3 Attempts
======================================================
Concept: while loop + counter + break.

The loop must stop for TWO different reasons:
   1. the password is correct  -> break out early (SUCCESS)
   2. three attempts are used  -> the while condition becomes False (LOCKED)

This is why a counter is needed. A plain `while True` would let the
user guess forever, which is exactly what a login system must prevent.

TEST CASES TO DEMONSTRATE IN THE VIDEO
   Successful : type  python123  on any attempt
   Failed     : type  a wrong password 3 times -> account locked
"""

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "python123"
MAX_ATTEMPTS = 3

print("=" * 45)
print("        SECURE LOGIN SYSTEM")
print("=" * 45)
print(f"You have a maximum of {MAX_ATTEMPTS} password attempts.")
print()

username = input("Enter username : ")

attempts = 0
logged_in = False

while attempts < MAX_ATTEMPTS:
    password = input(f"Enter password (attempt {attempts + 1} of {MAX_ATTEMPTS}) : ")
    attempts += 1

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        logged_in = True
        break                      # correct -> leave the loop immediately
    else:
        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"   Incorrect. {remaining} attempt(s) remaining.\n")
        else:
            print("   Incorrect. No attempts remaining.\n")

print("=" * 45)
if logged_in:
    print(f"LOGIN SUCCESSFUL. Welcome, {username}!")
    print(f"You logged in on attempt number {attempts}.")
else:
    print("ACCOUNT LOCKED.")
    print(f"All {MAX_ATTEMPTS} attempts were used without a correct password.")
print("=" * 45)
