"""
문제이름: [기초-종합] 수 나열하기2(py)
주소: https://codeup.kr/problem.php?id=6089
"""

# 시작값 a, 비율 d, 몇 번째인지를 나타내는 정수 n
# 등비수열
a, d, n = map(int, input().split())
s = a

for i in range(2, n+1):  # 시작값이 정해져있어서 2부터 시작
    s = s*d
    # print(s)

print(s)