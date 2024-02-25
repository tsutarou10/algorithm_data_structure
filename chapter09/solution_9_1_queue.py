from __future__ import annotations

MAX = 3


class Node(object):
    def __init__(self, data: any = None):
        self.data = data
        self.prev = None
        self.next = None


head = Node()
tail = Node()


def init():
    head.prev = tail
    head.next = tail
    tail.prev = head
    tail.next = head


def print_queue():
    if is_empty():
        print("queue is empty.")
    curr = head.next
    while curr != tail:
        print(curr.data, end=" -> ")
        curr = curr.next
    print()


def is_empty():
    return head.next == tail


def is_full():
    curr = head.next
    cnt = 1
    while curr != tail:
        if cnt == MAX:
            return True
        curr = curr.next
        cnt += 1
    return False


def enqueue(v):
    if is_full():
        print("error: queue is full.")
        return
    enqueued_node = Node(v)
    enqueued_node.next = tail
    tail.prev.next = enqueued_node
    enqueued_node.prev = tail.prev
    tail.prev = enqueued_node
    print_queue()


def dequeue():
    if is_empty():
        print("error: queue is empty.")
        return
    head.next.prev = head
    head.next = head.next.next
    print_queue()


def main():
    init()

    enqueue(3)
    enqueue(5)
    enqueue(7)
    enqueue(9)  # error

    dequeue()
    dequeue()
    dequeue()
    dequeue()


main()
