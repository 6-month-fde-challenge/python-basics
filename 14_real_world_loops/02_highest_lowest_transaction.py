"""
Question 2 - Highest and Lowest Transaction WITHOUT max() and min()
===================================================================
Concept: "champion" pattern.

Assume the FIRST item is the winner, then challenge it against every
other item. Whenever something beats the champion, it becomes the champion.

IMPORTANT: start with transactions[0], NOT with 0.
Starting the lowest at 0 would be a bug - no positive amount is below 0,
so the answer would always come out as 0.
"""

transactions = [1200, 450, 800, 1500, 2300, 700, 100]

print("Transactions :", transactions)
print()

# Step 1: assume the first transaction is both the highest and the lowest
highest = transactions[0]
lowest = transactions[0]
print(f"Starting assumption: highest = {highest}, lowest = {lowest}")
print()

# Step 2: challenge the champion against every remaining transaction
print("Comparing each transaction:")
for amount in transactions:
    if amount > highest:
        print(f"   {amount} beats {highest} -> new HIGHEST")
        highest = amount
    elif amount < lowest:
        print(f"   {amount} is below {lowest} -> new LOWEST")
        lowest = amount
    else:
        print(f"   {amount} changes nothing")

print()
print("HIGHEST transaction : Rs.", highest)
print("LOWEST  transaction : Rs.", lowest)
print("Difference (range)  : Rs.", highest - lowest)

# Verification
print()
print("Check with max()/min() :", max(transactions), "/", min(transactions),
      "-> match:", highest == max(transactions) and lowest == min(transactions))
