"""
문제이름: [기초-종합] 수 나열하기3(py)
주소: https://codeup.kr/problem.php?id=6090
"""

# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)
# n번째 수를 출력하는 프로그램
# 수열
a, m, d, n = map(int, input().split())
res = a

for i in range(2, n+1): # 시작값이 정해져있어서 2부터 시작
    res = (res * m) + d
    # print(i, res)
    
print(res)
