import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Randomly generates a specified number of unique random numbers within a given range.
    Args:
        min: The minimum value of the range.
        max: The maximum value of the range.
        quantity: The number of random numbers to generate.
    Returns:
        A list of random numbers within the specified range.
    """
    if min >= 1 and max <= 1000:
        unique_selected_digits = []
        while len(unique_selected_digits) != quantity:
            selected_digits = random.choices(range(min, max), k=quantity)
            unique_selected_digits = list(set(selected_digits))
        unique_selected_digits.sort()
        return unique_selected_digits
    else:
        return []


lottery_numbers = get_numbers_ticket(2, 1000, 10)
print(f"Ваші лотерейні числа: {lottery_numbers}")
