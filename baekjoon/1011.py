import sys

def get_result(x, y):
	i = 1
	result = 0
	while True:
		n1 = i * (i - 1) / 2
		n2 = (i + 1) * i / 2
		n3 = (i + 2) * (i + 1) / 2
		if x + n1 + n2 <= y < x + n2 + n3:
			break
		i += 1
	result = 2 * i - 1
	left = y - (x + n1 + n2)
	while True:
		if left <= i:
			if left > 0:
				result += 1
			break
		left -= i
		result += 1
	return result


t = int(sys.stdin.readline())
for _ in range(0, t):
	x, y = map(int, sys.stdin.readline().split())
	result = get_result(x,y)
	print(result)

