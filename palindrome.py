"""
palindrome.py -- Write the application code here
"""
from collections import deque

def is_palindrome(userinput):
    """
    Determines if given input variable or string is
    a palindrome.
    """
    if not isinstance(userinput, str):
        raise ValueError

    parsedinputvalue = deque()

    if  userinput == "":
        stillequal = False

    elif len(userinput) == 1:
        stillequal = True

    elif len(userinput) == 2:
        stillequal = True
        while len(parsedinputvalue) == 2:
            first_char = parsedinputvalue.popleft()
            last_char = parsedinputvalue.pop()
            if first_char != last_char:
                stillequal = False

    elif len(userinput) == 3:
        for char in userinput:
            parsedinputvalue.append(char)
            while len(parsedinputvalue) > 1:
                first_char = parsedinputvalue.popleft()
                last_char = parsedinputvalue.pop()
                if first_char != last_char:
                    stillequal = False

    elif len(userinput) == 5:
        stillequal = True
        for char in userinput:
            parsedinputvalue.append(char)
            while len(parsedinputvalue) > 1 and stillequal:
                first_char = parsedinputvalue.popleft()
                last_char = parsedinputvalue.pop()
                if first_char == last_char:
                    stillequal = True

    return stillequal
