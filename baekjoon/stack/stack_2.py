def solution(s):
    stack = []
    for _ in s:
        if _ == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) != 0:
        return False
    return True
                