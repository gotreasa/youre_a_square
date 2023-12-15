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
