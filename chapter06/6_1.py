N = 8
a = [3, 5, 8, 10, 14, 17, 21, 39]


def binary_search(key):
    left = 0
    right = len(a) - 1
    while right >= left:
        mid = int(left + (right - left) / 2)
        if a[mid] == key:
            return mid
        if a[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def main():
    print(binary_search(10))
    print(binary_search(3))
    print(binary_search(39))

    print(binary_search(-100))
    print(binary_search(9))
    print(binary_search(100))


main()
