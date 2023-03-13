#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        res = number * -1
        rem = res % 10
        print(rem, end="")
        return rem
    else:
        rem = number % 10
        print(rem, end="")
        return rem
