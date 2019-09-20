import sys

k, st, n = list(sys.stdin.readline().split())
st = [ord(st[0])-ord('A'), ord(st[1])-ord('1')]
k = [ord(k[0])-ord('A'), ord(k[1])-ord('1')]
direc = {'B': [0, -1], 'T': [0, 1], 'L': [-1, 0], 'R': [1, 0]}

for _ in range(int(n)):
	mv = sys.stdin.readline().split()[0]
	stone_check = False
	for ch in mv:
		k[0] += direc[ch][0]
		k[1] += direc[ch][1]
	if (st[0] == k[0] and st[1] == k[1]):
		stone_check = True
		for ch in mv:
			st[0] += direc[ch][0]
			st[1] += direc[ch][1]
	if not (0 <= st[0] <= 7 and 0 <= st[1] <= 7 and 0 <= k[0] <= 7  and 0 <= k[1] <= 7):
		for ch in mv:
			k[0] += direc[ch][0] * -1
			k[1] += direc[ch][1] * -1
			if stone_check:
				st[0] += direc[ch][0] * -1
				st[1] += direc[ch][1] * -1
				
st = chr(st[0]+ord('A')) + chr(st[1]+ord('1'))
k = chr(k[0]+ord('A')) + chr(k[1]+ord('1'))

print(k)
print(st)
