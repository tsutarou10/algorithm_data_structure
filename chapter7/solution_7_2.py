def check(red, blue):
    red.sort(key=lambda x: x[1], reverse=True)
    blue.sort(key=lambda x: x[0])
    rsl = 0

    used_red = []
    for b in blue:
        tmp_used_red = []
        for r in red:
            if r in used_red:
                continue
            if r[0] >= b[0] or r[1] >= b[1]:
                continue
            tmp_used_red.append(r)
        tmp_used_red.sort(key=lambda x: x[1], reverse=True)
        if len(tmp_used_red) > 0:
            rsl += 1
            used_red.append(tmp_used_red[0])
    return rsl


def main():
    N = int(input())

    red = []
    blue = []
    for _ in range(N):
        a, b = map(int, input().split())
        red.append((a, b))
    for _ in range(N):
        c, d = map(int, input().split())
        blue.append((c, d))

    rsl = check(red, blue)

    print(rsl)


main()
