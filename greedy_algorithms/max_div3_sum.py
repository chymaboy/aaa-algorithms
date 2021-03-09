def max_div3_sum(numbers):
    zero, plus_one, minus_one = [], [], []
    for num in numbers:
        if num % 3 == 0:
            zero.append(num)
        elif num % 3 == 1:
            plus_one.append(num)
        elif num % 3 == 2:
            minus_one.append(num)
    plus_one.sort()
    minus_one.sort()
    if sum(numbers) % 3 == 0:
        return sum(numbers)
    elif sum(numbers) % 3 == 1:
        if len(plus_one) > 0:
            if len(minus_one) > 1:
                if plus_one[0] <= minus_one[0] + minus_one[1]:
                    return sum(numbers) - plus_one[0]
                else:
                    return sum(numbers) - minus_one[0] - minus_one[1]
            else:
                return sum(numbers) - plus_one[0]
        elif len(minus_one) > 1:
            return sum(numbers) - minus_one[0] - minus_one[1]
        else:
            return 0
    elif sum(numbers) % 3 == 2:
        if len(minus_one) > 0:
            if len(plus_one) > 1:
                if minus_one[0] <= plus_one[0] + plus_one[1]:
                    return sum(numbers) - minus_one[0]
                else:
                    return sum(numbers) - plus_one[0] - plus_one[1]
            else:
                return sum(numbers) - minus_one[0]
        elif len(plus_one) > 1:
            return sum(numbers) - plus_one[0] - plus_one[1]
        else:
            return 0


def solution():
    numbers = [int(x) for x in input().split()]
    print(max_div3_sum(numbers))


solution()
