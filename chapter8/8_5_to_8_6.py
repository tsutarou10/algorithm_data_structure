from __future__ import annotations


class Node(object):
    def __init__(self, name: str = ""):
        self.name = name
        self.prev = None
        self.next = None


nil: Node = Node()


def init():
    nil.prev = nil
    nil.next = nil


def print_list():
    cur: Node = nil.next
    while cur != nil:
        print(cur.name, end=" -> ")
        cur = cur.next
    print()


def insert(v: Node, p: Node = nil):
    v.next = p.next
    p.next.prev = v
    p.next = v
    v.prev = p


def erase(v: Node):
    if v == nil:
        return
    v.prev.next = v.next
    v.next.prev = v.prev
    del v


def main():
    init()

    names = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]

    watanabe: Node
    for name in names:
        node: Node = Node(name)
        insert(node)
        if name == "watanabe":
            watanabe = node

    print("before: ", end="")
    print_list()
    erase(watanabe)
    print("after: ", end="")
    print_list()


main()
