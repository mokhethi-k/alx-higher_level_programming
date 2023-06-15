#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weighted = 0
    sumed = 0
    for score, weight in my_list:
        weighted += weight
        sumed += score * weight

    return sumed / weighted
