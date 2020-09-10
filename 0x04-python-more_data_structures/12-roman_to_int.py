#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is str and roman_string:
        conv_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        total = 0
        for r1, r2 in zip(roman_string, roman_string[1:]):
            if conv_dict[r1] < conv_dict[r2]:
                total -= conv_dict[r1]
            else:
                total += conv_dict[r1]
        total += conv_dict[roman_string[-1]]
        return total
    else:
        return 0
