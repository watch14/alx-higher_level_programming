#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("0 arguments:")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arguments))

    for i in range(1, len(sys.argv)
        print("{}: {}".format(i, sys.argv[i]))

