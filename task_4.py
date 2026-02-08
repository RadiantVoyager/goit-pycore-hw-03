from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list) -> list:
    """
    Get the upcoming birthdays of users for the future 7 days.
    Args:
       users: A list of dictionaries containing users names and birthdays.
    Returns:
       A list of dictionaries containing users names and upcoming birthdays.
    """
    today_date = datetime.today().date()
    seven_days_around_birthdays = []
    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        try:
            upd_birthday_with_current_year = birthday_date.replace(year=today_date.year)
        except ValueError:
            upd_birthday_with_current_year = birthday_date.replace(
                year=today_date.year, month=3, day=1
            )

        if upd_birthday_with_current_year < today_date:
            try:
                upd_birthday_with_current_year = upd_birthday_with_current_year.replace(
                    year=today_date.year + 1
                )
            except ValueError:
                upd_birthday_with_current_year = upd_birthday_with_current_year.replace(
                    year=today_date.year + 1, month=3, day=1
                )

        birthday_day_of_week = upd_birthday_with_current_year.weekday()
        shift = 7 - birthday_day_of_week if birthday_day_of_week > 4 else 0
        upd_birthday_with_current_year += timedelta(days=shift)

        if (
            today_date
            <= upd_birthday_with_current_year
            <= (today_date + timedelta(days=7))
        ):
            celebration_date = {
                "name": user["name"],
                "congratulation_date": upd_birthday_with_current_year.strftime(
                    "%Y.%m.%d"
                ),
            }
            seven_days_around_birthdays.append(celebration_date)
    return seven_days_around_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.02.13"},
    {"name": "Jane Smith", "birthday": "1990.02.23"},
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
