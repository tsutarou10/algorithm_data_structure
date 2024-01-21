from __future__ import annotations

MAX = 3


class Node(object):
    def __init__(self, data: any = None):
        self.data = data
        self.prev = None
        self.next = None


head: Node = Node()
tail: Node = Node()


def init():
    tail.prev = head
    tail.next = head
    head.prev = tail
    head.next = tail


def push(v):
    if is_full():
        print("error: stack is full.")
        return
    pushed_node = Node(v)
    pushed_node.next = head.next
    head.next.prev = pushed_node
    head.next = pushed_node
    pushed_node.prev = head
    print_stack()


def pop():
    if is_empty():
        print("error: stack is empty.")
        return
    head.next.next.prev = head
    head.next = head.next.next
    print_stack()


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


def print_stack():
    if is_empty():
        print("stack is empty.")
    curr = head.next
    while curr != tail:
        print(curr.data, end=" -> ")
        curr = curr.next
    print()


def main():
    init()

    push(3)
    push(5)
    push(7)
    push(9)  # error

    pop()
    pop()
    pop()
    pop()


main()
