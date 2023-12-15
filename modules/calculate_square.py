import math


def is_a_square(number: int) -> bool:
    if not isinstance(number, int):
        raise ValueError("❗️ Input must be an integer")

    return number >= 0 and math.sqrt(number) % 1 == 0
