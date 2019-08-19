import sys

n,m = list(map(int, sys.stdin.readline().split()))
chess = []
for _ in range(0, n):
	line = sys.stdin.readline().split()[0]
	chess.append(line)
result = 65
check = ["BWBWBWBW", "WBWBWBWB"]
for i in range(0, n-7):
	for j in range(0, m-7):
		count = 0
		for x in range(0, 8):
			for y in range(0, 8):
				if chess[i+x][j+y] != check[x%2][y]:
					count += 1
		if result > count:
			result = count
		count = 0
		for x in range(0, 8):
			for y in range(0, 8):
				if chess[i+x][j+y] != check[(x+1)%2][y]:
					count += 1
		if result > count:
			result = count
print(result)

