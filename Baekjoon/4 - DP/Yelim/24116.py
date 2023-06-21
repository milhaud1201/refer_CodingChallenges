fib = [-1] * 41
f = [-1] * 41
count = 0

fib[0] = fib[1] = 1
for n in range(2, 41):
  fib[n] = fib[n-1] + fib[n-2]

def fibonacci(n):
  global count, f
  f[1] = f[2] = 1
  for i in range(3, n+1):
    count += 1
    f[i] = f[i-1] + f[i-2]
  return f[n]

N = int(input())
fibonacci(N)
print(fib[N-1], count)