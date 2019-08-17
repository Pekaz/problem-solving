import sys

n,m = list(map(int, sys.stdin.readline().split()))
num = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(0, len(num)):
	left = num[i] - 1
	right = n + 1 - num[i]
	if left < right:
		result += left
		for j in range(0, len(num)):
			num[j] -= left
			if num[j] < 1:
				num[j] += n
	else:
		result += right
		for j in range(0, len(num)):
			num[j] += right
			if num[j] > n:
				num[j] -= n
	n -= 1
	for j in range(0, len(num)):
		num[j] -= 1
print(result)
