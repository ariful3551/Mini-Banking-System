"""
Menu module.

Displays the main menu to the user.
"""


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