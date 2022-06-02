#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    last_d = int(number[-1])
    number = int(number)
    if number < 0:
        last_d
    else:
        abs(last_d)
    print("{:d}".format(last_d), end='')
    return last_d
