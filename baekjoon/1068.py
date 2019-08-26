import sys

class Queue:
	arr = []
	def push(self, x):
		self.arr.append(x)
	def pop(self):
		re = self.arr[0]
		del self.arr[0]
		return re

n = int(sys.stdin.readline().split()[0])
num = list(map(int, sys.stdin.readline().split()))
tree = {}
qu = Queue()
m = int(sys.stdin.readline().split()[0])
for i, node in enumerate(num):
	if node == -1 and i != m:
		qu.push(i)
		continue
	if node not in tree:
		tree[node] = [i]
	else:
		tree[node].append(i)
re = 0
while True:
	if len(qu.arr) == 0:
		break
	node = qu.pop()
	if node not in tree:
		re += 1
		continue
	for child in tree[node]:
		if child == m:
			if len(tree[node]) == 1:
				re += 1
			continue
		qu.push(child)
print(re)