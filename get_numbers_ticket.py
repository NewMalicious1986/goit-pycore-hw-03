import random

MAX_NUMBER = 1000
MIN_NUMBER = 1


def get_numbers_ticket(
    min: int = MIN_NUMBER, max: int = MAX_NUMBER, quantity: int = 1
) -> list:
    """
    Generate a sorted list of unique random numbers within a specified range.

    Args:
        min (int): The minimum number in the range (inclusive). Defaults to MIN_NUMBER.
        max (int): The maximum number in the range (inclusive). Defaults to MAX_NUMBER.
        quantity (int): The number of unique random numbers to generate. Defaults to 1.

    Returns:
        list: A sorted list of unique random numbers within the specified range.
              Returns an empty list if the input parameters are invalid.
    """

    numbers_range = range(min, max + 1)

    if max > MAX_NUMBER or min < MIN_NUMBER or min > max or quantity < 1:
        return []

    ticket = random.sample(numbers_range, quantity)

    return sorted(ticket)


print(get_numbers_ticket(1, 2, 2))
