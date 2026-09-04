"""
Question 2 - Stop at the First Number Divisible by BOTH 7 and 11
=================================================================
Concept: the `break` statement.

`break` ends the ENTIRE loop immediately. Nothing after it runs, and the
loop never continues to the remaining numbers.

Compare with Question 1:
    continue -> skip THIS number, keep looping
    break    -> stop the loop COMPLETELY

"Divisible by both 7 and 11" needs the word AND:
    n % 7 == 0 and n % 11 == 0
A number divisible by both is really a multiple of 7 x 11 = 77,
so the answer inside 1-100 is 77 (the only one).
"""

print("Searching 1 to 100 for the first number divisible by both 7 and 11")
print("=" * 65)

found = None
checked = 0

for n in range(1, 101):
    checked += 1
    if n % 7 == 0 and n % 11 == 0:
        found = n
        print(f"   {n} -> divisible by 7 AND by 11 -> STOP")
        break                        # leave the loop at once
    # only reached when the number does not qualify
    if n % 7 == 0:
        print(f"   {n} -> divisible by 7 only, keep going")
    elif n % 11 == 0:
        print(f"   {n} -> divisible by 11 only, keep going")

print("=" * 65)
print("First number divisible by both :", found)
print("Numbers checked before stopping:", checked)
print("Numbers never examined         :", 100 - checked)
print()
print(f"Proof: {found} / 7  = {found // 7}   (remainder {found % 7})")
print(f"       {found} / 11 = {found // 11}   (remainder {found % 11})")
print()
print("WITHOUT break the loop would have checked all 100 numbers.")
print("break saved", 100 - checked, "unnecessary checks.")
