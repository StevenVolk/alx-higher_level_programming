#!/usr/bin/python3

def roman_to_int(roman_string):
    rom_con = {"I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000}
    num = []
    result = 0
    if roman_string == None or not(isinstance(roman_string, str)):
        return 0
    for r in range(0, len(roman_string)):
        if roman_string[r] not in rom_con:
            return 0
        else:
            num.append(rom_con[roman_string[r]])
        if len(num) > 1 and num[r-1] < num[r]:
            result = result - (2 * num[r-1]) + num[r]
        else:
            result += num[r]
    return result
