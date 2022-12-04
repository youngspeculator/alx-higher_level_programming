#!/usr/bin/python3
import random
number = random.randint(-100,100)
if (number > 0):
    print(f"{number:d} is positive\n".format(number))
elif (number < 0):
    print(f"{number:d} is negative\n".format(number))
else:
    print(f"{number:d} is zero\n".format(number))
