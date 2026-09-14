"""
00_concepts.py - the six ideas exercise 26 is built on
=======================================================
Class, object, __init__, instance method, class variable, class method.

Standalone and runnable. It imports nothing from the application and prints
real output rather than describing it:

    python 00_concepts.py

Read this first, then student.py, then main.py.
"""

LINE = "=" * 62


def title(number, text):
    print()
    print(LINE)
    print(f"  {number}. {text}")
    print(LINE)


# ---------------------------------------------------------------------------
# 1. A class is a blueprint. An object is one thing built from it.
# ---------------------------------------------------------------------------

def concept_1_class_and_object():
    title(1, "class and object")

    class Dog:
        """The blueprint. No dog exists yet."""

    first = Dog()          # calling the class builds an object
    second = Dog()

    print("    class Dog:  -> the blueprint")
    print(f"    Dog()       -> {first}")
    print(f"    Dog()       -> {second}")
    print()
    print(f"    first is second : {first is second}")
    print(f"    type(first)     : {type(first).__name__}")
    print()
    print("    Two calls, two separate objects. The class was written once.")


# ---------------------------------------------------------------------------
# 2. __init__ runs at build time and gives the object its attributes.
# ---------------------------------------------------------------------------

def concept_2_init():
    title(2, "__init__ - the constructor")

    class Dog:
        def __init__(self, name, breed):
            print(f"      __init__ is running for {name}")
            self.name = name        # self.<x> = ... creates an attribute
            self.breed = breed

    print("    Dog('Rocky', 'Beagle')")
    rocky = Dog("Rocky", "Beagle")
    print()
    print(f"    rocky.name      : {rocky.name}")
    print(f"    rocky.breed     : {rocky.breed}")
    print(f"    rocky.__dict__  : {rocky.__dict__}")
    print()
    print("    __init__ is never called by hand. Dog(...) calls it.")


# ---------------------------------------------------------------------------
# 3. self is the object the method was called on - nothing more.
# ---------------------------------------------------------------------------

def concept_3_self():
    title(3, "self, and instance methods")

    class Dog:
        def __init__(self, name):
            self.name = name

        def speak(self):
            return f"{self.name} says woof"

    rocky = Dog("Rocky")
    bruno = Dog("Bruno")

    print(f"    rocky.speak()     -> {rocky.speak()}")
    print(f"    bruno.speak()     -> {bruno.speak()}")
    print()
    print("    Both calls run the same four lines of code. The only")
    print("    difference is what self points at:")
    print()
    print(f"    Dog.speak(rocky)  -> {Dog.speak(rocky)}")
    print()
    print("    rocky.speak() IS Dog.speak(rocky). Python passes the object")
    print("    on the left of the dot as the first argument.")


# ---------------------------------------------------------------------------
# 4. Instance variable vs class variable.
# ---------------------------------------------------------------------------

def concept_4_class_variable():
    title(4, "instance variable vs class variable")

    class Dog:
        species = "Canis familiaris"    # class variable - one copy, shared
        count = 0                       # class variable - a running total

        def __init__(self, name):
            self.name = name            # instance variable - one per object
            Dog.count += 1

    rocky = Dog("Rocky")
    bruno = Dog("Bruno")

    print(f"    rocky.name     : {rocky.name}        (its own)")
    print(f"    bruno.name     : {bruno.name}        (its own)")
    print(f"    rocky.species  : {rocky.species}")
    print(f"    bruno.species  : {bruno.species}")
    print(f"    Dog.species    : {Dog.species}   <- they all read this one")
    print()
    print(f"    Dog.count      : {Dog.count}   (two objects were built)")

    print()
    print("    The trap: assigning through the object does NOT change the")
    print("    class variable, it creates an instance variable that hides it.")
    rocky.species = "Good boy"
    print()
    print(f"      rocky.species = 'Good boy'")
    print(f"      rocky.species : {rocky.species}")
    print(f"      bruno.species : {bruno.species}")
    print(f"      Dog.species   : {Dog.species}")
    print()
    print("    That is why the counter above says Dog.count += 1 and not")
    print("    self.count += 1 - the second one would count nothing.")


# ---------------------------------------------------------------------------
# 5. A class method receives the class, not the object.
# ---------------------------------------------------------------------------

def concept_5_class_method():
    title(5, "@classmethod")

    class Dog:
        count = 0

        def __init__(self, name):
            self.name = name
            Dog.count += 1

        @classmethod
        def get_count(cls):
            return cls.count            # cls is Dog

    print(f"    Dog.get_count()   -> {Dog.get_count()}   (no objects yet)")
    Dog("Rocky")
    Dog("Bruno")
    Dog("Simba")
    print(f"    Dog.get_count()   -> {Dog.get_count()}   (after three)")
    print()
    print("    get_count() is called on the class. It never needs an object,")
    print("    and asking a single dog how many dogs exist would be odd.")


# ---------------------------------------------------------------------------
# 6. The three kinds of method, side by side.
# ---------------------------------------------------------------------------

def concept_6_three_methods():
    title(6, "instance / class / static")

    class Dog:
        count = 0

        def __init__(self, name):
            self.name = name
            Dog.count += 1

        def speak(self):                 # needs THIS dog
            return f"{self.name} says woof"

        @classmethod
        def get_count(cls):              # needs the class
            return cls.count

        @staticmethod
        def is_valid_name(name):         # needs neither
            return isinstance(name, str) and name.strip() != ""

    rocky = Dog("Rocky")

    print("    def speak(self)          instance method  needs the object")
    print("    @classmethod get_count   class method     needs the class")
    print("    @staticmethod is_valid   static method    needs neither")
    print()
    print(f"    rocky.speak()            -> {rocky.speak()}")
    print(f"    Dog.get_count()          -> {Dog.get_count()}")
    print(f"    Dog.is_valid_name('')    -> {Dog.is_valid_name('')}")
    print(f"    Dog.is_valid_name('Su')  -> {Dog.is_valid_name('Su')}")
    print()
    print("    Pick by what the method needs, not by where it is written.")


def main():
    print()
    print(LINE)
    print("  EXERCISE 26 - concepts")
    print("  class, object, __init__, self, class variable, class method")
    print(LINE)

    concept_1_class_and_object()
    concept_2_init()
    concept_3_self()
    concept_4_class_variable()
    concept_5_class_method()
    concept_6_three_methods()

    print()
    print(LINE)
    print("  Every idea above is used by student.py.")
    print(LINE)
    print()


if __name__ == "__main__":
    main()
