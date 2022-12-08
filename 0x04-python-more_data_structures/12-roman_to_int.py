#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    number = 0
    if (type(roman_string) is not str or roman_string is None):
        return (0)
    for i, char in enumerate(roman_string):
        tmp_num = roman[char]
        try:
            if tmp_num < roman[roman_string[i + 1]]:
                tmp_num = tmp_num * -1
        except IndexError:
            pass
        number = number + tmp_num
    return (number)
