#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by another"""
    index = my_list.index(search)
    nlist = my_list.copy()
    nlist[index] = replace
    return nlist
