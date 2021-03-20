def fib(n, f0=1, f1=1):
    if n == 1:
        return f1
    f0, f1 = f1, f0 + f1
    return fib(n - 1, f0, f1)


def solution():
    n = int(input().strip())
    c = fib(n)
    print(c)


solution()
