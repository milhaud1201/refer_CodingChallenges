def solution(arr):
    ans = []
    ans.append(arr[0])
    for _ in arr:
        if ans[-1] != _:
            ans.append(_)
    return ans
