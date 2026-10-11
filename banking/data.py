"""
Data module.

Stores the user database and the session state shared across all modules.
"""

from typing import Dict, List, Optional, Union

# User database - stores all user accounts
# Structure: {username: {password: int, balance: float, transactions: List[str]}}
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

# Session state - tracks the currently logged-in user.
# A dictionary is used (instead of a plain variable) so that every module
# can modify the same shared value.
session: Dict[str, Optional[str]] = {"current_user": None}