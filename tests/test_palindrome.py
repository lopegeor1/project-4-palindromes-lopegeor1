# pylint: disable=missing-docstring
"""
The test module for Palindromes
"""
import pytest

from palindrome import is_palindrome

def test_invalid_input():
    """
    Given incorrect type input , a ValueError should be raised.
    """
    with pytest.raises(ValueError):
        is_palindrome(12345)

def test_null_value_input():
    """
    Given null input , validation test should return False.
    """
    assert not is_palindrome("")

def test_value_called_a():
    """
    Given input: is_palindrome returns True if called with "a"
    """
    assert is_palindrome("a")
