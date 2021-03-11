def validate_pushed_popped(pushed: list, popped: list) -> bool:
    return len(pushed) == len(popped)


def solution():
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))
    result = validate_pushed_popped(pushed, popped)
    print(result)

solution()
