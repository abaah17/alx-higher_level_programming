#!/usr/bin/env python3
def no_c(my_string):
    str1 = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            str1 += x
    return str1
