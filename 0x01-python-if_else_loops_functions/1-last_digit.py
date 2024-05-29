#!/usr/bin/python3
import random
num = random.randomint(-10000, 10000)
pos = "positive"
zer = "zero"
neg = "negative"
print("{} is ".format(num), end="")
if (num > 0):
	print("{}".foramt(pos))
if (num == 0):
	print("{}".format(zer))
if (num < 0):
	print("{}".format(neg))
