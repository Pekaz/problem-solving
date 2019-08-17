import sys

n,x,y = list(map(int,sys.stdin.readline().split()))

result = 1
while True:
	x = round(x/2+0.01)
	y = round(y/2+0.01)
	if x == y:
		break
	result += 1
print(result)
