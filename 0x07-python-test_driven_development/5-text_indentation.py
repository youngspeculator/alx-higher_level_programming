#!/usr/bin/python3
"""This is a function which splits a text according to `.`,`?`, and `:`"""


def text_indentation(text):
    """Splits a string of text according to punctuation
    Args:
        text (str): the string of text to split
    Raises:
        TypeError: `text must be a string` if text is not a string
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    text = text.strip()
    while i < len(text):
        print(text[i], end='')
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print('\n')
            if i == len(text) - 1:
                break
            if text[i + 1] == ' ':
                i += 1
            while text[i] == ' ' and text[i + 1] == ' ' and i + 1 < len(text):
                i += 1
        i += 1
