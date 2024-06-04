#!/usr/bin/python3
def uppercase(str):
    for letters in range(len(str)):
        uni_code = ord(str[letters])
        if uni_code >= 97 and uni_code <= 122:
            uni_code = uni_code - 32
        print("{}".format(chr(uni_code)), end='')
    print()
