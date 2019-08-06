import sys

num = []
for _ in range(0, 31):
	num.append([0]*31)

for i in range(1, 31):
	for j in range(i, 31):
		if i == 1:
			num[i][j] = j
			continue
		if i == j:
			num[i][j] = 1
			continue
		num[i][j] = 1
		for z in range(0, j-i):
			num[i][j] += num[i-1][j-z-1]

t = int(sys.stdin.readline())
for _ in range(0, t):
	n, m = map(int, sys.stdin.readline().split())
	print(num[n][m])
