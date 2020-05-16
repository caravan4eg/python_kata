# Technical interview
# Q22
# is_palindrom
"""
Напишите функцию 'Является ли строка палиндромом'?
"""


def is_palindrom_slicing(string):
    return string.lower() == string[::-1].lower()


def is_palindrom_list(string):
    # to list
    temp_list = list(string)
    # reverse list
    temp_list.reverse()
    # to string

    return string.lower() == ''.join(temp_list).lower()


def main():
    s = 'roza'
    print(is_palindrom_slicing(s))
    print(is_palindrom_list(s))


if __name__ == "__main__":
    main()
