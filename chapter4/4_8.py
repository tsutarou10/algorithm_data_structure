memo = []


def fibo(n):
    if n <= 1:
        return n

    if memo[n] != None:
        return memo[n]

    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]


def main():
    N = 50
    global memo
    memo = [None] * N

    fibo(N - 1)

    for i, m in enumerate(memo):
        print(f"{i} items: {m}")


main()
