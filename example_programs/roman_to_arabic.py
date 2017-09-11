
__author__ = "Markus Rother"

values = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
    }

def roman_to_arabic(roman):
    arabic = 0
    previous = 0
    for char in roman:
        arabic += values[char]
        if values[char] > previous > 0:
            arabic -= 2 * previous
        else:
            previous = values[char]
    return arabic


print roman_to_arabic("MCMLXXIV")
