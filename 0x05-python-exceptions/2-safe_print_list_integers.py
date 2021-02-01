#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    real_n = 0
    for i in range(0,x):
        try:
            print("{}".format(my_list[i]), end="")
            real_n += 1
        except (ValueError, TypeError):
            continue
    print("")
    return real_n
