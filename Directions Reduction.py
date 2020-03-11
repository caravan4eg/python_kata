from unittest import TestCase
"""
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
test.assert_equals(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])

['SOUTH', 'WEST', 'NORTH', '', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'EAST'] should equal ['SOUTH', 'WEST', 'NORTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'EAST']
['SOUTH', 'WEST', 'NORTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'EAST']

['SOUTH', 'WEST', 'NORTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'EAST']
['NORTH', 'NORTH', '', 'WEST', 'NORTH', 'WEST'] should equal

"""


def dirReduc(arr):
    if len(arr) == 1 and arr[0] == '':
        return []

    not_clean = True
    dir_pairs = ['north-south', 'south-north', 'east-west', 'west-east']
    d = '-'.join([i.lower() for i in arr]).strip('-').replace('--', '-')
    while not_clean:
        not_clean = False
        for pair in dir_pairs:
            if pair in d:
                d = d.replace(pair, '').strip('-').replace('--', '-')
                not_clean = True

    return list(d.upper().split('-'))

a = ['SOUTH', 'WEST', 'NORTH', '', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'EAST']
print(dirReduc(a))

a = ['SOUTH', 'WEST', 'NORTH', '', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'EAST']
print(dirReduc(a))

a=['']
print(dirReduc(a))
