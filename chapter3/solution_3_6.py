from sys import stdin


def main():
    K, S = map(int, stdin.readline().split())

    rsl = 0
    for x in range(K + 1):
        for y in range(K + 1):
            if S - K <= x + y <= S:
                rsl += 1
    print(rsl)


main()
