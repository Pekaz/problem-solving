import sys

result = []
prime_list = []
check = []

for i in range(2, 2000):
	if i not in check:
		prime_list.append(i)
		j = 1
		while True:
			check.append(i * j)
			j += 1
			if i * j > 2000:
				break
n = int(sys.stdin.readline().split()[0])
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

n_prime = list([0] * n for _ in range(n))
for i in range(n):
	for j in range(n):
		if i == j: continue
		if (num_list[i] + num_list[j]) in prime_list:
			n_prime[i][j] = 1

def find_result(check, x, start):
	global reuslt
	global n
	global n_prime
	for i in range(x, n):
		if i == x or i in check:
			continue
		if n_prime[x][i] == 1:
			check.append(x)
			check.append(i)
			if len(check) == n:
				if start == 0:
					result.append(num_list[i])
				else:
					result.append(start)
				return

			for j in range(n):
				if j not in check:
					if x == 0:
						find_result(check, j, num_list[i])
					else:
						find_result(check, j, start)
					break
			check.remove(x)
			check.remove(i)


find_result([], 0, 0)
if len(result) == 0:
	result.append(-1)
result.sort()
for r in result:
	print(r, end=' ')
