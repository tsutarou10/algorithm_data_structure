from sys import stdin


def func(n):
    print(f"call func({n})")

    if n == 0:
        return 0

    rsl = n + func(n - 1)
    print(f"sum from 0 to {n} is {rsl}")
    return rsl


func(5)
