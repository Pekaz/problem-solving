import sys

n,m = list(map(int, sys.stdin.readline().split()))
num = []
for _ in range(0, n):
	line = sys.stdin.readline()
	num.append(line)

max_width = min(n, m)
finished = False
for width in range(max_width-1, -1, -1):
	for i in range(0, n-width):
		for j in range(0, m-width):
			if num[i][j] == num[i+width][j] == num[i][j+width] == num[i+width][j+width]:
				finished = True
				print((width+1)**2)
			if finished:
				break
		if finished:
			break
	if finished:
		break
