#!/usr/bin/python3
# Write a function that prints the numbers from 1 to 100 separated by a space.
def fizzbuzz():
    result = ''
    for i in range(0, 101):
        if i == 0:
            result += f'{i} '
        elif i % 3 == 0 and i % 5 == 0:
            result += "FizzBuzz "
        elif i % 3 == 0:
            result += "Fizz "
        elif i % 5 == 0:
            result += "Buzz "
        else:
            result += f'{i} '
    print(result, end='')
    return result
