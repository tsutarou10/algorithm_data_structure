def fibo(n):
    print(f"call fibo({n})")

    if n <= 1:
        return n

    rsl = fibo(n - 1) + fibo(n - 2)
    print(f"{n} items = {rsl}")

    return rsl


print(fibo(6))
