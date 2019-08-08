import sys
t = int(sys.stdin.readline())
for _ in range(0, t):
	a, b = map(int, sys.stdin.readline().split())
	b = list(map(int, bin(b)[2:]))
	b.reverse()
	result = 1
	for n in b:
		if n == 1:
			result = (result * a)%10
		a = (a*a)%10
	if result == 0:
		result = 10
	print(result)