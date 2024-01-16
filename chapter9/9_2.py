MAX = 100000

que = [None for _ in range(MAX)]
tail = 0
head = 0


def init():
    global head, tail
    head = tail = 0


def is_empty():
    global head, tail
    return head == tail


def is_full():
    global head, tail
    return head == (tail + 1) % MAX


def enqueue(x):
    global tail
    if is_full():
        print("error: queue is full.")
        return
    que[tail] = x
    tail += 1
    if tail == MAX:
        tail = 0


def dequeue():
    global head
    if is_empty():
        print("error: queue is empty.")
        return -1
    res = que[head]
    head += 1
    if head == MAX:
        head = 0
    return res


def main():
    init()

    enqueue(3)
    enqueue(5)
    enqueue(7)

    print(dequeue())
    print(dequeue())

    enqueue(9)


main()
