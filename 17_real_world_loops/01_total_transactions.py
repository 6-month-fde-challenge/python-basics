"""
Question 1 - Total Transaction Value WITHOUT sum()
==================================================
Concept: accumulator pattern.

An ACCUMULATOR is a variable that starts at 0 and grows inside a loop.
This is exactly what sum() does internally - we are writing it by hand.
"""

transactions = [1200, 450, 800, 1500, 2300, 700, 100]

print("Transactions :", transactions)
print("Count        :", len(transactions))
print()

# Step 1: start the accumulator at 0 (NOT inside the loop - it would reset)
total = 0

# Step 2: visit every transaction and add it to the running total
print("Adding them one by one:")
for amount in transactions:
    total = total + amount          # same as: total += amount
    print(f"   + {amount:<6} -> running total = {total}")

print()
print("TOTAL TRANSACTION VALUE : Rs.", total)

# Verification (sum() is only used here to PROVE the loop is correct)
print("Check with sum()        : Rs.", sum(transactions), "-> match:", total == sum(transactions))
