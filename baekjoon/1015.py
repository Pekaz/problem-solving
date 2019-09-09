import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
check = [0] * n
srt = []
for i in range(0, n):
	srt.append(num[i])
srt.sort()
result = []
for i in range(0, n):
	for j in range(0, n):
		if num[i] == srt[j] and check[j] == 0:
			result.append(j)
			check[j] = 1
			break
for i in range(0, n):
	print(result[i], end=' ')