#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    roman_to_int - convert roman numeral to integer
    @roman_string: input roman numeral
    Return: integer equivalent of roman numeral
    """
    result = 0
    single_letter = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not isinstance(roman_string, str) or roman_string == None:
        return 0

    for i in range(len(roman_string)):
        if i != (len(roman_string) - 1) and single_letter[roman_string[i]] < \
            single_letter[roman_string[i + 1]]:
            result += single_letter[roman_string[i]] * -1
        else:
            result += single_letter[roman_string[i]]
    return result
