#!/usr/bin/python3
for al in range(97, 123):
    if al in [101, 113]:
        continue
    print("{}".format(chr(al)), end="")
