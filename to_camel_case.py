"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
"""
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
import re

def to_camel_case(string):
    if '-' not in string and '_' not in string:
        return string

    pattern = re.compile(r"-|_")
    words = pattern.split(string)
    camelCase = ''

    for word in words:
        if word in words[0] and word[0].islower():
            camelCase += word
            continue
        else:
            camelCase += word.capitalize()
    return camelCase
print(to_camel_case("the_stealth-warrior"))
