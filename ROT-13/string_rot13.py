from string import ascii_uppercase, ascii_lowercase
import math
def string_rot13(str):
    total = []
    for s in str:
        if s in ascii_uppercase:
            index = (ascii_uppercase.find(s) + 13) % 26
            total.append(ascii_uppercase[index])
        elif s in ascii_lowercase:
            index = (ascii_lowercase.find(s) + 13) % 26
            total.append(ascii_lowercase[index])
        else:
            total.append(s)
    return "".join(total)

