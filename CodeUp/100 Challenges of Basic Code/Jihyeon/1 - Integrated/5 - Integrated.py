"""
문제이름: [기초-종합] 3 6 9 게임의 왕이 되자(설명)(py) 해결
주소: https://codeup.kr/problem.php?id=6082
"""

n = int(input())

for i in range(1, n+1):
    s = str(i)
    count = 0
    for j in s:
        j = int(j)
        # print(j)
        if j in [3, 6, 9]:
            count += 1
    if count == 0:
        print(i, end=' ')
    else: 
        print(count*"X", end=' ')

'''
코드업 답안지
위의 내가 푼 풀이처럼 이 코드는 33과 같은 3,6,9가 두 번 들어간 수 일때, 
"짝짝"과 같이 박수를 두 번 치는 코드는 아니다.

n = int(input())

for i in range(1, n+1) :
  if i%10==3 or i%10==6 or i%10==9 :
    print("X", end=' ')
  else :
    print(i, end=' ')
'''