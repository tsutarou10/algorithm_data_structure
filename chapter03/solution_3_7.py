from sys import stdin


def main():
    S = stdin.readline().strip()
    N = len(S)

    total_sum = 0

    for bit in range(1 << N - 1):
        expression = []
        prev = 0

        for i in range(N - 1):
            if bit & (1 << i):
                expression.append(S[prev : i + 1])
                prev = i + 1
        expression.append(S[prev:])

        sum = 0
        for term in expression:
            sum += int(term)

        total_sum += sum
    print(total_sum)


main()
