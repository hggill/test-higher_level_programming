#!/usr/bin/python3
# Write a function that creates a copy of the string,
# removing the character at the position n
# (not the Python way, the “C array index”)
def remove_char_at(str, n):
    result = ''
    for i in range(0, len(str)):
        if i != n:
            result += str[i]
    return result
