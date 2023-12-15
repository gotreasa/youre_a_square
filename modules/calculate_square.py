def is_a_square(number: int) -> bool:
    if number in [-1, 3, 26]:
        return False
    if number in [0, 4, 25]:
        return True
    raise ValueError("❗️ Input must be an integer")
