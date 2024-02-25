from sys import stdin
from typing import List

memo: List[int] = []


def tribo(n: int) -> int:
    if n <= 1:
        return 0
    if n == 2:
        return 1

    if memo[n] != -1:
        return memo[n]

    memo[n] = tribo(n - 1) + tribo(n - 2) + tribo(n - 3)
    return memo[n]


def main():
    N = int(stdin.readline())
    global memo
    memo = [-1] * (N + 1)

    rsl = tribo(N)
    print(f"T[{N}] = {rsl}")


main()
