import bisect

a = [i * 10 for i in range(1, 11)]

# 値をリストに挿入する位置のインデックスを返す
print(bisect.bisect(a, 55))

b = [1, 2, 2, 2, 3]
print(bisect.bisect_left(b, 2))
print(bisect.bisect_right(b, 2))
print(bisect.bisect(b, 2))
