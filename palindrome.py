"""
palindrome.py -- Write the application code here
"""
# if not already done then install via
# "pip install pythonds"
from pythonds.basic.deque import Deque

def is_palindrome(inputs):
    """
    Determines if given input variable or string is
    a palindrome.
    """
    if not isinstance(inputs, str):
        raise ValueError

#INPUTVAR = int(input("Please Enter an string: "))
#print(is_palindrome("INPUTVAR"))
