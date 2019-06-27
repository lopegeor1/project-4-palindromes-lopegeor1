"""
palindrome.py -- Write the application code here
"""
def is_palindrome(userinput):
    """
    Determines if given input variable or string is
    a palindrome.
    """
    if not isinstance(userinput, str):
        raise ValueError

    if  userinput == "":
        stillequal = False

    elif len(userinput) == 1:
        stillequal = True

    return stillequal
