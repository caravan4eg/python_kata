# assert
from collections.abc import Iterable


def chk_value(iterable, k: int) -> str:
    assert isinstance(
        iterable, Iterable), "expected iterable as first argument"
    assert k > 0, "expected k > 0"
    print(''.join(sorted(iterable)))
    return sorted(iterable)[k-1]


def main():
    iterable = '54321'
    print(chk_value(iterable, 4))

    iterable = 54321
    print(chk_value(iterable, 4))

    assert chk_value(range(10), 3) == 2,


if __name__ == "__main__":
    main()
