#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    wscore = 0
    wtotal = 0

    for s, w in my_list:
        wscore += s * w
        wtotal += w
    return wscore/wtotal
