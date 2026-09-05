"""
Question 8 - Print Every Language With Its Length
==================================================
Concept: looping over a list of STRINGS and using len() on each item.

len() counts characters when given a string, and counts items when
given a list. The same function answers two different questions
depending on what you hand it.

Sample output: Python -> 6 characters
               Java -> 4 characters
               ...
"""

languages = ["Python", "Java", "C++", "JavaScript", "Go"]

print("Languages :", languages)
print("How many  :", len(languages), "<- len() on a LIST counts the items")
print()

print("=" * 45)
print("EACH LANGUAGE AND ITS LENGTH")
print("=" * 45)

for language in languages:
    print(f"   {language:<12} -> {len(language)} characters")

print()

# --- Numbered, using enumerate ---------------------------------------------
print("=" * 45)
print("THE SAME LIST, NUMBERED")
print("=" * 45)

for position, language in enumerate(languages, start=1):
    print(f"   {position}. {language:<12} ({len(language)} characters)")

print()

# --- Finding the longest and shortest without max() or min() ---------------
print("=" * 45)
print("LONGEST AND SHORTEST")
print("=" * 45)

longest = languages[0]
shortest = languages[0]

for language in languages:
    if len(language) > len(longest):
        longest = language
    if len(language) < len(shortest):
        shortest = language

print("Longest name  :", longest, f"({len(longest)} characters)")
print("Shortest name :", shortest, f"({len(shortest)} characters)")

total_characters = 0
for language in languages:
    total_characters += len(language)

print("Total characters across all names :", total_characters)
print("Average name length               :", round(total_characters / len(languages), 2))
print()

# --- len() on a string vs len() on a list ----------------------------------
print("len() answers two different questions:")
print("   len(languages)      =", len(languages), "  <- number of ITEMS in the list")
print("   len(languages[0])   =", len(languages[0]), "  <- number of CHARACTERS in 'Python'")
