#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        klist = list(a_dictionary)
        kmax = klist[0]
        for k in klist:
            if a_dictionary[kmax] < a_dictionary[k]:
                kmax = k
        return kmax
    else:
        return None
