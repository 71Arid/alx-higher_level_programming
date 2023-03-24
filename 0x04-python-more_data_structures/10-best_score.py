#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = None
    max_key = None
    for k, v in a_dictionary.items():
        if max_score is None or v > max_score:
            max_score = v
            max_key = k
    return max_key
