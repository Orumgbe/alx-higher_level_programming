#!/usr/bin/python3


def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""
    uniq_list = list(set(my_list)) 
    total = 0
    for elem in uniq_list:
        total = total + elem
    return total
