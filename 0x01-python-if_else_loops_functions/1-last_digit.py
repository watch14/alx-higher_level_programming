#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

x = abs(number) % 10

if x > 5:
    m = "and is greater than "
elif x == 0:
    m = "and is 0"
else:
    m = "and is less than 6 and not 0"

print(f"Last digit of {number} is {x} {m}")
