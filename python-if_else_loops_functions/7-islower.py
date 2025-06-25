#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        print(f'{c} is lower')
    elif ord(c) in range(65, 91):
        print(f'{c} is upper')
