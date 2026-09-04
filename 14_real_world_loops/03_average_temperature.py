"""
Question 3 - Average Temperature
================================
Concept: accumulator + division.

AVERAGE = TOTAL of all values / HOW MANY values there are.
The loop finds the total; len() gives the count.
"""

temperatures = [32, 35, 28, 40, 38, 31, 42]

print("Temperatures :", temperatures)
print("Readings     :", len(temperatures))
print()

# Step 1: add every temperature using an accumulator
total = 0
count = 0                            # counted manually to show what len() does

for temp in temperatures:
    total += temp
    count += 1
    print(f"   Day {count}: {temp} degrees -> running total = {total}")

# Step 2: divide the total by the number of readings
average = total / count

print()
print("Total of all temperatures :", total)
print("Number of readings        :", count)
print("AVERAGE TEMPERATURE       :", average)
print("Rounded to 2 decimals     :", round(average, 2), "degrees")
print()

# A useful extra: how many days were above average
above = 0
below = 0
for temp in temperatures:
    if temp > average:
        above += 1
    else:
        below += 1

print("Days ABOVE average :", above)
print("Days BELOW average :", below)
