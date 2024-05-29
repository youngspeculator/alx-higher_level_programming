#!/usr/bin/python3
for letter in range(ord('a'), ord('z') +1):
	if (letter != 101 and letter != 113):
		print("{}".format(chr(letter)), end="")
