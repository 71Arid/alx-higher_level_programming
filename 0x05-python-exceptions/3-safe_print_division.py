#!/usr/bin/python3
def safe_print_division(a, b):
    div = 0
    try:
        div = a / b
        return div
    except ZeroDivisionError:
        return None
    else:
        return div
    finally:
        print("Inside result: {}".format(div))
