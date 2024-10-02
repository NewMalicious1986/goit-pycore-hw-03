from datetime import datetime

"""
This module provides a function to calculate the number of days from a given date to today.
Functions:
    get_days_from_today(date: str) -> int:
        Calculates the number of days from the given date to today.
        Parameters:
            date (str): The date in the format 'YYYY-MM-DD'.
        Returns:
            int: The number of days from the given date to today.
        Raises:
            ValueError: If the date string is not in the correct format.
For more information, see the README at:
https://github.com/NewMalicious1986/goit-pycore-hw-03/blob/main/README.md#завдання-1
"""


def get_days_from_today(date: str, format: str = "%Y-%m-%d") -> int:
    try:
        date_object = datetime.strptime(date, format)
        date_now = datetime.today()
        delta = date_now - date_object
        return delta.days

    except ValueError:
        raise ValueError(
            "The date string is not in the correct format. Please use 'YYYY-MM-DD'."
        )
