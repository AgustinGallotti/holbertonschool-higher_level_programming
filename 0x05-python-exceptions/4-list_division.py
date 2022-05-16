#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_lenght):
    my_list_3 = []
    for i in range(list_lenght):
        quotient = 0
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
           my_list_3.append(quotient)
    return my_list_3

