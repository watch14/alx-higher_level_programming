#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    x = 0
    for i in range(1,l):
        x = x + int(sys.argv[i])
    print(x)
