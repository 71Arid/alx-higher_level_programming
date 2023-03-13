#!/usr/bin/python3
def islower(c):
    num = ord(c)
    for i in range(97, 123):
        if i == num:
            return True
        elif num > i and num < i:
            return False
