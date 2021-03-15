def calculate_stock_spans(prices: list) -> list:
    answer = [0] * len(prices)
    prices_stack = [prices[0]]
    days_stack = [1]
    for _, price in enumerate(prices):
        tmp_days = 1
        while len(prices_stack) > 0 and price >= prices_stack[-1]:
            prices_stack.pop()
            tmp_days = tmp_days + days_stack.pop()
        prices_stack.append(price)
        days_stack.append(tmp_days)
        answer.append(tmp_days)
    return answer


def solution():
    prices = list(map(int, input().split()))
    spans = calculate_stock_spans(prices)
    print(' '.join(map(str, spans)))


solution()
