import sys



n = int(sys.stdin.readline())
if n < 10:
	print(n)
	exit()

re = [9]

for i in range(0, n - 9):
	x = 0
	re[x] += 1
	while True:
		if re[x] == 10:
			if x == len(re) - 1:
				re.append(0)
				for i in range(0, len(re)):
					if i > 9:
						print(-1)
						exit()
					re[i] = i
				break
			else:
				if x == 0:
					re[x] = 0
				else:
					re[x] = re[x - 1] + 1
				re[x+1] += 1
				x += 1
		if x == len(re) - 1:
			break
		if re[x] == re[x+1]:
			re[x+1] += 1
			if x == 0:
				re[x] = 0
			else:
				re[x] = re[x-1] + 1
			x += 1
		else:
			break
re.reverse()
for i in re:
	print(i, end='')