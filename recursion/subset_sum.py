def pow(x, y):
    res = 1
    for i in range(y):
        res *= x
    return res


def filter_array(array, n) -> list:
    binary = bin(n)[2:].rjust(len(array))
    return [array[i] for i, v in enumerate(binary) if v == '1']


def has_subset_with_sum_k(array: list, k: int) -> bool:
    for n in range(int(pow(2, len(array)))):
        if sum(filter_array(array, n)) == k:
            return True
    return False


def solution():
    array = list(map(int, input().split()))
    s = int(input().strip())
    c = has_subset_with_sum_k(array, s)
    print(c)


solution()
