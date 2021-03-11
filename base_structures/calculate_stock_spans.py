def calculate_stock_spans(prices: list) -> list:
    return [1 for _ in prices]


def solution():
    prices = list(map(int, input().split()))
    spans = calculate_stock_spans(prices)
    print(' '.join(map(str, spans)))


solution()
