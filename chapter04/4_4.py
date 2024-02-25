def _gcd(m, n):
    if n == 0:
        return m

    return _gcd(n, m % n)


print(_gcd(51, 15))
print(_gcd(15, 51))
