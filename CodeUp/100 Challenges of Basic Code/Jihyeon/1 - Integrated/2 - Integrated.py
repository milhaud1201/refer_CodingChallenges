"""
문제이름: [기초-종합] 언제까지 더해야 할까?(py)
주소: https://codeup.kr/problem.php?id=6079
"""

while True:
    n = int(input())
    total = 0
    for i in range(1, n+1):
        # print(i)
        total += i
        if total >= n:
            print(i)
            break