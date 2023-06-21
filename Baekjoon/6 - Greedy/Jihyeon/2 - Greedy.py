"""
문제이름: 세탁소 사장 동혁
주소: https://www.acmicpc.net/problem/2720
"""

for i in range(int(input())):
    C = int(input())
    coins = [25, 10, 5, 1]
    ans = 0
    for coin in coins:
        ans = C // coin  # 124 // 25 = 4
        C %= coin  # 124 % 25 = 24
        # print(f"coin: {coin}, C: {C}, ans: {ans}")
        print(ans, end=' ')