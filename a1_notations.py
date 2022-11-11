"""
Given a number, write a program to translate the given number to a1 notation
Example: 1 -> A 26
"""
import math
import string


def find_a1_notation(input):
    alphabets = string.ascii_uppercase
    alphabet_map = {}
    for i in range(len(alphabets)):
        alphabet_map[i + 1] = alphabets[i]
    print(f"Input: {input}")
    print(f"Alphabet Map: {alphabet_map}")
    ans_string = ''
    init_char = math.floor(input / 26)
    last_char = input % 26
    if last_char > 0:
        ans_string += alphabet_map[last_char]
    while init_char >= 26:
        init_char = math.floor(init_char / 26)
        ll_char = init_char % 26
        if ll_char > 0:
            ans_string += alphabet_map[ll_char]
    ans_string += alphabet_map[init_char]
    print(f'A1 Notation: {ans_string[::-1]}')


find_a1_notation(27)
