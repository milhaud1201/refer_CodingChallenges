def gcb(a, b):
    if a % b == 0:
        return b
    else:
        return gcb(b, a%b)

a, b = map(int, input().split())
a, b = max(a, b), min(a, b) # 큰 수가 a가 되어야 함
print(gcb(a, b))
print(a * b // gcb(a, b))