"""
문제이름: [기초-종합] 수 나열하기1(py)
주소: https://codeup.kr/problem.php?id=6088
"""

# 시작값 a, 등차 d, 몇 번째인지를 나타내는 정수 n
a, d, n = map(int, input().split())
s = a

for i in range(2, n+1):  # 시작값이 정해져있어서 2부터 시작
    s += d
    print(s)

print(s)

'''
문제 설명:
어떤 규칙에 따라 수를 순서대로 나열한 것을 수열(sequences)이라고 한다.

예를 들어
1 4 7 10 13 16 19 22 25 ... 은
1부터 시작해 이전에 만든 수에 3을 더해 다음 수를 만든 수열이다.
이러한 것을 수학에서는 앞뒤 수들의 차이가 같다고 하여

등차(차이가 같다의 한문 말) 수열이라고 한다. (등차수열 : arithmetic progression/sequence)

처음 문제 풀이:
처음에 작성한 while문 보다 for문으로 처리한 코드가 더 빨랐다.

a, d, n = map(int, input().split())
s = 1
while True:
    a += d
    s += 1
    # print(s)
    # print(a)
    if s == n:
        break
print(a)
'''