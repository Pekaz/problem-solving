import sys

class fibo:
	result = []

	def fibonacci(self, n):
		if len(self.result) > n:
			return self.result[n]
		if n == 0:
			self.result.append((1,0))
			return (1,0)
		elif n == 1:
			self.result.append((0,1))
			return (0,1)
		a = self.fibonacci(n-1)
		b = self.fibonacci(n-2)
		self.result.append((a[0]+b[0], a[1]+b[1]))
		return self.result[n]

t = int(input())
fb = fibo()
for i in range(0, 41):
	fb.fibonacci(i)

for i in range(0, t):
	n = input()
	print(f'{fb.result[int(n)][0]} {fb.result[int(n)][1]}')


