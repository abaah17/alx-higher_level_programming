def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None
    for i in my_list:
        print("{:d}".format(my_list[-i]))
