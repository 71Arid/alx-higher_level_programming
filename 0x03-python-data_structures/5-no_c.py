def no_c(my_string):
    my_stringcpy = ""
    c = "c"
    C = "C"
    for i in range(len(my_string)):
        if my_string[i] != C and my_string[i] != c:
            my_stringcpy = my_stringcpy + my_string[i]
    return my_stringcpy
