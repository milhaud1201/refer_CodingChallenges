"""
문제이름: 동전 0
주소: https://www.acmicpc.net/problem/11047
"""

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
print(coins)
coins.reverse()  # 내림차순
ans = 0

for coin in coins:
    ans += K // coin   # 4200 // 1000 = 4
    K %= coin  # K = 200
    print(f'coin: {coin}, K:{K}, ans:{ans}')

print(ans)