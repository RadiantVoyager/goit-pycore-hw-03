from datetime import datetime


def get_days_from_today(date: str) -> int:
    """Calculate the number of days between a given date and today's date.
    Args:
        date: A date in 'YYYY-MM-DD' format.
    Returns:
        The difference in days
    """
    try:
        provided_date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.now().date()
        days_difference = (current_date - provided_date).days
        return int(days_difference)
    except ValueError:
        raise ValueError(f"Invalid input format {date}. Please use YYYY-MM-DD.")


print(get_days_from_today("2021-10-04"))
