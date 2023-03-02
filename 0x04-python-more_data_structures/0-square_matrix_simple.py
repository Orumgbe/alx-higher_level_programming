#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Computes square values of all integers of a matrix"""
    new_matrix = []
    for i in range(len(matrix[0])):
        nlist = []
        for elem in matrix[i]:
            nlist.append(elem ** 2)
        new_matrix.append(nlist)
    return new_matrix
