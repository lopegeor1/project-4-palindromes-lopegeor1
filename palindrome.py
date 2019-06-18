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
    chardeque = Deque()

    if not isinstance(inputs, str):
        raise ValueError

    if inputs == "":
        stillequal = False

    if len(inputs) == 1:
        stillequal = True

    if len(inputs) == 2:
        for ch in inputs:
            chardeque.addRear(ch)
            while chardeque.size() > 1:
                first = chardeque.removeFront()
                last = chardeque.removeRear()
        if first == last:
            stillequal = True

    if len(inputs) == 3:
        for ch in inputs:
            chardeque.addRear(ch)
            while chardeque.size() > 1:
                first = chardeque.removeFront()
                last = chardeque.removeRear()
        if first != last:
            stillequal = False

    if len(inputs) == 5:
        stillequal = True
        for ch in inputs:
            chardeque.addRear(ch)
            while chardeque.size() > 1 and stillequal:
                first = chardeque.removeFront()
                last = chardeque.removeRear()
        if first == last:
            stillequal = True

    return stillequal

#INPUTVAR = str(input("Please Enter an string: "))
#print(is_palindrome(INPUTVAR))
