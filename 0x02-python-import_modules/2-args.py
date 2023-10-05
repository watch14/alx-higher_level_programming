#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num = len(sys.argv) - 1
    if num == 0:
        print("0 arguments:")
    else:
        print("{} arguments:".format(num))
    for i in range(1, num + 1):
        print("{}: {}".format(i, sys.argv[i]))
