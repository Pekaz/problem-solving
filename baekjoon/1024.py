import sys

n,m = list(map(int, sys.stdin.readline().split()))
finished = False
for i in range(m, 101):
	if (2 * n) % i == 0:
		a = int(2 * n / i) - i + 1
		if a % 2 == 0 and a >= 0:
			a = int(a / 2)
			for r in range(a, a + i):
				print(r, end=' ')
			finished = True
			break
if not finished:
	print(-1)
