import sys

def change(map, x, y):
	for i in range(x-1, x+2):
		for j in range(y-1, y+2):
			map[i][j] ^= 1

n,m = list(map(int, sys.stdin.readline().split()))
map1 = []
map2 = []
re = 0
for _ in range(0, n):
	line = list(sys.stdin.readline().split()[0])
	map1.append(list(map(int, line)))
for _ in range(0, n):
	line = list(sys.stdin.readline().split()[0])
	map2.append(list(map(int, line)))

for i in range(1, n-1):
	for j in range(1, m-1):
		if map1[i-1][j-1] != map2[i-1][j-1]:
			re += 1
			change(map1, i, j)
for i in range(0, n):
	for j in range(0, m):
		if map1[i][j] != map2[i][j]:
			re = -1
print(re)

