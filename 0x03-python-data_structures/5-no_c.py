#!/user/bin/python3
def no_c(my_string):
    st = ""
    for char in my_string:
        if char not in ('c', 'C'):
            st = st + char
    return st
