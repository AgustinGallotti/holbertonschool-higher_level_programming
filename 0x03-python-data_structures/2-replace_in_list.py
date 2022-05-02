#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for idx, element in enumerate(my_list):
        if element == 4: #or "== my_list[idx:x]
            my_list[idx] = 9

    print(my_list)
