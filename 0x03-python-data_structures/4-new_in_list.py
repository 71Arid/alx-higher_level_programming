#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_listcpy = my_list
    if idx < 0 or idx > len(my_listcpy) - 1:
        return my_listcpy
    else:
        my_listcpy[idx] = element
        return my_listcpy
