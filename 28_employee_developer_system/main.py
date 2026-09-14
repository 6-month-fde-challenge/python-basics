"""
main.py - the employee and developer demonstration
===================================================
Five people on one payroll: two plain employees and three developers. The point
of the exercise is what the developers get **without** Developer defining it.

    python main.py

All of the logic lives in employee.py.
"""

from employee import Developer, Employee

LINE = "=" * 62


def title(number, text):
    print()
    print(LINE)
    print(f"  {number}. {text}")
    print(LINE)


# ---------------------------------------------------------------- 1

def demo_1_building():
    title(1, "Two classes, five objects")

    staff = [
        Employee("E101", "Anita Desai", 68_000, "Finance"),
        Employee("E102", "Vikram Shah", 74_500, "Operations"),
        Developer("E103", "Rahul Verma", 92_000, "Engineering", "Python", 6),
        Developer("E104", "Sneha Pillai", 81_000, "Engineering", "JavaScript", 3),
        Developer("E105", "Imran Qureshi", 1_10_000, "Engineering", "Go", 9),
    ]

    for person in staff:
        print(f"      {person!r}")

    print()
    print(f"    Employee.get_total_employees()  -> "
          f"{Employee.get_total_employees()}")
    print()
    print("    Five, not two. Developer.__init__ calls super().__init__, and")
    print("    the counter is incremented there - so a developer is counted")
    print("    by code that was never written in Developer.")
    return staff


# ---------------------------------------------------------------- 2

def demo_2_what_is_inherited(staff):
    title(2, "What Developer got for free")

    rahul = staff[2]

    print("    Developer defines: __init__, role(), display_details(),")
    print("                       is_senior(), code(), _clean_experience()")
    print()
    print("    Everything below is Employee's code, running on a Developer:")
    print()
    print(f"      rahul.annual_salary()  -> {rahul.annual_salary():,.2f}")
    print(f"      rahul.give_raise(8000) -> {rahul.give_raise(8_000):,.2f}")
    print(f"      rahul.company          -> {rahul.company}")
    print(f"      rahul.CURRENCY         -> {rahul.CURRENCY}")
    print(f"      Employee.get_total_employees() from rahul -> "
          f"{rahul.get_total_employees()}")
    print()
    print("    And the one thing only a Developer can do:")
    print(f"      rahul.code('fix the import bug')")
    print(f"        -> {rahul.code('fix the import bug')}")
    print()

    anita = staff[0]
    try:
        anita.code("anything")
    except AttributeError as error:
        print(f"      anita.code('anything') -> AttributeError: {error}")
    print("    Inheritance runs one way only.")


# ---------------------------------------------------------------- 3

def demo_3_display(staff):
    title(3, "display_details() - overridden, not replaced")

    staff[0].display_details()
    print()
    staff[2].display_details()
    print()
    print("    The first six lines of both blocks come from the same method.")
    print("    Developer.display_details() is four lines long:")
    print()
    print("        def display_details(self):")
    print("            super().display_details()")
    print("            print(... language ...)")
    print("            print(... experience ...)")
    print("            print(... senior ...)")
    print()
    print("    Copying the parent's six prints instead would have worked today")
    print("    and drifted out of step the first time Employee changed.")


# ---------------------------------------------------------------- 4

def demo_4_overriding(staff):
    title(4, "Overriding role() and BONUS_RATE")

    print(f"    {'name':<16}{'class':<12}{'role()':<20}{'bonus rate':>11}")
    print(f"    {'-' * 59}")
    for person in staff:
        print(f"    {person.name:<16}{type(person).__name__:<12}"
              f"{person.role():<20}{person.BONUS_RATE:>11.0%}")

    print()
    print("    role() is defined twice - once in each class. Python looks at")
    print("    the object's own class first:")
    print(f"      Employee.__mro__   {' -> '.join(c.__name__ for c in Employee.__mro__)}")
    print(f"      Developer.__mro__  {' -> '.join(c.__name__ for c in Developer.__mro__)}")

    print()
    print("    BONUS_RATE is a class variable defined in both classes, so the")
    print("    same inherited bonus() method gives two different answers:")
    print()
    for person in (staff[0], staff[2]):
        print(f"      {person.name:<16}{person.annual_salary():>14,.2f}"
              f" x {person.BONUS_RATE:.0%} = {person.bonus():>12,.2f}")
    print()
    print("    bonus() was written once, in Employee, and never overridden.")


# ---------------------------------------------------------------- 5

def demo_5_is_a(staff):
    title(5, "isinstance() - a Developer IS an Employee")

    rahul, anita = staff[2], staff[0]

    print(f"    isinstance(rahul, Developer)  -> {isinstance(rahul, Developer)}")
    print(f"    isinstance(rahul, Employee)   -> {isinstance(rahul, Employee)}")
    print(f"    isinstance(anita, Developer)  -> {isinstance(anita, Developer)}")
    print(f"    type(rahul) is Employee       -> {type(rahul) is Employee}")
    print(f"    issubclass(Developer, Employee) -> {issubclass(Developer, Employee)}")

    print()
    print("    Which is what lets one loop handle both kinds:")
    print()
    total = 0
    for person in staff:
        total += person.annual_salary()
        note = f"  [{person.language}]" if isinstance(person, Developer) else ""
        print(f"      {person.name:<16}{person.annual_salary():>14,.2f}{note}")
    print(f"      {'-' * 30}")
    print(f"      {'payroll':<16}{total:>14,.2f}")
    print()
    print("    annual_salary() is called five times and exists once.")


# ---------------------------------------------------------------- 6

def demo_6_class_members(staff):
    title(6, "One counter and one company, across two classes")

    print(f"    Employee.company   -> {Employee.company}")
    print(f"    Developer.company  -> {Developer.company}"
          f"   <- inherited, not copied")
    print()
    Employee.set_company("Nova Systems International")
    print("    Employee.set_company('Nova Systems International')")
    print(f"    Employee.company   -> {Employee.company}")
    print(f"    Developer.company  -> {Developer.company}")
    print()
    for person in staff[:3]:
        print(f"      {person.name:<16}{person.company}")

    print()
    print(f"    Employee.total_employees         -> {Employee.total_employees}")
    print(f"    Developer.total_employees        -> {Developer.total_employees}")
    print(f"    Employee.get_total_employees()   -> "
          f"{Employee.get_total_employees()}")
    print()
    print("    There is one counter, held by Employee. Developer reads it")
    print("    through inheritance, which is why the total is five and not")
    print("    two plus three kept in two different places.")

    print()
    print("    The validation both classes share:")
    cases = [
        ("salary is a string", lambda: Employee("E999", "X", "lots", "IT")),
        ("salary is zero", lambda: Employee("E999", "X", 0, "IT")),
        ("experience is negative",
         lambda: Developer("E999", "X", 50_000, "IT", "Python", -2)),
    ]
    for label, call in cases:
        try:
            call()
        except ValueError as error:
            print(f"      {label:<24} ValueError: {error}")
    print()
    print("    Developer never wrote the salary check. It inherited it.")


def main():
    print()
    print(LINE)
    print("  EXERCISE 28 - Employee and Developer")
    print("  Parent class, child class, inheritance, super(), overriding")
    print(LINE)

    staff = demo_1_building()
    demo_2_what_is_inherited(staff)
    demo_3_display(staff)
    demo_4_overriding(staff)
    demo_5_is_a(staff)
    demo_6_class_members(staff)

    print()
    print(LINE)
    print("  Developer is 47 lines long and behaves like a full Employee,")
    print("  because the other 83 lines were written once, one class up.")
    print(LINE)
    print()


if __name__ == "__main__":
    main()
