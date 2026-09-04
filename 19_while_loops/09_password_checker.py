"""
Question 9 - Keep Asking for the Password Until It Is Correct
==============================================================
ANOTHER CASE WHERE for CANNOT WORK.

The loop must run until a condition is met - the correct password is
typed. That might take one attempt or twenty. A for loop would have to
guess a number of attempts in advance and would either cut the user off
too early or keep asking after they had already succeeded.

SAMPLE RUN
    Enter password: hello      -> Incorrect. Try again.
    Enter password: python     -> Incorrect. Try again.
    Enter password: python123  -> ACCESS GRANTED (attempt 3)

NOTE: this version has NO attempt limit - it keeps asking until the
password is right. A version WITH a limit is
shown at the end, because unlimited attempts is a real security problem.
"""

CORRECT_PASSWORD = "python123"

print("=" * 55)
print("PASSWORD CHECKER")
print("=" * 55)
print("(The password is 'python123' - it is printed here only so the")
print(" program can be demonstrated.)")
print()

# INITIALIZATION : no attempts made yet, and no password entered yet.
# `entered` starts as an empty string so it cannot accidentally match.
attempts = 0
entered = ""

# CONDITION : keep asking while the entered password is still wrong.
# The FIRST check is against "" which never matches, so the loop always
# runs at least once.
while entered != CORRECT_PASSWORD:
    entered = input("   Enter password : ")
    attempts += 1

    # UPDATE / TERMINATION : the loop ends the moment `entered` matches
    # CORRECT_PASSWORD, because the condition at the top then becomes False.
    if entered != CORRECT_PASSWORD:
        print(f"      Incorrect. Attempt {attempts} failed. Try again.")

print()
print("=" * 55)
print("   ACCESS GRANTED")
print("=" * 55)
print(f"   Correct password entered on attempt {attempts}.")
print()

# --- The same idea, but with a limit ---------------------------------------
print("=" * 55)
print("A SAFER VERSION - WITH AN ATTEMPT LIMIT")
print("=" * 55)
print("""
   MAX_ATTEMPTS = 3

   # INITIALIZATION
   attempts = 0
   logged_in = False

   # CONDITION : two ways to leave - success, or running out of attempts
   while attempts < MAX_ATTEMPTS and not logged_in:
       entered = input("Password: ")
       attempts += 1              # UPDATE - guarantees termination
       if entered == CORRECT_PASSWORD:
           logged_in = True

   Unlimited attempts let someone guess forever, so real login systems
   always cap them. The version above deliberately loops until the
   password is correct, to show the unbounded form first.
""")

print("=" * 55)
print("WHY while AND NOT for")
print("=" * 55)
print("""
   for attempt in range(5):     <- why 5? The number is arbitrary.

   The loop must end when a CONDITION is met (the password matches), not
   after a fixed count. The number of passes depends entirely on how many
   times the user gets it wrong, which is unknowable in advance.
""")
