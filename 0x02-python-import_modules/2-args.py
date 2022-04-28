#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = len(sys.argv) - 1
    itinerate = 1

    if arguments == 0:
        print(f"{argument} {itinerate} arguments.")
    elif arguments == 1:
        prin(f"{arguments} arguments:")
    else:
        print(f"{arguments} arguments:")

    while (arguments >= itinerate):
        print(f"{itinerate}: {sys.argv[itinerate]}")
        itinerate += 1
