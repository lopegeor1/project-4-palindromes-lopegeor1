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

    if inputs == "":
        stillequal = False

    if len(inputs) == 1:
        stillequal = True
    return stillequal

#INPUTVAR = str(input("Please Enter an string: "))
#print(is_palindrome(INPUTVAR))
