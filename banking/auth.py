"""
Authentication module.

Handles user login and logout.
"""

from banking.data import USERS, session


def login() -> None:
    """
    Authenticate user by validating username and password.

    Prompts user for credentials and sets the current user in the
    session if authentication is successful.

    Returns:
        None: Updates session["current_user"] or leaves it as None on failure.
    """
    # Get username input
    username = input("Enter your username: ").strip()

    # Check if user exists
    if username not in USERS:
        print(f"Error: User '{username}' does not exist.")
        session["current_user"] = None
        return

    # Get password input (with error handling for non-integer input)
    try:
        password = int(input("Enter your password: "))
    except ValueError:
        print("Error: Password must be a number.")
        session["current_user"] = None
        return

    # Validate password
    if USERS[username]["password"] == password:
        print(f"Access granted! Welcome, {username}.")
        session["current_user"] = username
    else:
        print("Error: Incorrect password.")
        session["current_user"] = None


def logout() -> None:
    """
    Log out the current user by clearing the session.

    Returns:
        None: Sets session["current_user"] to None.
    """
    session["current_user"] = None
    print("Logged out successfully.")