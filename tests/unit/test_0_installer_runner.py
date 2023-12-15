import pytest
from modules import calculate_square


def describe_is_a_square():
    def should_error_when_not_an_integer(capsys):
        """🧪 should give an error when the value being checked is not an integer"""
        with pytest.raises(ValueError, match="❗️ Input must be an integer"):
            calculate_square.is_a_square("blah")
