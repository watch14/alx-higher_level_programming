#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1
    if l == 0:
        print("0 arguments.")
    if l == 1:
        print("1 arguments.")
    else:
        print("{} arguments:".format(l))
    for i in range(l):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
