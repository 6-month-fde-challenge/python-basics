"""
Question 11 - Reverse a String Using a for Loop
================================================
The shortcuts text[::-1] and reversed() are NOT used, because they
bypass the technique being practised.

THE TECHNIQUE: build a new string by putting each character in FRONT
of what has been collected so far.

    reversed_text = char + reversed_text

Read that line carefully. Because the new character goes FIRST and the
existing text goes AFTER, every character pushes the previous ones to
the right - which reverses the order.

Walking through "cat":
    start           reversed_text = ""
    char 'c'  ->    "c" + ""    = "c"
    char 'a'  ->    "a" + "c"   = "ac"
    char 't'  ->    "t" + "ac"  = "tac"

Sample input : Python
Sample output: nohtyP
"""

text = "Python"

print("=" * 50)
print("METHOD 1 - build the string backwards")
print("=" * 50)
print("Original :", text)
print()

reversed_text = ""

print("Building the reversed string one character at a time:")
for char in text:
    reversed_text = char + reversed_text        # new char goes in FRONT
    print(f"   took '{char}'  ->  reversed_text is now '{reversed_text}'")

print()
print("Original :", text)
print("Reversed :", reversed_text)
print()

# --- Method 2: walk the string backwards by index --------------------------
print("=" * 50)
print("METHOD 2 - walk backwards using indexes")
print("=" * 50)
print("range(len(text) - 1, -1, -1) counts down through the positions:")
print("   ", list(range(len(text) - 1, -1, -1)))
print()

reversed_2 = ""
for i in range(len(text) - 1, -1, -1):          # last index down to 0
    reversed_2 += text[i]
    print(f"   index {i} holds '{text[i]}'  ->  '{reversed_2}'")

print()
print("Reversed :", reversed_2)
print("Both methods agree :", reversed_text == reversed_2)
print()
print("NOTE on the stop value: it is -1, not 0. range() excludes its stop,")
print("so stopping at 0 would miss index 0 - the first character.")
print()

# --- Try it on your own input ----------------------------------------------
print("=" * 50)
print("TRY YOUR OWN")
print("=" * 50)

user_text = input("Enter a string to reverse : ")

result = ""
for char in user_text:
    result = char + result

print("Original :", user_text)
print("Reversed :", result)

# A small bonus: a reversed string is how you check for a palindrome
if result.lower() == user_text.lower():
    print("Interesting - that string is a PALINDROME (same both ways).")
