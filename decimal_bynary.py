
"""
Найти макс число повторяющихся 1 в бинарном представлении числа
"""
n = int(input())

b_groups = str(bin(n).split('b')[1]).split('0')
print(b_groups)
print(max([len(group) for group in b_groups]))
