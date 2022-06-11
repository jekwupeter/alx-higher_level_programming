#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    roman_to_int - convert roman numeral to integer
    @roman_string: input roman numeral
    Return: integer equivalent of roman numeral
    """
    result = 0
    single_letter = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    special_case = {"IX": 9, "IV": 4}
    if not isinstance(roman_string, str) or roman_string == None:
        return 0

    if roman_string[-2:] in list(special_case):
        for char in roman_string[:-2]:
            for letter, num in single_letter.items():
                if letter == char:
                    result += num
        for i in range(2):
            if list(special_case)[i] == roman_string[-2:]:
                result += special_case[list(special_case)[i]]
    else:
        for i in roman_string:
            for letter, num in single_letter.items():
                if letter == i:
                    result += num
    return result
