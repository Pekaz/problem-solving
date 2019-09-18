import sys

n = sys.stdin.readline().split()[0]
calc = list([0]*2 for _ in range(10))
calc[0][0] = 1
calc[0][1] = 1
for i in range(1, 10):
	if i > 1:
		for j in range(1, i):
			calc[i][0] += 10**j
	for j in range(0, i):
		calc[i][0] += calc[j][0]
		calc[i][1] += calc[j][1]
	calc[i][0] *= 9
	calc[i][1] *= 9
	calc[i][1] += 10**i

n_list = list(n)
result = [0]*10

if len(n_list) > 1:
	for i in range(len(n_list) - 1):
		result[0] += calc[i][0]
		for j in range(1, 10):
			result[j] += calc[i][1]

for idx, ch in enumerate(n_list):
	num = int(ch)
	if idx == len(n_list) - 1:
		for i in range(num + 1):
			result[i] += 1
		break
	for i in range(0, num + 1):
		if idx == 0 and i == 0:
			continue
		if i < num:
			result[i] += 10**(len(n_list)-idx-1)
			for j in range(len(n_list)-idx-1):
				result[0] += calc[j][0]
				if len(n_list)-(idx+j+2) > 0:
					result[0] += 10**(len(n_list)-(idx+j+2))
				for z in range(1, 10):
					result[z] += calc[j][1]
		else:
			result[i] += (int(n) % (10**(len(n_list) - idx - 1)) + 1)
result[0] -= 1
for r in result:
	print(r, end=' ')

