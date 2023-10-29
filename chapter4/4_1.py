from sys import stdin


def func(n):
    if n == 0:
        return 0
    return n + func(n - 1)


rsl = func(10)
print(rsl)
