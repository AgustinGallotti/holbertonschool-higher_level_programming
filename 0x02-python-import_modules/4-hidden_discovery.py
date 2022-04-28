#!/usr/bin/python3
#ignore in compilation
if __name__ == '__main__':
    import sys
    import hidden_4
    #access to directory
    for i in dir(hidden_4):
        #__hidden__ exapmle of before [:2] = "__"
        if i[:2] != "__":
            print(i)
