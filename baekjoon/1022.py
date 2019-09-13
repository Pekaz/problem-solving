import sys
from time import sleep

r1, c1, r2, c2 = list(map(int, sys.stdin.readline().split()))
result = [[0] * (c2 - c1 + 1) for i in range(r2 - r1 + 1)]
count = 0
x = 0
y = 0
last = 1
dic = [[0,1],[-1,0],[0,-1],[1,0]]
re_count = 0

if r2 >= x >= r1 and c2 >= y >= c1:
	result[x - r1][y - c1] = str(last)
	re_count += 1

while True:
	length = int(count/2) + 1
	past_x = x
	past_y = y
	x += dic[count%4][0] * length
	y += dic[count%4][1] * length
	
	if ((x >= r2 and r1 >= past_x) or (past_x >= r2 and r1 >= x) or (r2 >= x >= r1) or (r2 >= past_x >= r1)) and ((y >= c2 and c1 >= past_y) or (past_y >= c2 and c1 >= y) or (c2 >= y >= c1) or (c2 >= past_y >= c1)):
		for _ in range(length):
			past_x += dic[count%4][0]
			past_y += dic[count%4][1]
			last += 1
			if r2 >= past_x >= r1 and c2 >= past_y >= c1:
				result[past_x - r1][past_y - c1] = str(last)
				re_count += 1
	else:
		last += length
	count += 1
	if re_count == (r2-r1 + 1) * (c2-c1 + 1):
		break

max_len = 0
for i in range(r2 - r1 + 1):
	for re in result[i]:
		if max_len < len(re):
			max_len = len(re)

re_str_list = []
for i in range(r2 - r1 + 1):
	re_str = ''
	for re in result[i]:
		re_str += ' ' * (max_len - len(re))
		re_str += re + ' '
	re_str_list.append(re_str)
	
for re_str in re_str_list:
	print(re_str)