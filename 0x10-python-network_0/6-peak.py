#!/usr/bin/python3
""" . """


def find_peak(list_of_integers):
    """ . """
    listt = list_of_integers.copy()
    for idx in range(len(listt)):
        if (idx - 1) >= 0 and (idx + 1) <= (len(listt) - 1):
            if listt[idx] >= listt[idx - 1] and listt[idx] >= listt[idx + 1]:
                return listt[idx]
        if (idx - 1) < 0:
            if listt[idx] >= listt[idx + 1]:
                return listt[idx]
        if (idx + 1) > (len(listt) - 1):
            if listt[idx] >= listt[idx - 1]:
                return listt[idx]

    return None