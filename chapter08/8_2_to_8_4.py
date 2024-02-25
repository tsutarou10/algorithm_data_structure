from __future__ import annotations


class Node(object):
    def __init__(self, name: str = "") -> None:
        self.name = name
        self.next = None


nil: Node = Node()


def init():
    nil.next = nil


def print_list():
    cur: Node = nil.next
    while cur != nil:
        print(cur.name, end=" -> ")
        cur = cur.next
    print()


def insert(v: Node, p: Node = nil):
    v.next = p.next
    p.next = v


def main():
    init()

    names = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]

    for i, name in enumerate(names):
        node: Node = Node(name)

        insert(node)

        print(f"step {i}: ".format(i), end="")
        print_list()


main()
