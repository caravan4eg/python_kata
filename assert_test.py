# assert
from collections.abc import Iterable


def chk_value(iterable, k: int) -> str:
    assert isinstance(
        iterable, Iterable), "expected iterable as first argument"
    assert k > 0, "expected k > 0"
    print(''.join(sorted(iterable)))
    return sorted(iterable)[k-1]


s1 = '54321'
print(chk_value(s1, 4))
