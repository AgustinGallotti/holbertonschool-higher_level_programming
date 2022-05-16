#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        my_list = []

        print(my_list[])

    except (IndexError, NameError)

    except IndexError:
        print("Sorry that index doesn't exist")

    except:
        print("An unknoen error ocurred")
