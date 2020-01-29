import sys

t = int(sys.stdin.readline())

for _ in range(t):
	n,m = list(map(int, sys.stdin.readline().split()))
	re = 0
	if m == 0:
		re += 1
	s = sys.stdin.readline().split()[0]
	n_sum = []
	for i, c in enumerate(s):
		if i == 0:
			n_sum.append(1 if c == '0' else -1)
		else:
			n_sum.append(n_sum[i-1] + (1 if c == '0' else -1))
	cycle = n_sum[-1:][0]
	if cycle == 0:
		flag = False
		for i in n_sum:
			if i == m:
				flag = True
				break
		if flag:
			print(-1)
		else:
			print(0)
		continue
	for i in n_sum:
		if((m - i)%cycle == 0 and int((m - i)/cycle)>=0):
			re += 1
	print(re)



