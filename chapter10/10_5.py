# Python では heapq が標準ライブラリ用意されている
class Heap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        self.heap.append(x)
        idx = len(self.heap) - 1  # index of inserted vertex
        while idx > 0:
            p = int((idx - 1) / 2)  # index of parent
            if (
                self.heap[p] >= x
            ):  # the key of parent is larger than that of inserted vertex
                break
            self.heap[idx] = self.heap[p]
            idx = p
        self.heap[idx] = x

    def top(self):
        if len(self.heap) != 0:
            return self.heap[0]
        return -1

    def pop(self):
        if len(self.heap) == 0:
            return
        x = self.heap[-1]  # the vertex inserted into root
        del self.heap[-1]
        idx = 0
        while idx * 2 + 1 < len(self.heap):
            left_child = idx * 2 + 1
            right_child = idx * 2 + 2
            large_child = left_child
            if (
                right_child < len(self.heap)
                and self.heap[right_child] > self.heap[left_child]
            ):
                large_child = right_child
            if self.heap[large_child] <= x:
                return
            self.heap[idx] = self.heap[large_child]
            idx = large_child
        self.heap[idx] = x


def main():
    h = Heap()
    h.push(5)
    h.push(3)
    h.push(7)
    h.push(1)

    print(h.top())  # 7
    h.pop()
    print(h.top())  # 5

    h.push(11)
    print(h.top())  # 11


main()
