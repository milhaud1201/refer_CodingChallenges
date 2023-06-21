"""
문제이름: [기초-종합] 그림 파일 저장용량 계산하기(py)
주소: https://codeup.kr/problem.php?id=6085
"""

w, h, b = map(int, input().split())

res = w * h * b / 8 / 1024 / 1024

print(f"{round(res, 2):.2f} MB")