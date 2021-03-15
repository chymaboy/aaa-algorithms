def validate_pushed_popped(pushed: list, popped: list) -> bool:
    stack_in = []
    stack_out = []
    for i in range(len(pushed)):
        stack_in.append(pushed[i])
        while len(stack_in) > 0 and stack_in[len(stack_in) - 1] == popped[len(stack_out)]:
            el = stack_in.pop()
            stack_out.append(el)
    return stack_out == popped


def solution():
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))
    result = validate_pushed_popped(pushed, popped)
    print(result)


solution()
