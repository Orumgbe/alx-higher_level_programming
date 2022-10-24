#!/usr/bin/python3
"""Adds all argument to a python list"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":

    filename = "add_item.json"

    try:
        arg_list = load_from_json_file(filename)
    except FileNotFoundError:
        arg_list = []
    except ValueError:
        arg_list = []

    for i in range(1, len(sys.argv)):
        arg_list.append(sys.argv[i])

    save_to_json_file(arg_list, filename)