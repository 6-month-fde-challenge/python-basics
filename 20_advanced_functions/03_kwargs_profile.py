"""
Question 3 - create_profile(**kwargs)
======================================
Concept: **kwargs = "any number of KEYWORD arguments".

    *args   collects extra POSITIONAL arguments into a TUPLE
    **kwargs collects extra KEYWORD arguments into a DICTIONARY

    create_profile(name="Rahul", age=22)
        -> kwargs is {"name": "Rahul", "age": 22}

Because kwargs is a dictionary, .items() walks through it and gives
both the attribute name and its value.

WHY THIS IS USEFUL: a profile does not have a fixed set of fields.
One user supplies a phone number, another supplies a GitHub link.
**kwargs lets one function handle every combination without needing
a parameter for each possible field.
"""


def create_profile(**kwargs):
    """Print every attribute the caller chose to supply."""
    print("   Inside the function, kwargs =", kwargs)
    print("   Type of kwargs              =", type(kwargs).__name__)
    print("   Attributes supplied         =", len(kwargs))
    print()

    if len(kwargs) == 0:
        print("   No details were supplied.")
        return

    print("   USER PROFILE")
    print("   " + "-" * 40)
    for key, value in kwargs.items():
        # replace underscores so 'phone_number' reads as 'Phone Number'
        label = key.replace("_", " ").title()
        print(f"   {label:<18}: {value}")
    print("   " + "-" * 40)


print("=" * 55)
print("EXAMPLE 1 - a short profile")
print("=" * 55)
create_profile(name="Rahul", age=22)

print()
print("=" * 55)
print("EXAMPLE 2 - a longer profile, completely different fields")
print("=" * 55)
create_profile(
    name="Priya",
    age=24,
    city="Hyderabad",
    course="Data Science",
    phone_number="9876543210",
    is_certified=True
)

print()
print("=" * 55)
print("EXAMPLE 3 - no details at all")
print("=" * 55)
create_profile()

print()

# --- *args and **kwargs in the same function -------------------------------
print("=" * 55)
print("*args AND **kwargs TOGETHER")
print("=" * 55)


def show_everything(required, *args, **kwargs):
    """The order must always be: normal parameters, then *args, then **kwargs."""
    print("   required (a normal parameter) :", required)
    print("   args     (extra positionals)  :", args)
    print("   kwargs   (extra keywords)     :", kwargs)


print("\nshow_everything('Rahul', 10, 20, 30, city='Delhi', age=22)")
show_everything("Rahul", 10, 20, 30, city="Delhi", age=22)
print()
print("   The order is fixed: normal parameters, then *args, then **kwargs.")
print()

# --- Unpacking a dictionary into **kwargs ----------------------------------
print("=" * 55)
print("PASSING A DICTIONARY IN WITH **")
print("=" * 55)

details = {"name": "Aman", "age": 25, "city": "Pune"}
print("details =", details)
print("create_profile(**details) unpacks it into keyword arguments:")
print()
create_profile(**details)
