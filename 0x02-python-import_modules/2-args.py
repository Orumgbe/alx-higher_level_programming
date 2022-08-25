#!/usr/bin/python3
import sys
if __name__ == "__main__":
    list_num = len(sys.argv)
    if list_num == 1:
        print("{:d} arguments.".format(0))
    elif list_num == 2:
        print("{:d} argument:".format(1))
    else:
        print("{:d} arguments:".format(list_num - 1))
    for i in range(list_num): 
        if i == 0:
            continue 
        print("{:d}: {:s}".format(i, sys.argv[i]))
