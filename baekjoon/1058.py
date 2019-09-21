import sys

n = int(sys.stdin.readline().split()[0])
fri = []
for _ in range(n):
	fri.append(list(sys.stdin.readline().split()[0]))

re = 0

for i in range(n):
	check = [0]*n
	for j in range(n):
		if fri[i][j] == 'Y':
			check[j]=1
			for z in range(n):
				if fri[j][z] == 'Y':
					check[z] = 1
	cnt = 0
	for j in range(n):
		if j == i:
			continue
		cnt += check[j]
	if re < cnt:
		re = cnt
print(re)