#!/usr/bin/python3
for i in range(0, 10):
    for u in range(1, 10):
        if i >= u:
            continue
        elif i == 8 and u == 9:
            print("{}{}".format(i, u))
        else:
            print("{}{}, ".format(i, u), end="")
