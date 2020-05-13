# Написать декоратор к функции func для кеширования результатов
import pickle
import time


def memorized(func):
    memory = {}

    def memo(*args, **kwargs):
        hash = pickle.dumps(args, len(kwargs))

        if hash not in memory:
            memory[hash] = func(*args, **kwargs)
            print('Кеширую: ', memory[hash])
        return memory[hash]
    return memo

@memorized
def func(x):
    print('Wait I\'m calculating...')
    return x*x+1

for i in range(10):
    start = time.time()
    print('Результат = ', func(i))
    end = time.time()
    print(f'Время вычисления c с аргументом {i} = {end-start}')
