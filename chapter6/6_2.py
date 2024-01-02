# x が条件を満たすかどうか
def P(x):
    pass


N = 10


def binary_search():
    # P(left) = false, P(right) = true となるように初期化
    left = 0
    right = N

    while right - left > 1:
        mid = int(left + (right - left) / 2)
        if P(mid):
            right = mid
        else:
            left = mid
    return right
