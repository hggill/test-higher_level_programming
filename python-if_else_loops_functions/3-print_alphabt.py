#!/usr/bin/python3
print("{}".format("".join(
    chr(i) for i in range(97, 123)
    if chr(i) != 'e' and chr(i) != 'q'
)), end='')
