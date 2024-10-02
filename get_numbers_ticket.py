import random

MAX_NUMBER = 1000
MIN_NUMBER = 1


def get_numbers_ticket(
    min: int = MIN_NUMBER, max: int = MAX_NUMBER, quantity: int = 6
) -> list:
    """
    This module provides a function to generate a ticket with random numbers.
    Functions:
        get_numbers_ticket(min: int, max: int, quantity: int) -> list:
            Generates a ticket with random numbers.
            Parameters:
                min (int): The minimum value of the ticket.
                max (int): The maximum value of the ticket.
                quantity (int): The quantity of numbers on the ticket.
            Returns:
                list: The ticket with random numbers.
    For more information, see the README at:
        https://github.com/NewMalicious1986/goit-pycore-hw-03/blob/main/README.md#завдання-2
    """

    if max > MAX_NUMBER or min < MIN_NUMBER or min > max:
        return []

    ticket = random.sample(range(min, max + 1), quantity)

    return sorted(ticket)