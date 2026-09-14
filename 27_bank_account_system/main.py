"""
main.py - the banking demonstration
====================================
Opens four accounts, moves money between them, refuses the withdrawals that
should be refused, and renames the whole bank with one call.

    python main.py

All of the logic lives in account.py. This file only creates objects, calls
methods and prints what came back.
"""

from account import (BankAccount, BankError, InsufficientFundsError,
                     InvalidAmountError)

LINE = "=" * 62


def title(number, text):
    print()
    print(LINE)
    print(f"  {number}. {text}")
    print(LINE)


def balances(accounts):
    for account in accounts:
        print(f"      {account.holder_name:<16}{account.account_number:<10}"
              f"{account.check_balance():>12,.2f}")


# ---------------------------------------------------------------- 1

def demo_1_opening():
    title(1, "Opening accounts")

    print(f"    BankAccount.get_total_accounts()  -> "
          f"{BankAccount.get_total_accounts()}")
    print()

    accounts = [
        BankAccount("Aarav Sharma", "AC1001", 25_000),
        BankAccount("Diya Menon", "AC1002", 8_400.50),
        BankAccount("Kabir Rao", "AC1003"),                     # no opening balance
        BankAccount.open_salary_account("Meera Nair", "AC1004"),  # second constructor
    ]

    for account in accounts:
        print(f"      {account!r}")

    print()
    print(f"    BankAccount.get_total_accounts()  -> "
          f"{BankAccount.get_total_accounts()}")
    print()
    print("    Kabir's account opened at 0.00 - the default argument.")
    print("    Meera's opened at 1,000.00 without main.py naming the figure:")
    print("    open_salary_account() is a class method that calls cls(...).")
    return accounts


# ---------------------------------------------------------------- 2

def demo_2_deposit_withdraw(accounts):
    title(2, "deposit(), withdraw(), check_balance()")

    aarav, diya, kabir, meera = accounts

    print("    before")
    balances(accounts)
    print()

    print(f"    aarav.deposit(5000)      -> {aarav.deposit(5_000):>12,.2f}")
    print(f"    aarav.withdraw(12000)    -> {aarav.withdraw(12_000):>12,.2f}")
    print(f"    diya.deposit(1599.50)    -> {diya.deposit(1_599.50):>12,.2f}")
    print(f"    kabir.deposit(3000)      -> {kabir.deposit(3_000):>12,.2f}")
    print(f"    meera.withdraw(250)      -> {meera.withdraw(250):>12,.2f}")
    print()

    print("    after")
    balances(accounts)
    print()
    print("    Every call changed exactly one object. deposit() and withdraw()")
    print("    return the new balance, so a caller never has to guess.")


# ---------------------------------------------------------------- 3

def demo_3_validation(accounts):
    title(3, "The validation - you cannot take out what is not there")

    kabir = accounts[2]
    print(f"    Kabir's balance: {kabir.check_balance():,.2f}")
    print()

    cases = [
        ("more than the balance", lambda: kabir.withdraw(9_999)),
        ("exactly one rupee over", lambda: kabir.withdraw(3_001)),
        ("a negative amount", lambda: kabir.withdraw(-500)),
        ("zero", lambda: kabir.deposit(0)),
        ("a string", lambda: kabir.deposit("2000")),
        ("True", lambda: kabir.deposit(True)),
        ("above the per-transaction limit", lambda: kabir.withdraw(60_000)),
    ]

    for label, call in cases:
        try:
            call()
        except BankError as error:
            print(f"    {label:<32}{type(error).__name__}")
            print(f"    {'':<32}  {error}")

    print()
    print(f"    Kabir's balance is still {kabir.check_balance():,.2f} - a refused")
    print("    withdrawal changes nothing. The check happens before the")
    print("    subtraction, not after it.")
    print()
    print("    And the boundary that is allowed:")
    print(f"      kabir.withdraw(3000)   -> {kabir.withdraw(3_000):,.2f}")
    kabir.deposit(3_000)


# ---------------------------------------------------------------- 4

def demo_4_transfer(accounts):
    title(4, "transfer_to() - two objects in one call")

    aarav, diya = accounts[0], accounts[1]

    print(f"    before   Aarav {aarav.check_balance():>12,.2f}"
          f"   Diya {diya.check_balance():>12,.2f}")
    aarav.transfer_to(diya, 4_000)
    print("    aarav.transfer_to(diya, 4000)")
    print(f"    after    Aarav {aarav.check_balance():>12,.2f}"
          f"   Diya {diya.check_balance():>12,.2f}")

    print()
    print("    A transfer that cannot be afforded moves nothing:")
    before = (aarav.check_balance(), diya.check_balance())
    try:
        aarav.transfer_to(diya, 40_000)
    except BankError as error:
        print(f"      {type(error).__name__}: {error}")
    after = (aarav.check_balance(), diya.check_balance())
    print(f"      balances before {before}")
    print(f"      balances after  {after}")
    print()
    print("    withdraw() runs first and raises, so deposit() is never reached.")
    print("    Ordering the two calls the other way round would credit Diya")
    print("    with money Aarav never had.")


# ---------------------------------------------------------------- 5

def demo_5_details(accounts):
    title(5, "display_account_details()")

    for account in accounts[:2]:
        account.display_account_details()
        print()

    print("    Each account keeps its own history list, built in __init__.")
    print(f"    Aarav has {len(accounts[0].history)} movements, "
          f"Kabir has {len(accounts[2].history)}.")


# ---------------------------------------------------------------- 6

def demo_6_class_members(accounts):
    title(6, "The class variable and the class method")

    print(f"    BankAccount.bank_name  -> {BankAccount.bank_name}")
    print("    Every account reads the same one:")
    for account in accounts[:3]:
        print(f"      {account.holder_name:<16}{account.bank_name}")

    print()
    print("    BankAccount.rename_bank('Nova Federal Bank')")
    BankAccount.rename_bank("Nova Federal Bank")
    print(f"    BankAccount.bank_name  -> {BankAccount.bank_name}")
    print()
    for account in accounts[:3]:
        print(f"      {account.holder_name:<16}{account.bank_name}")

    print()
    print("    Four objects changed and not one of them was touched, because")
    print("    the name was never copied into them. rename_bank() assigns to")
    print("    cls.bank_name - the single shared copy.")

    print()
    print("    The trap, for contrast:")
    rogue = accounts[3]
    rogue.bank_name = "Rogue Bank"
    print("      meera.bank_name = 'Rogue Bank'")
    print(f"      meera.bank_name        -> {rogue.bank_name}")
    print(f"      BankAccount.bank_name  -> {BankAccount.bank_name}")
    print(f"      aarav.bank_name        -> {accounts[0].bank_name}")
    print("    Assigning through the object made an instance variable that")
    print("    hides the class variable - for that one account only.")
    del rogue.bank_name
    print(f"      del meera.bank_name    -> {rogue.bank_name}  (the shared one is back)")

    print()
    print(f"    BankAccount.total_accounts        -> {BankAccount.total_accounts}")
    print(f"    BankAccount.get_total_accounts()  -> "
          f"{BankAccount.get_total_accounts()}")


def main():
    print()
    print(LINE)
    print("  EXERCISE 27 - Bank Account System")
    print("  Class variables, class methods, and refusing a bad withdrawal")
    print(LINE)

    accounts = demo_1_opening()
    demo_2_deposit_withdraw(accounts)
    demo_3_validation(accounts)
    demo_4_transfer(accounts)
    demo_5_details(accounts)
    demo_6_class_members(accounts)

    print()
    print(LINE)
    print(f"  {BankAccount.get_total_accounts()} accounts, one bank name, "
          f"one counter.")
    print("  Not one rupee left an account that did not have it.")
    print(LINE)
    print()


if __name__ == "__main__":
    main()
