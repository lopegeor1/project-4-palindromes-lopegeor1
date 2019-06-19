"""
palindrome.py -- Write the application code here
"""
# if not already done then install via
# "pip install pythonds"
#from pythonds.basic.deque import Deque
class Deque:
    """
    manually added Deque function
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        manually added Deque function
        """
        return self.items == []

    def add_front(self, item):
        """
        manually added Deque function
        """
        self.items.append(item)

    def add_rear(self, item):
        """
        manually added Deque function
        """
        self.items.insert(0, item)

    def remove_front(self):
        """
        manually added Deque function
        """
        return self.items.pop()

    def remove_rear(self):
        """
        manually added Deque function
        """
        return self.items.pop(0)

    def size(self):
        """
        manually added Deque function
        """
        return len(self.items)

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

    for char in inputs:
        chardeque.add_rear(char)

    if  inputs == "":
        stillequal = False

    elif len(inputs) == 1:
        stillequal = True

    elif len(inputs) > 1:
        stillequal = True
        while chardeque.size() > 1 and stillequal:
            first = chardeque.remove_front()
            last = chardeque.remove_rear()
            if first != last:
                stillequal = False

    return stillequal

#INPUTVAR = str(input("Please Enter an string: "))
#print(is_palindrome(INPUTVAR))
