import sys

class queue:
	qu = []
	def push(self, n):
		self.qu.append(n)
	def pop(self):
		ret = self.qu[0]
		del self.qu[0]
		return ret


t = int(input())
direction = [[0,1],[1,0],[0,-1],[-1,0]]
for _ in range(0, t):
	result = 0

	line = input().split()
	m = int(line[0])
	n = int(line[1])
	k = int(line[2])
	mapp = []
	for _ in range(0, n):
		mapp.append([0] * m)

	for _ in range(0, k):
		bug = input().split()
		x = int(bug[0])
		y = int(bug[1])
		mapp[y][x] = 1

	qu = queue()
	for i in range(0, n):
		for j in range(0, m):
			if mapp[i][j] == 1:
				qu.push((i, j))
				mapp[i][j] = 0
				while True:
					if len(qu.qu) == 0:
						break
					bug = qu.pop()
					for k in range(0,4):
						new_bug = (bug[0] + direction[k][0], bug[1] + direction[k][1])
						if 0 <= new_bug[0] < n and 0 <= new_bug[1] < m and mapp[new_bug[0]][new_bug[1]] == 1:
							qu.push(new_bug)
							mapp[new_bug[0]][new_bug[1]] = 0
				result += 1
	print(result)

