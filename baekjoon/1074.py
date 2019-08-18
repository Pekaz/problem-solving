import sys

class zclass:
	result = 0
	r = 0
	c = 0
	def goback(self, m, x, y):
		if m == 1:
			if x == self.r and y == self.c:
				print(int(self.result))
			return
		
		if x <= self.r < x + int(m/2) and y <= self.c < y + int(m/2):
			self.goback(int(m/2), x, y)
		elif  x <= self.r < x + int(m/2) and y + int(m/2) <= self.c:
			self.result += (m/2)**2
			self.goback(int(m/2), x, y + int(m/2))
		elif  x + int(m/2) <= self.r and y <= self.c < y + int(m/2):
			self.result += (m/2)**2 * 2
			self.goback(int(m/2), x + int(m/2), y)
		else:
			self.result += (m/2)**2 * 3
			self.goback(int(m/2), x + int(m/2), y + int(m/2))

z = zclass()
n,r,c = list(map(int, sys.stdin.readline().split()))
z.r = r
z.c = c
z.goback(2**n, 0, 0)
