"""
00_concepts.py - the five ideas exercise 28 is built on
========================================================
Parent class, child class, inheriting, overriding, and super().

Standalone and runnable. It imports nothing from the application:

    python 00_concepts.py

Read this first, then employee.py, then main.py.
"""

LINE = "=" * 62


def title(number, text):
    print()
    print(LINE)
    print(f"  {number}. {text}")
    print(LINE)


# ---------------------------------------------------------------------------
# 1. A child class starts with everything the parent has.
# ---------------------------------------------------------------------------

def concept_1_inheriting():
    title(1, "class Child(Parent) - inheriting")

    class Animal:
        def __init__(self, name):
            self.name = name

        def eat(self):
            return f"{self.name} is eating"

    class Dog(Animal):
        """Four words of code. It already has __init__ and eat()."""

    rocky = Dog("Rocky")

    print("    class Animal:  __init__, eat()")
    print("    class Dog(Animal):  <- and nothing else")
    print()
    print(f"    rocky = Dog('Rocky')")
    print(f"    rocky.name    -> {rocky.name}       (from Animal.__init__)")
    print(f"    rocky.eat()   -> {rocky.eat()}   (from Animal.eat)")
    print()
    print("    Dog defined neither. It inherited both.")


# ---------------------------------------------------------------------------
# 2. The child adds what makes it different.
# ---------------------------------------------------------------------------

def concept_2_adding():
    title(2, "The child adds its own")

    class Animal:
        def __init__(self, name):
            self.name = name

        def eat(self):
            return f"{self.name} is eating"

    class Dog(Animal):
        def fetch(self):
            return f"{self.name} fetched the ball"

    rocky = Dog("Rocky")
    generic = Animal("Some animal")

    print(f"    rocky.eat()     -> {rocky.eat()}")
    print(f"    rocky.fetch()   -> {rocky.fetch()}")
    print()
    try:
        generic.fetch()
    except AttributeError as error:
        print(f"    generic.fetch() -> AttributeError: {error}")
    print()
    print("    Inheritance goes one way. A Dog is an Animal; an Animal is not")
    print("    a Dog, and does not get fetch().")


# ---------------------------------------------------------------------------
# 3. Overriding: same method name, different behaviour.
# ---------------------------------------------------------------------------

def concept_3_overriding():
    title(3, "Overriding a method")

    class Animal:
        def speak(self):
            return "some sound"

    class Dog(Animal):
        def speak(self):            # same name -> the child's wins
            return "woof"

    class Cat(Animal):
        def speak(self):
            return "meow"

    for thing in (Animal(), Dog(), Cat()):
        print(f"    {type(thing).__name__:<8}.speak()  -> {thing.speak()}")

    print()
    print("    Python looks on the object's own class first, and only walks up")
    print("    to the parent if it finds nothing:")
    print(f"      Dog.__mro__  ->  {' -> '.join(c.__name__ for c in Dog.__mro__)}")


# ---------------------------------------------------------------------------
# 4. super() - reusing the parent instead of retyping it.
# ---------------------------------------------------------------------------

def concept_4_super():
    title(4, "super() - calling the parent")

    class Animal:
        def __init__(self, name):
            print(f"        Animal.__init__ set name = {name}")
            self.name = name

        def describe(self):
            return f"{self.name}, an animal"

    class Dog(Animal):
        def __init__(self, name, breed):
            super().__init__(name)          # let the parent do its half
            print(f"        Dog.__init__ set breed = {breed}")
            self.breed = breed

        def describe(self):
            return super().describe() + f", breed {self.breed}"

    print("    Dog('Rocky', 'Beagle')")
    rocky = Dog("Rocky", "Beagle")
    print()
    print(f"    rocky.__dict__   -> {rocky.__dict__}")
    print(f"    rocky.describe() -> {rocky.describe()}")
    print()
    print("    Dog.describe() did not copy Animal's sentence. It called it and")
    print("    added to it, so a change in Animal reaches Dog for free.")

    print()
    print("    What happens if the child forgets super().__init__:")

    class Broken(Animal):
        def __init__(self, name, breed):
            self.breed = breed              # name is never set

    broken = Broken("Rocky", "Beagle")
    try:
        broken.describe()
    except AttributeError as error:
        print(f"      broken.describe() -> AttributeError: {error}")


# ---------------------------------------------------------------------------
# 5. isinstance and issubclass - asking what something is.
# ---------------------------------------------------------------------------

def concept_5_isinstance():
    title(5, "isinstance() and issubclass()")

    class Animal:
        pass

    class Dog(Animal):
        pass

    rocky = Dog()
    generic = Animal()

    print(f"    isinstance(rocky, Dog)       -> {isinstance(rocky, Dog)}")
    print(f"    isinstance(rocky, Animal)    -> {isinstance(rocky, Animal)}"
          f"    <- a Dog IS an Animal")
    print(f"    isinstance(generic, Dog)     -> {isinstance(generic, Dog)}"
          f"   <- but not the other way")
    print(f"    type(rocky) is Animal        -> {type(rocky) is Animal}"
          f"   <- type() ignores inheritance")
    print()
    print(f"    issubclass(Dog, Animal)      -> {issubclass(Dog, Animal)}")
    print(f"    issubclass(Animal, Dog)      -> {issubclass(Animal, Dog)}")
    print()
    print("    Use isinstance() when the question is 'can I treat it as an")
    print("    Animal?'. type() answers a narrower question and is usually")
    print("    the wrong one.")


def main():
    print()
    print(LINE)
    print("  EXERCISE 28 - concepts")
    print("  parent, child, inherit, override, super()")
    print(LINE)

    concept_1_inheriting()
    concept_2_adding()
    concept_3_overriding()
    concept_4_super()
    concept_5_isinstance()

    print()
    print(LINE)
    print("  Every idea above is used by employee.py.")
    print(LINE)
    print()


if __name__ == "__main__":
    main()
