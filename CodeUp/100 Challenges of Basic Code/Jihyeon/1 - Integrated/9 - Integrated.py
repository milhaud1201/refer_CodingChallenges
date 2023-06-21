"""
문제이름: [기초-종합] 거기까지! 이제 그만~(설명)(py)
주소: https://codeup.kr/problem.php?id=6086
"""

n = int(input())
s = 0
c = 0

while True:
    s = s+c  # 1, 3, 6, 10 ...
    c = c+1  # 1, 2, 3, 4 ...
    if s >= n:
        break
    
print(s)