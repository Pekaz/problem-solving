import sys

x,y = list(map(int,sys.stdin.readline().split()))
z = int(y * 100 / x)
if z >= 99:
	print(-1)
else:
	a = 0
	b = 1000000000
	re = -1
	while a <= b:
		mid = int((a + b) / 2)
		check = int((y + mid) * 100 / (x + mid))
		if z >= check:
			re = mid + 1
			a = mid + 1
		else:
			b = mid - 1
	print(re)