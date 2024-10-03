from datetime import datetime, timedelta

DATE_FORMAT = "%Y.%m.%d"
DAYS_IN_WEEK = 7
WEEKEND_DAYS = [5, 6]  # Saturday and Sunday


def get_upcoming_birthdays(users):
    """
    Get a list of users with upcoming birthdays within the next 7 days.
    Args:
        users (list): A list of dictionaries, where each dictionary contains
                      user information including 'name' and 'birthday' keys.
                      The 'birthday' should be in the format specified by DATE_FORMAT.
    Returns:
        list: A list of dictionaries, where each dictionary contains:
              - 'name': The name of the user.
              - 'next_upcoming_birthday': The date of the next upcoming birthday,
                adjusted to the next Monday if it falls on a weekend.
    """
    today = datetime.now().date()
    upcoming_birthdays = []

    for user in users:
        birthday_this_year = (
            datetime.strptime(user["birthday"], DATE_FORMAT)
            .date()
            .replace(year=today.year)
        )
        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= DAYS_IN_WEEK:
            if birthday_this_year.weekday() in WEEKEND_DAYS:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "next_upcoming_birthday": birthday_this_year.strftime(DATE_FORMAT),
                }
            )

    return upcoming_birthdays
