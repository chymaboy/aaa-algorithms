def max_even_sum(numbers):
    if sum(numbers) % 2 == 0:
        return sum(numbers)
    odds = list(filter(lambda x: x % 2 == 1, numbers))
    if len(odds) > 0:
        min_odd = min(odds)
        return sum(numbers)-min_odd
    else:
        return 0


def solution():
    numbers = [int(x) for x in input().split()]
    print(max_even_sum(numbers))


solution()
