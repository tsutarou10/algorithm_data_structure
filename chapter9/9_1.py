MAX = 100000

st = [None for _ in range(MAX)]
top = 0


def init():
    global top
    top = 0


def is_empty():
    global top
    return top == 0


def is_full():
    global top
    return top == MAX


def push(x):
    global top
    if is_full():
        print("error: stack is full.")
        return
    st[top] = x
    top += 1


def pop():
    global top
    if is_empty():
        print("error: stack is empty.")
        return -1
    top -= 1
    return st[top]


def main():
    init()

    push(3)
    push(5)
    push(7)

    print(pop())
    print(pop())

    push(9)


main()
