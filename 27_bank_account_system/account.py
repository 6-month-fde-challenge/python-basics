"""
account.py - the BankAccount class
===================================
An account holder, an account number, a balance, and the four operations a
counter clerk can perform on them.

    from account import BankAccount

    acc = BankAccount("Aarav Sharma", "AC1001", 5000)
    acc.deposit(2500)          #  7500.0
    acc.withdraw(9000)         #  InsufficientFundsError
    acc.check_balance()        #  7500.0
    BankAccount.total_accounts #  1

The bank's name is a class variable, so it is stored once rather than copied into
every account, and `BankAccount.rename_bank()` changes it for all of them.
"""


class BankError(Exception):
    """Base class for everything this module raises - one except clause catches all."""


class InsufficientFundsError(BankError):
    """Raised when a withdrawal is larger than the balance."""

    def __init__(self, requested, available):
        self.requested = requested
        self.available = available
        self.short_by = requested - available
        super().__init__(
            f"cannot withdraw {requested:,.2f} from a balance of {available:,.2f} "
            f"(short by {self.short_by:,.2f})"
        )


class InvalidAmountError(BankError):
    """Raised when an amount is not a usable positive number."""

    def __init__(self, amount, reason):
        self.amount = amount
        self.reason = reason
        super().__init__(f"invalid amount {amount!r}: {reason}")


class BankAccount:
    """One account at one bank."""

    # ---------------------------------------------------------------- class
    # One copy, shared by every account object.

    bank_name = "Nova Bank"
    total_accounts = 0          # the bonus: how many accounts have been opened
    MIN_BALANCE = 0.0
    WITHDRAWAL_LIMIT = 50_000.0

    # ------------------------------------------------------------ construct

    def __init__(self, holder_name, account_number, balance=0.0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = self._clean_amount(balance, allow_zero=True)
        self.history = []           # its own list - see the note in the README

        BankAccount.total_accounts += 1
        self._record("OPEN", self.balance)

    # ------------------------------------------------------- internal parts

    @staticmethod
    def _clean_amount(amount, allow_zero=False):
        """Turn an incoming amount into a float, or raise. Used by all three."""
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise InvalidAmountError(amount, "must be a number")
        amount = float(amount)
        if amount < 0:
            raise InvalidAmountError(amount, "must not be negative")
        if amount == 0 and not allow_zero:
            raise InvalidAmountError(amount, "must be greater than zero")
        return round(amount, 2)

    def _record(self, kind, amount):
        """Append one line to this account's own history."""
        self.history.append((kind, round(amount, 2), self.balance))

    # ------------------------------------------------------------- instance

    def deposit(self, amount):
        """Add money. Returns the new balance."""
        amount = self._clean_amount(amount)
        self.balance = round(self.balance + amount, 2)
        self._record("DEPOSIT", amount)
        return self.balance

    def withdraw(self, amount):
        """Take money out - never more than is there. Returns the new balance."""
        amount = self._clean_amount(amount)

        if amount > self.WITHDRAWAL_LIMIT:
            raise InvalidAmountError(
                amount, f"above the per-transaction limit of {self.WITHDRAWAL_LIMIT:,.2f}"
            )
        if amount > self.balance - self.MIN_BALANCE:
            # the validation the assignment asks for: refuse, do not overdraw
            raise InsufficientFundsError(amount, self.balance - self.MIN_BALANCE)

        self.balance = round(self.balance - amount, 2)
        self._record("WITHDRAW", amount)
        return self.balance

    def check_balance(self):
        """What is in the account right now."""
        return self.balance

    def transfer_to(self, other, amount):
        """Move money to another account. Withdraw first, so a refusal costs nothing."""
        if not isinstance(other, BankAccount):
            raise InvalidAmountError(other, "transfer target is not a BankAccount")
        self.withdraw(amount)          # raises before anything is credited
        other.deposit(amount)
        return self.balance, other.balance

    def display_account_details(self):
        """Print the account as a block. The only method here that prints."""
        print(f"    {self.holder_name}  ({self.account_number})")
        print(f"      bank      : {self.bank_name}")
        print(f"      balance   : {self.balance:>12,.2f}")
        print(f"      movements : {len(self.history)}")
        for kind, amount, running in self.history:
            print(f"        {kind:<9}{amount:>12,.2f}   -> {running:>12,.2f}")

    # ---------------------------------------------------------------- class

    @classmethod
    def rename_bank(cls, new_name):
        """Change the bank's name for every account there is, open or not yet."""
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValueError("bank name must be a non-empty string")
        cls.bank_name = new_name.strip()
        return cls.bank_name

    @classmethod
    def get_total_accounts(cls):
        """How many accounts have been opened."""
        return cls.total_accounts

    @classmethod
    def open_salary_account(cls, holder_name, account_number):
        """A second constructor: a salary account starts with a 1,000 credit."""
        return cls(holder_name, account_number, 1_000.0)

    # -------------------------------------------------------------- dunders

    def __repr__(self):
        return (f"BankAccount({self.holder_name!r}, {self.account_number!r}, "
                f"{self.balance!r})")


if __name__ == "__main__":
    demo = BankAccount("Test Holder", "AC0000", 1_000)
    demo.deposit(500)
    try:
        demo.withdraw(9_999)
    except InsufficientFundsError as error:
        print("refused:", error)
    demo.display_account_details()
    print()
    print("total accounts:", BankAccount.get_total_accounts())
