"""
main.py - the shop demonstration
=================================
Five products, a few sales, one restock, and a static method that is called
before any product exists.

    python main.py

All of the logic lives in product.py.
"""

from product import Product

LINE = "=" * 62


def title(number, text):
    print()
    print(LINE)
    print(f"  {number}. {text}")
    print(LINE)


def catalogue(products):
    print(f"    {'id':<7}{'name':<16}{'category':<14}{'price':>11}{'stock':>8}")
    print(f"    {'-' * 56}")
    for item in products:
        print(f"    {item.product_id:<7}{item.name:<16}{item.category:<14}"
              f"{item.price:>11,.2f}{item.stock:>8}")


# ---------------------------------------------------------------- 1

def demo_1_static_first():
    title(1, "A static method needs no object")

    print(f"    Product.get_total_products()  -> {Product.get_total_products()}")
    print("    There is not a single product yet - and this still works:")
    print()

    for price in [1299, 58_990.50, 0, -250, "999", True, None]:
        print(f"      Product.is_valid_price({price!r:<10}) -> "
              f"{Product.is_valid_price(price)}")

    print()
    print("    is_valid_price() reads no attribute of any product. It takes a")
    print("    number and answers a question about that number, so it takes")
    print("    neither self nor cls:")
    print()
    print("        @staticmethod")
    print("        def is_valid_price(price):")
    print("            return price > 0")
    print()
    print("    True is rejected first. bool subclasses int, so True > 0 is")
    print("    True and a price of True would be stored as 1.00.")


# ---------------------------------------------------------------- 2

def demo_2_catalogue():
    title(2, "Five products")

    products = [
        Product("P101", "Laptop", 58_990.00, "Electronics", 12),
        Product("P102", "Coffee Mug", 349.00, "Home", 60),
        Product("P103", "Notebook", 120.50, "Stationery", 4),
        Product("P104", "Olive Oil 1L", 899.00, "Grocery", 25),
        Product("P105", "Running Shoes", 4_250.00, "Fashion", 8),
    ]

    catalogue(products)
    print()
    print(f"    Product.get_total_products()  -> {Product.get_total_products()}")
    print(f"    Product.store_name            -> {Product.store_name}")
    return products


# ---------------------------------------------------------------- 3

def demo_3_total_price(products):
    title(3, "calculate_total_price(quantity)")

    laptop, mug = products[0], products[1]

    print(f"    {laptop.name} at {laptop.price:,.2f}, GST {Product.GST_RATE:.0%}")
    print()
    print(f"    {'qty':<6}{'subtotal':>14}{'with GST':>14}")
    print(f"    {'-' * 34}")
    for quantity in (1, 2, 5):
        print(f"    {quantity:<6}"
              f"{laptop.calculate_total_price(quantity, include_tax=False):>14,.2f}"
              f"{laptop.calculate_total_price(quantity):>14,.2f}")

    print()
    print("    include_tax defaults to True, so the common call is the short")
    print("    one and the exception is spelled out - the default-argument")
    print("    rule from exercise 19.")

    print()
    print("    A quantity that is not a quantity:")
    for bad in (0, -3, 2.5, "two"):
        try:
            mug.calculate_total_price(bad)
        except ValueError as error:
            print(f"      calculate_total_price({bad!r:<6}) -> ValueError: {error}")


# ---------------------------------------------------------------- 4

def demo_4_buying(products):
    title(4, "Buying - update_stock() through sell()")

    laptop, mug, notebook, oil, shoes = products

    print("    before")
    catalogue(products)
    print()

    sales = [(laptop, 2), (mug, 10), (shoes, 1), (oil, 3), (notebook, 2)]
    receipt = 0
    for item, quantity in sales:
        paid = item.sell(quantity)
        receipt += paid
        print(f"      sell {quantity:>2} x {item.name:<16}"
              f"{paid:>13,.2f}   {item.stock} left")

    print(f"      {'-' * 47}")
    print(f"      {'order total':<22}{receipt:>13,.2f}")

    print()
    print("    after")
    catalogue(products)

    print()
    print("    Stock went down by exactly what was sold, and units_sold went")
    print("    up by the same amount - both inside sell().")


# ---------------------------------------------------------------- 5

def demo_5_refusals(products):
    title(5, "What the shop refuses")

    notebook, laptop = products[2], products[0]

    print(f"    {notebook.name}: {notebook.stock} in stock")
    cases = [
        ("more than the shelf holds", lambda: notebook.sell(5)),
        ("a negative quantity", lambda: notebook.sell(-2)),
        ("half a notebook", lambda: notebook.sell(1.5)),
        ("a stock change of zero", lambda: notebook.update_stock(0)),
        ("removing more than exists", lambda: notebook.update_stock(-99)),
        ("a 100% discount", lambda: laptop.apply_discount(100)),
        ("a price of zero at build time",
         lambda: Product("P999", "Freebie", 0, "Home", 1)),
        ("an unknown category",
         lambda: Product("P998", "Anvil", 500, "Hardware", 1)),
    ]

    for label, call in cases:
        try:
            call()
        except ValueError as error:
            print(f"      {label:<28} ValueError: {error}")

    print()
    print(f"    {notebook.name} is still at {notebook.stock} - a refused sale")
    print("    changes nothing, because sell() prices the order and checks the")
    print("    stock before it touches either number.")

    print()
    print("    And the boundary that is allowed:")
    print(f"      notebook.sell({notebook.stock}) -> "
          f"{notebook.sell(notebook.stock):,.2f}   stock now {notebook.stock}")
    print(f"      notebook.in_stock()  -> {notebook.in_stock()}")


# ---------------------------------------------------------------- 6

def demo_6_restock_and_display(products):
    title(6, "Restocking, discounts and display_product()")

    notebook, shoes = products[2], products[4]

    print(f"    notebook.restock(50)  -> {notebook.restock(50)} in stock")
    print(f"    shoes.apply_discount(15) -> price {shoes.apply_discount(15):,.2f}")
    print()

    for item in (products[0], notebook, shoes):
        item.display_product()
        print()

    # the accumulator and champion patterns from exercise 18, over objects
    shelf_total, best = 0, products[0]
    for item in products:
        shelf_total += item.stock_value()
        if item.units_sold > best.units_sold:
            best = item

    print(f"    {'total shelf value':<24}{Product.CURRENCY} {shelf_total:>12,.2f}")
    print(f"    {'best seller':<24}{best.name} ({best.units_sold} units)")
    print(f"    {'low stock':<24}"
          f"{', '.join(i.name for i in products if i.is_low_stock()) or 'none'}")

    print()
    Product.set_store_name("Nova Cart India")
    print("    Product.set_store_name('Nova Cart India')")
    print(f"      Product.store_name   -> {Product.store_name}")
    print(f"      laptop.store_name    -> {products[0].store_name}")


def main():
    print()
    print(LINE)
    print("  EXERCISE 29 - E-Commerce Product System")
    print("  Static methods, stock updates, and pricing an order")
    print(LINE)

    demo_1_static_first()
    products = demo_2_catalogue()
    demo_3_total_price(products)
    demo_4_buying(products)
    demo_5_refusals(products)
    demo_6_restock_and_display(products)

    print()
    print(LINE)
    print(f"  {Product.get_total_products()} products exist. Two more were refused "
          f"before they did,")
    print("  because is_valid_price() runs in __init__ - before the object is.")
    print(LINE)
    print()


if __name__ == "__main__":
    main()
