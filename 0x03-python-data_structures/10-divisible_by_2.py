#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiples = []
    for i in my_list:
        multiples.append(i % 2 == 0)
    return multiples
