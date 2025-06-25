#!/usr/bin/python3
# Write a program that prints the ASCII alphabet,
# in reverse order, alternating lowercase and uppercase
# (z in lowercase and Y in uppercase) , not followed by a new line.
print("{}".format(
    "".join(chr(i-32)
            if i % 2 != 0
            else chr(i)
            for i in range(122, 96, -1))), end='')
