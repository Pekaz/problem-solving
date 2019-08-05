import sys
import math

def distance_square(x1, y1, x2, y2):
	return (x2-x1)**2 + (y2-y1)**2

t = int(sys.stdin.readline())
for _ in range(0, t):
	x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
	dist = distance_square(x1, y1, x2, y2)
	if x1 == x2 and y1 == y2 and r1 == r2:
		print(-1)
	elif x1 == x2 and y1 == y2 and r1 != r2:
		print(0)
	elif dist == (r1+r2)**2:
		print(1)
	elif dist > (r1+r2)**2:
		print(0)
	else:
		if dist == (r1-r2)**2:
			print(1)
		elif dist > (r1-r2)**2:
			print(0)
		else:
			print(2)

