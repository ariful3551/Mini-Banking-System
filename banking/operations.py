"""
Banking operations module.

Contains balance check, deposit, withdrawal, transaction history
and program exit.
"""

import sys

from banking.data import USERS, session


def check_balance() -> None:
    """
    Display the current balance of the logged-in user.

    Returns:
        None: Prints balance to console.
    """
    user = session["current_user"]

    # Validate user is logged in
    if user is None:
        print("Error: Please login first!")
        return

    balance = USERS[user]["balance"]
    print(f"Your current balance: ${balance:.2f}")


def deposit() -> None:
    """
    Deposit money into the current user's account.

    Prompts user for amount, validates input, updates balance,
    and records transaction.

    Returns:
        None: Updates user data in memory.
    """
    user = session["current_user"]

    # Validate user is logged in
    if user is None:
        print("Error: Please login first!")
        return

    try:
        amount = float(input("Enter amount to deposit: $"))
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    # Validate amount is positive
    if amount <= 0:
        print("Error: Deposit amount must be greater than zero.")
        return

    # Process deposit
    USERS[user]["balance"] += amount
    USERS[user]["transactions"].append(
        f"Deposit: +${amount:.2f}"
    )
    print(f"Deposit successful! New balance: ${USERS[user]['balance']:.2f}")


def withdraw() -> None:
    """
    Withdraw money from the current user's account.

    Prompts user for amount, validates sufficient balance,
    updates balance, and records transaction.

    Returns:
        None: Updates user data in memory.
    """
    user = session["current_user"]

    # Validate user is logged in
    if user is None:
        print("Error: Please login first!")
        return

    try:
        amount = float(input("Enter amount to withdraw: $"))
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    # Validate amount is positive
    if amount <= 0:
        print("Error: Withdrawal amount must be greater than zero.")
        return

    # Check sufficient balance
    if USERS[user]["balance"] < amount:
        print(f"Error: Insufficient balance. Available: ${USERS[user]['balance']:.2f}")
        return

    # Process withdrawal
    USERS[user]["balance"] -= amount
    USERS[user]["transactions"].append(
        f"Withdrawal: -${amount:.2f}"
    )
    print(f"Withdrawal successful! New balance: ${USERS[user]['balance']:.2f}")


def view_transaction_history() -> None:
    """
    Display all transactions for the current user.

    Shows transaction history with numbered entries.

    Returns:
        None: Prints transaction history to console.
    """
    user = session["current_user"]

    # Validate user is logged in
    if user is None:
        print("Error: Please login first!")
        return

    transactions = USERS[user]["transactions"]

    # Check if there are any transactions
    if not transactions:
        print("No transactions found.")
        return

    print("\n" + "=" * 40)
    print("       TRANSACTION HISTORY")
    print("=" * 40)

    for index, transaction in enumerate(transactions, start=1):
        print(f"{index:2}. {transaction}")

    print("=" * 40)


def exit_program() -> None:
    """
    Exit the banking system gracefully.

    Returns:
        None: Terminates program.
    """
    print("\n" + "=" * 40)
    print("Thank you for using the Mini Banking System!")
    print("   Have a great day!")
    print("=" * 40)
    sys.exit(0)