import pytest
from modules import calculate_square


def describe_is_a_square():
    def should_error_when_not_an_integer():
        """🧪 should give an error when the value being checked is not an integer"""
        with pytest.raises(ValueError, match="❗️ Input must be an integer"):
            calculate_square.is_a_square("blah")

    def should_return_false_when_negative_one():
        """🧪 should take -1 and return false"""
        assert calculate_square.is_a_square(-1) == False

    def should_return_true_when_zero():
        """🧪 should take 0 and return true"""
        assert calculate_square.is_a_square(0) == True

    def should_return_false_when_three():
        """🧪 should take 3 and return false"""
        assert calculate_square.is_a_square(3) == False

    def should_return_true_when_four():
        """🧪 should take 4 and return true"""
        assert calculate_square.is_a_square(4) == True

    def should_return_true_when_twenty_five():
        """🧪 should take 25 and return true"""
        assert calculate_square.is_a_square(25) == True
