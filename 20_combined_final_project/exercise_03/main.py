"""
Exercise 03 - Inventory Management
==================================
Maintains a list of products, each holding a name, price and quantity.

    1. Add product          2. Display all products
    3. Search product       4. Update quantity
    5. Total inventory value               6. Exit

DATA STRUCTURE
A list of dictionaries - the standard shape for tabular data:

    inventory = [
        {"name": "Laptop", "price": 55000.0, "quantity": 4},
        ...
    ]

FUNCTIONS
    add_product()            - append a new product after validation
    display_products()       - print the inventory as a table
    search_product()         - find products by a partial, case-insensitive name
    update_quantity()        - change the stock level of one product
    calculate_total_value()  - price x quantity summed over every product
    main()                   - the while loop driving the menu

ERROR HANDLING
    rejects blank names, non-numeric prices and quantities, negative values,
    and duplicate product names; reports clearly when a search finds nothing.

SAMPLE INPUT / OUTPUT
    Option 2 -> Laptop 55000.00 x 4 = 220000.00
                Mouse    700.00 x 20 =  14000.00
    Option 5 -> TOTAL INVENTORY VALUE : Rs.328500.00
"""

# Each product is a dictionary; the inventory is a list of them
inventory = [
    {"name": "Laptop", "price": 55000.0, "quantity": 4},
    {"name": "Mouse", "price": 700.0, "quantity": 20},
    {"name": "Keyboard", "price": 1500.0, "quantity": 15},
    {"name": "Monitor", "price": 12000.0, "quantity": 6},
]


def show_menu():
    """Display the inventory menu."""
    print()
    print("=" * 50)
    print("           INVENTORY MANAGEMENT")
    print("=" * 50)
    print(f"   Products on record : {len(inventory)}")
    print("   " + "-" * 44)
    print("   1. Add product")
    print("   2. Display all products")
    print("   3. Search product")
    print("   4. Update quantity")
    print("   5. Calculate total inventory value")
    print("   6. Exit")
    print("=" * 50)


def find_product(name):
    """Return the product dictionary with this exact name, or None."""
    for product in inventory:
        if product["name"].lower() == name.lower():
            return product
    return None


def get_positive_number(prompt, allow_zero=False, whole_number=False):
    """
    Ask for a number and return it, or None if the input is invalid.

    allow_zero    - accept 0 as a valid value
    whole_number  - require an integer rather than a decimal
    """
    entry = input(prompt)

    try:
        value = int(entry) if whole_number else float(entry)
    except ValueError:
        kind = "whole number" if whole_number else "number"
        print(f"      ERROR: '{entry}' is not a valid {kind}.")
        return None

    if value < 0:
        print("      ERROR: the value cannot be negative.")
        return None

    if value == 0 and not allow_zero:
        print("      ERROR: the value must be greater than zero.")
        return None

    return value


def add_product():
    """Add a new product to the inventory after validating every field."""
    name = input("   Product name : ").strip()

    if name == "":
        print("      ERROR: the product name cannot be blank.")
        return

    if find_product(name) is not None:
        print(f"      ERROR: '{name}' is already in the inventory.")
        print("      Use option 4 to change its quantity instead.")
        return

    price = get_positive_number("   Price        : Rs.")
    if price is None:
        return

    quantity = get_positive_number("   Quantity     : ", allow_zero=True, whole_number=True)
    if quantity is None:
        return

    inventory.append({"name": name, "price": price, "quantity": quantity})
    print()
    print(f"   SUCCESS: '{name}' added.")
    print(f"   {quantity} unit(s) at Rs.{price:.2f} = Rs.{price * quantity:.2f}")


def display_products():
    """Print every product as an aligned table."""
    print()
    print("   CURRENT INVENTORY")
    print("   " + "-" * 56)

    if len(inventory) == 0:
        print("   The inventory is empty.")
        print("   " + "-" * 56)
        return

    print(f"   {'#':<4}{'PRODUCT':<18}{'PRICE':>12}{'QTY':>6}{'VALUE':>14}")
    print("   " + "-" * 56)

    for index, product in enumerate(inventory, start=1):
        value = product["price"] * product["quantity"]
        print(f"   {index:<4}{product['name']:<18}"
              f"{product['price']:>12.2f}{product['quantity']:>6}{value:>14.2f}")

    print("   " + "-" * 56)
    print(f"   {len(inventory)} product(s)"
          f"{'TOTAL: Rs.' + format(calculate_total_value(), '.2f'):>42}")


def search_product():
    """Search for products whose name contains the text entered."""
    term = input("   Search for : ").strip()

    if term == "":
        print("      ERROR: please enter something to search for.")
        return

    matches = []
    for product in inventory:
        if term.lower() in product["name"].lower():
            matches.append(product)

    print()
    if len(matches) == 0:
        print(f"   No product matching '{term}' was found.")
        return

    print(f"   Found {len(matches)} match(es) for '{term}':")
    print("   " + "-" * 50)
    for product in matches:
        value = product["price"] * product["quantity"]
        stock = "IN STOCK" if product["quantity"] > 0 else "OUT OF STOCK"
        print(f"   {product['name']:<18} Rs.{product['price']:>10.2f}"
              f" x {product['quantity']:<4} = Rs.{value:>10.2f}   {stock}")
    print("   " + "-" * 50)


def update_quantity():
    """Change the stock level of an existing product."""
    name = input("   Product to update : ").strip()
    product = find_product(name)

    if product is None:
        print(f"      ERROR: '{name}' is not in the inventory.")
        return

    print(f"   Current quantity of {product['name']} : {product['quantity']}")
    new_quantity = get_positive_number("   New quantity      : ",
                                       allow_zero=True, whole_number=True)
    if new_quantity is None:
        return

    old_quantity = product["quantity"]
    product["quantity"] = new_quantity

    print()
    print(f"   SUCCESS: {product['name']} updated from {old_quantity} to {new_quantity}.")
    print(f"   New line value: Rs.{product['price'] * new_quantity:.2f}")


def calculate_total_value():
    """Return the total value of the whole inventory, without using sum()."""
    total = 0.0
    for product in inventory:
        total += product["price"] * product["quantity"]
    return total


def show_total_value():
    """Display the total inventory value with a per-product breakdown."""
    print()
    print("   INVENTORY VALUATION")
    print("   " + "-" * 46)

    if len(inventory) == 0:
        print("   The inventory is empty, so the total value is Rs.0.00")
        return

    for product in inventory:
        value = product["price"] * product["quantity"]
        print(f"   {product['name']:<18} {product['price']:>10.2f} x {product['quantity']:<4}"
              f" = Rs.{value:>12.2f}")

    print("   " + "-" * 46)
    print(f"   TOTAL INVENTORY VALUE : Rs.{calculate_total_value():.2f}")


def main():
    """Run the inventory management menu until the user exits."""
    print("Inventory Management System starting...")

    # INITIALIZATION
    running = True

    # CONDITION : keep the application open until Exit is chosen
    while running:
        show_menu()
        choice = input("   Choose an option (1-6) : ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_quantity()
        elif choice == "5":
            show_total_value()
        elif choice == "6":
            # UPDATE / TERMINATION
            running = False
            print()
            print("=" * 50)
            print(f"   Products on record   : {len(inventory)}")
            print(f"   Total inventory value: Rs.{calculate_total_value():.2f}")
            print("   Goodbye!")
            print("=" * 50)
        else:
            print()
            print(f"   INVALID OPTION: '{choice}'. Please choose 1 to 6.")


if __name__ == "__main__":
    main()
