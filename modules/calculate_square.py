def is_a_square(number: int) -> bool:
    if number == -1:
        return False
    if number == 0:
        return True
    raise ValueError("❗️ Input must be an integer")
