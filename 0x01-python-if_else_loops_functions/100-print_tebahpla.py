for char_code in range(90, 64, -1):
    char = chr(char_code)
    print("{:s}".format(char.lower() if char_code % 2 == 0 else char.upper()), end="")
