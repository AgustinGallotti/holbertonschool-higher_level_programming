#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cn = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            cn += 1
    except IndexError as error:
        pass
    print()
    return (cn)
