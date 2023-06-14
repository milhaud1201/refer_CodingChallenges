from math import ceil
def solution(progresses, speeds):
    arr = [ceil((100 - progresses[i])/speeds[i]) for i in range(len(progresses))]
    pop, flag = arr[0], 0
    stack = []
    for i in range(len(arr)):
        if arr[i] > pop:
            stack.append(flag)
            pop, flag = arr[i], 1
        else :
            flag += 1
        if i == len(arr)-1:
            stack.append(flag)
    return stack