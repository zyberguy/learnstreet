#string defs project
def revers(str):
    # Accept an input string, str, and reverse its characters in order
    #"REPLACE THIS CODE WITH YOUR CONVERSION METHOD"
    rev = ""
    str_length = str.__len__()-1
    for i in range(str_length,-1,-1):
        rev += str[i]
    return rev

def uppercase(str):
    # Convert all the characters of the input string, str, to upper
    # case. Reurn the uppercased string.
    #"REPLACE THIS CODE WITH YOUR CONVERSION METHOD"
    uppercased = str.upper()
    return uppercased

def palindrome(str):
    # Check if the input string, str, is spelled the same forwards
    # as it is spelled backwards.
    # Return "is a palindrome" if it is, or "is not a palindrome" if it is not.
    #"REPLACE THIS CODE WITH YOUR CONVERSION METHOD"
    u = uppercase(str)
    r = revers(u)
    if r == u:
        return "is a palindrome"
    else:
        return "is not a palindrome"