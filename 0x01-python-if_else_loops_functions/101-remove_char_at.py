#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = str
    for i in range(len(str_cpy)):
        if i != n:
            print(str_cpy[i], end="")
