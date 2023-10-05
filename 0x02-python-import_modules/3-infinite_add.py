#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lum = len(sys.argv)
    x = 0
    for i in range(1, lum):
        x = x + int(sys.argv[i])
    print(x)
