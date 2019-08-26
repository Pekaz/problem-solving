import sys
import math

che = [0] * 1000001
prime = []
for i in range(2, 1000001):
	if che[i] == 1:
		continue
	if i**2 > 1000001000000:
		break
	prime.append(i)
	j = 2
	while True:
		if i*j > 1000000:
			break
		che[i*j] = 1
		j += 1
n, m = list(map(int, sys.stdin.readline().split()))
che = [0] * 1000001
for num in prime:
	i = int(n/num**2)
	while True:
		target = (num**2)*i
		if target > m:
			break
		if target < n:
			i += 1
			continue
		che[target-n]=1
		i += 1
re = 0
for i in range(0, m-n+1):
	if che[i] == 0:
		re += 1
print(re)
