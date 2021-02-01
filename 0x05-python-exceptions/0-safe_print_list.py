#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    real_n = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            real_n += 1
        except IndexError:
            break
        print("")
        return real_n
