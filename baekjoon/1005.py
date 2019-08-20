import sys

class Queue:
	arr = []
	def push(self, x):
		self.arr.append(x)
	def pop(self):
		re = self.arr[0]
		del self.arr[0]
		return re

t = int(sys.stdin.readline().split()[0])

for _ in range(0, t):
	n, k = list(map(int, sys.stdin.readline().split()))
	build = list(map(int, sys.stdin.readline().split()))
	path = {}
	needs = [0]*(n+1)
	for _ in range(0, k):
		x, y = list(map(int, sys.stdin.readline().split()))
		if x == y:
			continue
		needs[y] += 1
		if x in path:
			path[x].append(y)
		else:
			path[x] = [y]
	r = int(sys.stdin.readline().split()[0])
	cost = [0]*(n+1)
	qu = Queue()

	for i in range(1, n+1):
			if needs[i] == 0:
				cost[i] = build[i - 1]
				qu.push(i)

	while True:
		if len(qu.arr) == 0:
			break
		target = qu.pop()
		if target not in path:
			continue
		for kid in path[target]:
			needs[kid] -= 1
			if cost[kid] < cost[target] + build[kid -1]:
				cost[kid] = cost[target] + build[kid -1]

			if needs[kid] == 0:
				qu.push(kid)
	print(cost[r])