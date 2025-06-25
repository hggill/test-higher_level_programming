#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        print(f'{c} is lower')
    elif ord(c) in range(65, 91):
        print(f'{c} is upper')
    else:
        print(f'{c} is not a letter')


for i in range(65, 123):
    islower(chr(i))
