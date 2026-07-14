"""
Mini Banking System - Professional Edition
===========================================

A command-line banking application demonstrating core Python concepts:
- User authentication
- Account management (balance, deposits, withdrawals)
- Transaction history tracking
- Session management

This project is designed for learning purposes to practice:
- Variables, Data Types, Input/Output
- Conditional Statements, Loops, Functions
- Lists, Dictionaries, Match-Case
- Problem-Solving and Software Design

Author: [Ariful Islam]
Date: 2026
Version: 1.0.0
"""

import sys
from typing import Dict, List, Optional, Union


# ============================================
# CONSTANTS & CONFIGURATION
# ============================================

# User database - stores all user accounts
# Structure: {username: {password: int, balance: float, transaction: List[str]}}
USERS: Dict[str, Dict[str, Union[int, float, List[str]]]] = {
    "max": {
        "password": 1234,
        "balance": 0.0,
        "transactions": []
    },
    "leon": {
        "password": 1235,
        "balance": 0.0,
        "transactions": []
    },
    "jonas": {
        "password": 1236,
        "balance": 0.0,
        "transactions": []
    },
    "felix": {
        "password": 1237,
        "balance": 0.0,
        "transactions": []
    }
}

# Global session variable - tracks currently logged-in user
current_user: Optional[str] = None


# ============================================
# AUTHENTICATION FUNCTIONS
# ============================================

def login() -> None:
    """
    Authenticate user by validating username and password.

    Prompts user for credentials and sets the global current_user
    if authentication is successful.

    Returns:
        None: Sets current_user globally or leaves as None on failure.
    """
    global current_user

    # Get username input
    username = input("Enter your username: ").strip()

    # Check if user exists
    if username not in USERS:
        print(f"Error: User '{username}' does not exist.")
        current_user = None
        return

    # Get password input (with error handling for non-integer input)
    try:
        password = int(input("Enter your password: "))
    except ValueError:
        print("Error: Password must be a number.")
        current_user = None
        return

    # Validate password
    if USERS[username]["password"] == password:
        print(f"Access granted! Welcome, {username}.")
        current_user = username
    else:
        print("Error: Incorrect password.")
        current_user = None


def logout() -> None:
    """
    Log out the current user by clearing the session.

    Returns:
        None: Sets current_user to None.
    """
    global current_user
    current_user = None
    print("Logged out successfully.")


# ============================================
# MENU FUNCTIONS
# ============================================

def display_menu() -> None:
    """
    Display the main menu options to the user.

    Returns:
        None: Prints menu to console.
    """
    print("\n" + "=" * 40)
    print("         MINI BANKING SYSTEM")
    print("=" * 40)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Logout")
    print("6. Exit Program")
    print("=" * 40)


# ============================================
# BANKING OPERATIONS
# ============================================

def check_balance() -> None:
    """
    Display the current balance of the logged-in user.

    Returns:
        None: Prints balance to console.
    """
    # Validate user is logged in
    if current_user is None:
        print("Error: Please login first!")
        return

    balance = USERS[current_user]["balance"]
    print(f"Your current balance: ${balance:.2f}")


def deposit() -> None:
    """
    Deposit money into the current user's account.

    Prompts user for amount, validates input, updates balance,
    and records transaction.

    Returns:
        None: Updates user data in memory.
    """
    # Validate user is logged in
    if current_user is None:
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
    USERS[current_user]["balance"] += amount
    USERS[current_user]["transactions"].append(
        f"Deposit: +${amount:.2f}"
    )
    print(f"Deposit successful! New balance: ${USERS[current_user]['balance']:.2f}")


def withdraw() -> None:
    """
    Withdraw money from the current user's account.

    Prompts user for amount, validates sufficient balance,
    updates balance, and records transaction.

    Returns:
        None: Updates user data in memory.
    """
    # Validate user is logged in
    if current_user is None:
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
    if USERS[current_user]["balance"] < amount:
        print(f"Error: Insufficient balance. Available: ${USERS[current_user]['balance']:.2f}")
        return

    # Process withdrawal
    USERS[current_user]["balance"] -= amount
    USERS[current_user]["transactions"].append(
        f"Withdrawal: -${amount:.2f}"
    )
    print(f"Withdrawal successful! New balance: ${USERS[current_user]['balance']:.2f}")


def view_transaction_history() -> None:
    """
    Display all transactions for the current user.

    Shows transaction history with numbered entries.

    Returns:
        None: Prints transaction history to console.
    """
    # Validate user is logged in
    if current_user is None:
        print("Error: Please login first!")
        return

    transactions = USERS[current_user]["transactions"]

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


# ============================================
# MAIN PROGRAM LOOP
# ============================================

def main() -> None:
    """
    Main program entry point.

    Controls the flow of the application:
    1. User login
    2. Menu display and option selection
    3. Execution of banking operations
    4. Logout or exit

    Returns:
        None: Runs until user exits.
    """
    print("\n" + "=" * 40)
    print("  WELCOME TO MINI BANKING SYSTEM")
    print("=" * 40)

    while True:
        # Step 1: Login
        login()

        # If login failed, try again
        if current_user is None:
            print("\nPlease try logging in again.\n")
            continue

        # Step 2: Main menu loop (while logged in)
        while True:
            display_menu()

            # Get user choice
            choice = input("\nEnter your choice (1-6): ").strip()

            # Process choice using match-case
            match choice:
                case "1":
                    check_balance()

                case "2":
                    deposit()

                case "3":
                    withdraw()

                case "4":
                    view_transaction_history()

                case "5":
                    logout()
                    break  # Exit inner loop, return to login

                case "6":
                    exit_program()

                case _:
                    print("Error: Invalid choice. Please select 1-6.")

            # Add a small pause for readability
            print("\n" + "-" * 40)


# ============================================
# PROGRAM ENTRY POINT
# ============================================

if __name__ == "__main__":
    """
    This ensures the program runs only when executed directly,
    not when imported as a module.
    """
    try:
        main()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nProgram interrupted. Goodbye!")
        sys.exit(0)
    except Exception as error:
        # Catch any unexpected errors
        print(f"\nAn unexpected error occurred: {error}")
        print("   Please restart the program.")
        sys.exit(1)


