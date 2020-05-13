# decorators
def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'[*] Время выполнения функции {func}: {end-start} секунд')
        return return_value

    return wrapper


@benchmark
def fetch_webpage(url):
    import requests
    r = requests.get(url)
    return r.text


web_page = fetch_webpage('http://google.com')
print(web_page)
