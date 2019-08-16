import sys

t = int(sys.stdin.readline())
for _ in range(0, t):
	x1,y1,x2,y2 = list(map(int, sys.stdin.readline().split()))
	n = int(sys.stdin.readline())
	result = 0
	for _ in range(0, n):
		x,y,r = list(map(int, sys.stdin.readline().split()))
		check1 = ((x-x1)**2 + (y-y1)**2 <= r**2)
		check2 = ((x-x2)**2 + (y-y2)**2 <= r**2)
		if check1 != check2:
			result += 1
	print(result)