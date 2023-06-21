"""
문제이름: [기초-종합] 빛 섞어 색 만들기(설명)(py)
주소: https://codeup.kr/problem.php?id=6083
"""

r, g, b = input().split()

r = int(r)
g = int(g)
b = int(b)
rgb = 0

for i in range(r):
    for j in range(g):
        for z in range(b):
            rgb += 1
            print(i, j, z)
print(rgb)