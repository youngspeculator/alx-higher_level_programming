#!/usr/bin/python3
for number in range(0, 100):
    if number != 99:
        print("{}, ".format(int(number)), end="")
    else:
        print("{}".format(int(number)))
