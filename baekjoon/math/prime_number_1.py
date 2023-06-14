def is_prime(N):
  global prime_number
  if N == 1:
    pass
  elif N == 2:
    prime_number.append(N)
  else:
    if all(N%pnum for pnum in prime_number) != 0:
      prime_number.append(N)

prime_number = []

N = int(input())
data = list(map(int, input().split()))
for _ in range(1, 1000):
  is_prime(_)
ans = 0
print(sum(1 for _ in data if _ in prime_number))