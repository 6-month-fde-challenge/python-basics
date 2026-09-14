"""
employee.py - Employee, and Developer(Employee)
================================================
The parent holds what every employee has. The child adds what only a developer
has, and reuses the rest rather than repeating it.

    Employee
       |
    Developer

    from employee import Employee, Developer

    anita = Employee("E101", "Anita Desai", 68_000, "Finance")
    rahul = Developer("E104", "Rahul Verma", 92_000, "Engineering",
                      "Python", 4)

    anita.display_details()
    rahul.display_details()        # the child's version, which calls the parent's
    rahul.annual_salary()          # inherited unchanged
"""


class Employee:
    """Anybody on the payroll."""

    # ---------------------------------------------------------------- class
    company = "Nova Systems"
    total_employees = 0        # counts EVERY employee, including subclasses
    CURRENCY = "INR"
    BONUS_RATE = 0.05

    # ------------------------------------------------------------ construct

    def __init__(self, employee_id, name, salary, department):
        self.employee_id = employee_id
        self.name = name
        self.salary = self._clean_salary(salary)
        self.department = department
        Employee.total_employees += 1

    # --------------------------------------------------------------- static

    @staticmethod
    def _clean_salary(salary):
        if isinstance(salary, bool) or not isinstance(salary, (int, float)):
            raise ValueError(f"salary must be a number, got {salary!r}")
        if salary <= 0:
            raise ValueError(f"salary must be greater than zero, got {salary}")
        return float(salary)

    # ------------------------------------------------------------- instance

    def annual_salary(self):
        """Twelve months of the monthly figure."""
        return self.salary * 12

    def bonus(self):
        """A flat percentage of the annual salary."""
        return round(self.annual_salary() * self.BONUS_RATE, 2)

    def give_raise(self, amount):
        """Increase the monthly salary. Returns the new figure."""
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise ValueError(f"raise must be a number, got {amount!r}")
        if amount <= 0:
            raise ValueError(f"raise must be greater than zero, got {amount}")
        self.salary = float(self.salary + amount)
        return self.salary

    def role(self):
        """What this person is. Overridden by every child class."""
        return "Employee"

    def display_details(self):
        """Print the employee. Children extend this rather than replacing it."""
        print(f"    {self.name}  ({self.employee_id})")
        print(f"      role       : {self.role()}")
        print(f"      department : {self.department}")
        print(f"      company    : {self.company}")
        print(f"      salary     : {self.CURRENCY} {self.salary:>12,.2f} / month")
        print(f"      annual     : {self.CURRENCY} {self.annual_salary():>12,.2f}")
        print(f"      bonus      : {self.CURRENCY} {self.bonus():>12,.2f}")

    # ---------------------------------------------------------------- class

    @classmethod
    def get_total_employees(cls):
        """How many employees exist, of any kind."""
        return cls.total_employees

    @classmethod
    def set_company(cls, name):
        """Rename the company for everybody on the payroll."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("company name must be a non-empty string")
        Employee.company = name.strip()
        return Employee.company

    # -------------------------------------------------------------- dunders

    def __repr__(self):
        return (f"{type(self).__name__}({self.employee_id!r}, {self.name!r}, "
                f"{self.salary!r}, {self.department!r})")


class Developer(Employee):
    """An employee who writes code. Adds a language and years of experience."""

    # a class variable of its own, alongside the ones inherited from Employee
    BONUS_RATE = 0.08          # overrides Employee.BONUS_RATE for developers only
    SENIOR_YEARS = 5

    def __init__(self, employee_id, name, salary, department,
                 language, experience):
        # the parent sets the four fields every employee has, including the
        # counter - so Developer never has to know how any of that works
        super().__init__(employee_id, name, salary, department)

        self.language = language
        self.experience = self._clean_experience(experience)

    @staticmethod
    def _clean_experience(years):
        if isinstance(years, bool) or not isinstance(years, (int, float)):
            raise ValueError(f"experience must be a number, got {years!r}")
        if years < 0:
            raise ValueError(f"experience must not be negative, got {years}")
        return float(years)

    # ------------------------------------------------------- overrides

    def role(self):
        """Overrides Employee.role()."""
        return "Senior Developer" if self.is_senior() else "Developer"

    def display_details(self):
        """Overrides Employee.display_details() - and calls it first."""
        super().display_details()                 # the parent prints its six lines
        print(f"      language   : {self.language}")
        print(f"      experience : {self.experience:.0f} years")
        print(f"      senior     : {self.is_senior()}")

    # ------------------------------------------------------- its own

    def is_senior(self):
        return self.experience >= self.SENIOR_YEARS

    def code(self, task):
        """Something only a Developer can do."""
        return f"{self.name} is writing {self.language} to {task}"


if __name__ == "__main__":
    anita = Employee("E101", "Anita Desai", 68_000, "Finance")
    rahul = Developer("E104", "Rahul Verma", 92_000, "Engineering", "Python", 6)
    anita.display_details()
    print()
    rahul.display_details()
    print()
    print("total employees:", Employee.get_total_employees())
