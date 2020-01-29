import sys

t = int(sys.stdin.readline())
for _ in range(t):
	n = int(sys.stdin.readline())
	re = int(n/2) * "1"
	if n%2 == 1:
		re = "7" + re[1:]
	print(re)

