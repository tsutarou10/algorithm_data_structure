def main():
    N = int(input())
    inters = []
    for _ in range(N):
        start, end = map(int, input().split())
        inters.append((start, end))

    inters.sort(key=lambda x: x[1])

    rsl = 0
    current_end = 0
    for inter in inters:
        if inter[0] < current_end:
            continue
        rsl += 1
        current_end = inter[1]
    print(rsl)


main()
