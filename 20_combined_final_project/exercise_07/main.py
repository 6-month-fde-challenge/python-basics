"""
Exercise 07 - Shopping Cart
===========================
A menu-driven shopping cart that runs until the user chooses Exit.

    1. Add product     2. Remove product     3. View cart
    4. Calculate bill  5. Exit

FUNCTIONS
    show_menu()        - display the options
    add_product()      - add an item, or increase the quantity if already present
    remove_product()   - remove an item, or reduce its quantity
    view_cart()        - display the cart as a table
    calculate_bill()   - subtotal, GST and grand total
    main()             - the while loop driving the menu

DESIGN NOTE
Adding an item that is ALREADY in the cart increases its quantity instead
of creating a duplicate line - which is how a real cart behaves. Removing
asks how many units to take out, and only deletes the line when the
quantity reaches zero.

ERROR HANDLING
    unknown products, blank names, non-numeric quantities, quantities of
    zero or less, and removing more units than the cart holds.

SAMPLE INPUT / OUTPUT
    Add Laptop x1, Mouse x2, then View cart:
        Laptop   55000.00 x 1 = 55000.00
        Mouse      700.00 x 2 =  1400.00
    Calculate bill -> Subtotal 56400.00, GST 18% 10152.00, TOTAL 66552.00
"""

# The shop's catalogue: product name -> unit price
CATALOGUE = {
    "laptop": 55000.0,
    "mouse": 700.0,
    "keyboard": 1500.0,
    "monitor": 12000.0,
    "headphones": 2500.0,
    "webcam": 3200.0,
}

GST_RATE = 18  # percent

# The cart: product name -> quantity
cart = {}


def show_menu():
    """Display the shopping cart menu."""
    item_count = 0
    for quantity in cart.values():
        item_count += quantity

    print()
    print("=" * 48)
    print("              SHOPPING CART")
    print("=" * 48)
    print(f"   Items in cart : {item_count}")
    print("   " + "-" * 42)
    print("   1. Add product")
    print("   2. Remove product")
    print("   3. View cart")
    print("   4. Calculate bill")
    print("   5. Exit")
    print("=" * 48)


def show_catalogue():
    """Display the products available to buy."""
    print()
    print("   AVAILABLE PRODUCTS")
    print("   " + "-" * 34)
    for name, price in CATALOGUE.items():
        print(f"   {name.title():<16} Rs.{price:>10.2f}")
    print("   " + "-" * 34)


def get_quantity(prompt):
    """Ask for a quantity and return it, or None if the input is invalid."""
    entry = input(prompt)

    try:
        quantity = int(entry)
    except ValueError:
        print(f"      ERROR: '{entry}' is not a whole number.")
        return None

    if quantity <= 0:
        print("      ERROR: the quantity must be at least 1.")
        return None

    return quantity


def add_product():
    """Add a product to the cart, or increase its quantity if already there."""
    show_catalogue()

    name = input("   Product to add : ").strip().lower()

    if name == "":
        print("      ERROR: no product name entered.")
        return

    if name not in CATALOGUE:
        print(f"      ERROR: '{name}' is not in the catalogue.")
        return

    quantity = get_quantity("   Quantity       : ")
    if quantity is None:
        return

    # Already in the cart -> increase the quantity rather than duplicate the line
    if name in cart:
        cart[name] += quantity
        print()
        print(f"   UPDATED: {name.title()} quantity is now {cart[name]}.")
    else:
        cart[name] = quantity
        print()
        print(f"   ADDED: {quantity} x {name.title()}")

    line_total = CATALOGUE[name] * cart[name]
    print(f"   Line total: Rs.{line_total:.2f}")


def remove_product():
    """Remove units of a product, deleting the line when it reaches zero."""
    if len(cart) == 0:
        print()
        print("   The cart is empty - there is nothing to remove.")
        return

    view_cart()

    name = input("   Product to remove : ").strip().lower()

    if name not in cart:
        print(f"      ERROR: '{name}' is not in your cart.")
        return

    print(f"   You currently have {cart[name]} x {name.title()}")
    quantity = get_quantity("   How many to remove : ")
    if quantity is None:
        return

    if quantity > cart[name]:
        print(f"      ERROR: you only have {cart[name]} in the cart.")
        return

    cart[name] -= quantity

    print()
    if cart[name] == 0:
        del cart[name]
        print(f"   REMOVED: {name.title()} has been taken out of the cart.")
    else:
        print(f"   UPDATED: {name.title()} quantity is now {cart[name]}.")


def view_cart():
    """Display the cart contents as a table."""
    print()
    print("   YOUR CART")
    print("   " + "-" * 52)

    if len(cart) == 0:
        print("   The cart is empty.")
        print("   " + "-" * 52)
        return

    print(f"   {'PRODUCT':<16}{'PRICE':>12}{'QTY':>6}{'LINE TOTAL':>16}")
    print("   " + "-" * 52)

    subtotal = 0.0
    for name, quantity in cart.items():
        price = CATALOGUE[name]
        line_total = price * quantity
        subtotal += line_total
        print(f"   {name.title():<16}{price:>12.2f}{quantity:>6}{line_total:>16.2f}")

    print("   " + "-" * 52)
    print(f"   {'SUBTOTAL':<34}{subtotal:>18.2f}")


def calculate_bill():
    """Calculate and display the final bill including GST."""
    print()
    print("=" * 52)
    print("                  FINAL BILL")
    print("=" * 52)

    if len(cart) == 0:
        print("   The cart is empty. Nothing to bill.")
        print("=" * 52)
        return 0.0

    subtotal = 0.0
    item_count = 0

    for name, quantity in cart.items():
        price = CATALOGUE[name]
        line_total = price * quantity
        subtotal += line_total
        item_count += quantity
        print(f"   {name.title():<16} {price:>9.2f} x {quantity:<3} ="
              f" Rs.{line_total:>12.2f}")

    gst = subtotal * GST_RATE / 100
    grand_total = subtotal + gst

    print("   " + "-" * 46)
    print(f"   {'Items':<28}: {item_count}")
    print(f"   {'Subtotal':<28}: Rs.{subtotal:>12.2f}")
    print(f"   {'GST at ' + str(GST_RATE) + '%':<28}: Rs.{gst:>12.2f}")
    print("   " + "-" * 46)
    print(f"   {'GRAND TOTAL':<28}: Rs.{grand_total:>12.2f}")
    print("=" * 52)

    return grand_total


def main():
    """Run the shopping cart until the user chooses Exit."""
    print("Welcome to the online store.")

    # INITIALIZATION
    running = True

    # CONDITION : the cart stays open until Exit is chosen
    while running:
        show_menu()
        choice = input("   Choose an option (1-5) : ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            remove_product()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            calculate_bill()
        elif choice == "5":
            # UPDATE / TERMINATION
            running = False
            print()
            if len(cart) > 0:
                print("   Your final bill before leaving:")
                calculate_bill()
            print()
            print("   Thank you for shopping with us. Goodbye!")
        else:
            print()
            print(f"   INVALID OPTION: '{choice}'. Please choose 1 to 5.")


if __name__ == "__main__":
    main()
