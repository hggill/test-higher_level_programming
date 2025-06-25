#!/usr/bin/python3
# Write a function that prints a string in uppercase followed by a new line.
def uppercase(str):
    result = ""
    for c in str:
        if ord(c) in range(97, 123):
            result += chr(ord(c) - 32)
        else:
            result += c
    print('{}'.format(result))
