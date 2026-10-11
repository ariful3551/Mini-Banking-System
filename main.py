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

from banking.data import session
from banking.auth import login, logout
from banking.menu import display_menu
from banking.operations import (
    check_balance,
    deposit,
    withdraw,
    view_transaction_history,
    exit_program,
)


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
        if session["current_user"] is None:
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
    # Runs only when executed directly, not when imported as a module.
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



"""
===============================================================================
LEARNING CONCEPTS COVERED
===============================================================================

1.  Variables                  - Storing data in memory
2.  Data Types                 - str, int, float, list, dict
3.  Input / Output             - input() and print()
4.  Type Casting               - int(), float(), str()
5.  Arithmetic Operators       - +, -, +=, -= 
6.  Comparison Operators       - ==, !=, >, <, >=, <=
7.  Conditional Statements     - if, elif, else
8.  While Loop                 - Main program loop
9.  For Loop                   - Iterating through transactions
10. Functions                  - Modular code organization
11. Global Variables           - current_user
12. Lists                      - transaction history
13. Dictionaries               - Nested user data
14. List Methods               - append()
15. String Formatting          - f-strings
16. Match-Case Statements      - Menu selection
17. User Authentication        - Login system
18. Session Management         - current_user tracking
19. Balance Management         - Deposit and withdraw logic
20. Transaction Tracking       - History recording
21. Menu-Driven Programming    - Interactive CLI
22. Program Flow Control       - Nested loops and break
23. Error Handling             - try-except blocks
24. Input Validation           - Data validation
25. Type Hints                 - Type annotations
26. Docstrings                 - Function documentation
27. Constants                  - UPPERCASE naming
28. Modular Design             - Separate functions
29. Exit Handling              - Graceful shutdown
30. Software Design Thinking   - Clean architecture
 """
