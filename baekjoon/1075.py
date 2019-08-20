import sys
n = sys.stdin.readline().split()[0]
f = int(sys.stdin.readline().split()[0])

for i in range(0, 100):
	num = f'{n[:-2]}{i:02}'
	if int(num) % f == 0:
		print(f'{i:02}')
		break
