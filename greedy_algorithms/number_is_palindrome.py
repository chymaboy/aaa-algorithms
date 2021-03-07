from math import log10


def is_palindrome(x):
    while x > 0:
        if x % 10 != x // 10**(int(log10(x))):
            return False
        x = x % 10**(int(log10(x))) // 10
    return True


def solution():
    a = int(input())
    c = is_palindrome(a)
    print(c)


solution()
