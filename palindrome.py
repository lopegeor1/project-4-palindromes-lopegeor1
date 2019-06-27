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

    userinput = userinput.upper()

    parsedinputvalue = deque()

    for char in userinput:
        parsedinputvalue.append(char)

    if  userinput == "":
        stillequal = False

    elif len(userinput) == 1:
        stillequal = True

    elif len(userinput) > 1:
        #at beginning of while loop assume conditions are true (that the first
        #character and last character are both the same).  While true perform
        #test i.e. pop the first and last character of string 'parsedinputvalue'
        #and compare them to find out if they are the same.
        stillequal = True
        while len(parsedinputvalue) > 1 and stillequal:
            first_char = parsedinputvalue.popleft()
            last_char = parsedinputvalue.pop()
            if first_char != last_char:
                #if they are not the same return False
                stillequal = False

    return stillequal
