def check(src):
    stack = []
    rsl = []
    for idx, s in enumerate(src):
        if s == '(':
            stack.append(idx)
            continue
        if len(stack) == 0:
            print('error')
            return
        rsl.append((stack.pop(), idx))

    if len(stack) != 0:
        print('too many (')
        return

    rsl.sort(key=lambda x: x[0])
    print(rsl)


def main():
    check("((()())())")  # (0, 9) (1, 6), (2, 3), (4, 5), (7, 8)
    check("())")  # error
    check("(()")  # too many (


main()
