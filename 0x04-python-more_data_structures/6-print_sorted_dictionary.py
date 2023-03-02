#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    keylist = sorted(a_dictionary.keys())
    for k in keylist:
        print("{:s}: {}".format(k, a_dictionary[k]))
