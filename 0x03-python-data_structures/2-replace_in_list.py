#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    elif idx >= len(my_list):
        return (my_list)
    else:
        for idx, element in enumerate(my_list):
            if element == 4:
                my_list[idx] = 9

        return (my_list)
