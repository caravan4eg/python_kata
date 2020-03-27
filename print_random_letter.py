import random

phrase = 'Caravan4eg - Full-stack developer'
i = 0
print('-' * 50)
while i < 50:
    index = random.randrange(0, len(phrase))
    print(phrase[index], end='')
    i += 1
print()
print('-' * 50)
