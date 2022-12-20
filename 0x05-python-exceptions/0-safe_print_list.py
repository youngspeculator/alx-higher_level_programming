#!/usr/bin/python3
""" 
my_list can contain any type (integer, string, etc.)
all elements must be printed on the same line
followed by a new line.
@x: the number of elements to print
    x can be > len(my_list)
Return: real number of elements printed
"""
def safe_print_list(my_list=[], x=0):
    total = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            total += 1
        except IndexError:
            break
    print()
    return(total)


