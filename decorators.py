# decorators
def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Время выполнения функции {func}: {end-start} секунд')
    return wrapper

@benchmark
def fetch_webpage():
    import requests
    r = requests.get('http://google.com')
    print(r)


fetch_webpage()
