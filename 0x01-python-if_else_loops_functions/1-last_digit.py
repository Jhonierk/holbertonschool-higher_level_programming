#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Number = abs(number) % 10
if number < 0:
    Number = -Number
print("Last digit of {} is {} and is ".format(number, Number), end="")
if Number > 5:
    print("greater than 5")
elif Number == 0:
    print("0")
else:
    print("less than 6 and not 0")
