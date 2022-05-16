#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cn = 0
    for item in (my_list):
        try:
            print(item, end="")
            cn += 1
        except IndexError:
            print("Out of Range")
        except:
            print("An unknow error ocurred")
    print("")
    return (cn)
