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

    if isinstance(inputs, int):
        raise ValueError

    inputs = inputs.upper()

    chardeque = Deque()

    for ch in inputs:
        chardeque.addRear(ch)

    if  inputs == "":
        stillequal = False

    elif len(inputs) == 1:
        stillequal = True

    elif len(inputs) > 1:
        stillequal = True
        while chardeque.size() > 1 and stillequal:
            first = chardeque.removeFront()
            last = chardeque.removeRear()
            if first != last:
                stillequal = False

    return stillequal

#INPUTVAR = str(input("Please Enter an string: "))
#print(is_palindrome(INPUTVAR))
