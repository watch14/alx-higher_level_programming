#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    if len(sys.argv) == 0:
        print(".")
    print("{} arguments:".format(len(sys.argv)))
    for i in range (1, (len(sys.argv))):
        print("{}: {}".format(i, sys.argv[i]))
