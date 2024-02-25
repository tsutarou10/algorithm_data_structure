def main():
    X = int(input())
    a = list(map(int, input().split()))
    currencies = [500, 100, 50, 10, 5, 1]

    rsl = 0
    for idx, currency in enumerate(currencies):
        cnt = X // currency
        if cnt > a[idx]:
            cnt = a[idx]
        rsl += cnt
        X -= currency * cnt
    print(rsl)


main()
