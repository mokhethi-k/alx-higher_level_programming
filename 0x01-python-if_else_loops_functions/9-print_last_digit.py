#!/usr/bin/python3
def print_last_digit(number):
    l_number = abs(number) % 10
    print(l_number, end="")
    return l_number
