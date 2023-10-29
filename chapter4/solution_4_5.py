from sys import stdin

cnt = 0


def solve(N, curr, is_used):
    global cnt
    if curr > N:
        return
    if is_used == 0b111:
        cnt += 1

    solve(N, curr * 10 + 7, is_used | 0b001)
    solve(N, curr * 10 + 5, is_used | 0b010)
    solve(N, curr * 10 + 3, is_used | 0b100)


def main():
    N = int(stdin.readline().strip())

    global cnt
    solve(N, 0, 0)
    print(cnt)


main()
