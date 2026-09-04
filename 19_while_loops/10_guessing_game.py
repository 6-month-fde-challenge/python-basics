"""
Question 10 - Number Guessing Game
===================================
The secret number is predefined. The user keeps guessing until they get
it right, and the program helps by saying "too high" or "too low".

WHY while: the number of guesses depends on how lucky and how logical
the player is. It could be one guess or fifteen. Only a condition can
express "keep going until correct".

The hints turn this into a real algorithm. Guessing halfway each time
(binary search) finds any number from 1 to 100 in at most 7 guesses,
because each guess halves the range that is still possible.

SAMPLE RUN
    Guess: 50   -> Too high
    Guess: 25   -> Too low
    Guess: 37   -> Too low
    Guess: 42   -> CORRECT in 4 guesses
"""

SECRET_NUMBER = 42
LOWEST = 1
HIGHEST = 100

print("=" * 55)
print("NUMBER GUESSING GAME")
print("=" * 55)
print(f"   I am thinking of a number between {LOWEST} and {HIGHEST}.")
print("   Keep guessing - I will tell you if you are too high or too low.")
print()

# INITIALIZATION : no guesses made yet, and nothing guessed correctly yet.
guesses = 0
found = False

# CONDITION : keep playing while the correct number has not been found.
# `found` is the flag that controls the loop.
while not found:
    entry = input("   Your guess : ")

    # Reject bad input without ending the game
    try:
        guess = int(entry)
    except ValueError:
        print(f"      '{entry}' is not a whole number. Try again.")
        continue

    guesses += 1

    if guess < LOWEST or guess > HIGHEST:
        print(f"      That is outside {LOWEST}-{HIGHEST}, but it still counts as a guess.")

    # UPDATE / TERMINATION : `found` becomes True only on a correct guess,
    # which is what makes the condition `not found` False and ends the loop.
    if guess < SECRET_NUMBER:
        print(f"      {guess} is TOO LOW. Guess higher.")
    elif guess > SECRET_NUMBER:
        print(f"      {guess} is TOO HIGH. Guess lower.")
    else:
        found = True

print()
print("=" * 55)
print("   CORRECT!")
print("=" * 55)
print(f"   The number was {SECRET_NUMBER}.")
print(f"   You found it in {guesses} guess(es).")

if guesses == 1:
    print("   First try - remarkable.")
elif guesses <= 7:
    print("   Well within the 7 guesses that halving the range would need.")
else:
    print("   Tip: guess the middle of the remaining range each time.")

print()
print("=" * 55)
print("THE HALVING STRATEGY")
print("=" * 55)
print("""
   Guess the middle of whatever range is still possible:

       1-100  -> guess 50   -> too high -> now 1-49
       1-49   -> guess 25   -> too low  -> now 26-49
       26-49  -> guess 37   -> too low  -> now 38-49
       38-49  -> guess 43   -> too high -> now 38-42
       38-42  -> guess 40   -> too low  -> now 41-42
       41-42  -> guess 41   -> too low  -> must be 42
       -> 42, in 7 guesses at most, for ANY number in 1-100

   Each guess halves the possibilities, which is why 100 numbers need
   only about 7 guesses rather than 100.
""")

print("=" * 55)
print("WHY while AND NOT for")
print("=" * 55)
print("""
   The game ends on a CONDITION (the guess matches), not after a fixed
   number of passes. A for loop would have to pick an arbitrary limit and
   would either stop the player mid-game or keep asking after they had won.
""")
