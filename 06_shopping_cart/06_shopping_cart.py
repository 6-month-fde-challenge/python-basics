"""
Exercise 06 - Shopping Cart Using a Python List
===============================================
Concepts practised: append(), extend(), insert(), remove(), pop(),
                    index(), count(), copy(), reverse(), sort(), clear()

IMPORTANT: unlike strings, LIST METHODS CHANGE THE LIST ITSELF (in place)
and return None. That is why we write   cart.sort()   and NOT   cart = cart.sort()
The cart is printed after every step so you can watch it change.
"""

# ---------------------------------------------------------------------------
# Create the shopping cart
# ---------------------------------------------------------------------------

cart = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]


# ---------------------------------------------------------------------------
# 1. Display all products
# ---------------------------------------------------------------------------
print("1.  All products        :", cart)
print("    Total products      :", len(cart))
print()


# ---------------------------------------------------------------------------
# 2. Access the first and the last product
# ---------------------------------------------------------------------------
print("2.  First product [0]   :", cart[0])
print("    Last product  [-1]  :", cart[-1])
print()


# ---------------------------------------------------------------------------
# 3. append("Webcam") - adds ONE item to the END
# ---------------------------------------------------------------------------
cart.append("Webcam")
print("3.  After append('Webcam')        :", cart)


# ---------------------------------------------------------------------------
# 4. insert("USB Hub" at index 2) - adds at a CHOSEN position,
#    everything from index 2 onwards shifts one place to the right
# ---------------------------------------------------------------------------
cart.insert(2, "USB Hub")
print("4.  After insert(2, 'USB Hub')    :", cart)


# ---------------------------------------------------------------------------
# 5. remove("Mouse") - deletes BY VALUE (you say WHAT to remove)
#    Only the FIRST match is removed. Missing value -> ValueError.
# ---------------------------------------------------------------------------
cart.remove("Mouse")
print("5.  After remove('Mouse')         :", cart)


# ---------------------------------------------------------------------------
# 6. pop() - deletes BY POSITION (you say WHERE), default is the last item.
#    pop() also RETURNS the removed item, so we can use it.
# ---------------------------------------------------------------------------
removed_item = cart.pop()
print("6.  pop() removed and returned    :", removed_item)
print("    Cart after pop()              :", cart)
print()


# ---------------------------------------------------------------------------
# 7. index("Monitor") - the CURRENT position of Monitor.
#    It happens to still be 3: insert() pushed Monitor one place right,
#    then remove('Mouse') pulled it one place back left. Coincidence,
#    not a rule - index() always reports the position RIGHT NOW.
# ---------------------------------------------------------------------------
print("7.  Index of 'Monitor'  :", cart.index("Monitor"))


# ---------------------------------------------------------------------------
# 8. count("Laptop") - how many times it appears
# ---------------------------------------------------------------------------
print("8.  Count of 'Laptop'   :", cart.count("Laptop"))
print()


# ---------------------------------------------------------------------------
# 9. copy() - make an INDEPENDENT duplicate.
#    cart_copy = cart would NOT copy - both names would point to the SAME list.
# ---------------------------------------------------------------------------
cart_copy = cart.copy()
print("9.  Original cart       :", cart)
print("    Copy of the cart    :", cart_copy)
print("    Same object in memory? ", cart is cart_copy, "<- False means truly independent")
print()


# ---------------------------------------------------------------------------
# 10. reverse() - flips the current order back to front (does NOT sort)
# ---------------------------------------------------------------------------
cart.reverse()
print("10. After reverse()     :", cart)


# ---------------------------------------------------------------------------
# 11. sort() - arranges alphabetically (A-Z) in place
# ---------------------------------------------------------------------------
cart.sort()
print("11. After sort()        :", cart)
print("    sort(reverse=True)  :", end=" ")
cart.sort(reverse=True)
print(cart, "<- Z to A")
cart.sort()   # put it back in A-Z order


# ===========================================================================
# BONUS DEMOS - the two methods not used above: extend() and clear()
# ===========================================================================

print()
print("=" * 62)
print("BONUS : append() vs extend()  |  and clear()")
print("=" * 62)

# --- append() vs extend() : a common point of confusion --------------------
demo_a = ["Laptop", "Mouse"]
demo_b = ["Laptop", "Mouse"]
new_items = ["Cable", "Charger"]

demo_a.append(new_items)    # adds the LIST as ONE single item -> nested list
demo_b.extend(new_items)    # adds each item SEPARATELY -> flat list

print("append(['Cable','Charger']) ->", demo_a, "| length:", len(demo_a))
print("extend(['Cable','Charger']) ->", demo_b, "| length:", len(demo_b))
print("append added 1 item (a list inside a list); extend added 2 separate items.")
print()

# --- clear() : empties a list but the list still exists --------------------
print("clear() demo on our copy:")
print("   cart_copy before clear() :", cart_copy, "| length:", len(cart_copy))
cart_copy.clear()
print("   cart_copy after  clear() :", cart_copy, "| length:", len(cart_copy))
print("   Original cart untouched  :", cart, "<- proves copy() was independent")
