#!/usr/bin/python3
for digit1 in range(0, 10):
    for digit2 in range(0, 10):
        if (digit1 < digit2):
            print(f"{int(digit1)}{int(digit2)}", end="")
            if (digit2 < 8):
                print(", ", end=" ")
            elif(digit2 > 8):
                print(", ", end=" ")
            else:
                print(", ", end=" ")
print(f"\n", end="")
