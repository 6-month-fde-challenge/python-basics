"""
Question 6 - Print Only Products Costing More Than Rs.2000
===========================================================
Concept: looping over a dictionary with .items() + a filter condition.

.items() gives BOTH the key and the value on each pass, so the loop
variable list has two names:  for name, price in products.items()

WATCH THE BOUNDARY: "more than 2000" means  price > 2000, NOT >= 2000.
Headphones cost exactly 2000, so they are EXCLUDED. Using >= by mistake
would wrongly include them - this is the classic off-by-one trap.
"""

products = {
    "Laptop": 55000,
    "Phone": 30000,
    "Headphones": 2000,
    "Mouse": 700,
    "Keyboard": 1500
}

print("All products in the catalogue:")
for name, price in products.items():
    print(f"   {name:<12} Rs.{price}")
print()

print("=" * 42)
print("PRODUCTS COSTING MORE THAN Rs.2000")
print("=" * 42)

found = 0
for name, price in products.items():
    if price > 2000:
        print(f"   {name:<12} Rs.{price}")
        found += 1

print("-" * 42)
print(f"{found} product(s) matched out of {len(products)}.")
print()

# Show the decision made for every product, including the boundary case
print("Why each product was included or excluded:")
for name, price in products.items():
    decision = "INCLUDED" if price > 2000 else "excluded"
    print(f"   {name:<12} Rs.{price:<6} {price} > 2000 is {price > 2000}  -> {decision}")

print()
print("NOTE: Headphones cost EXACTLY 2000. 'More than 2000' excludes them.")
