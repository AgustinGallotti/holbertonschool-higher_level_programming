#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = len(sys.argv)
    adding = 0

    for i in range(1, arguments):
        adding += int(sys.argv[i])
    print(f"{adding}")
