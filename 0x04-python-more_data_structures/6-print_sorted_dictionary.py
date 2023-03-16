#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_1 = list(a_dictionary.keys())
    key_1.sort()
    for i in key_1:
        print("{}: {}".format(i, a_dictionary.get(i)))
