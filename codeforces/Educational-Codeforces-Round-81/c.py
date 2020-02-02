from collections import defaultdict

T = int(input())

for _ in range(T):
	s = input()
	t = input()
	
	for i in range(len(s)):
		if i == 0:
			continue
		num = lens - 1 - i
		if i > 0:
			for j in range(26):
				check[num][j] = check[num + 1][j]
		if check[num][ord(s[num + 1]) - ord('a')] == -1 or check[num][ord(s[num + 1]) - ord('a')] > num:
			check[num][ord(s[num + 1]) - ord('a')] = num + 1
	init = check[0].copy()
	init[ord(s[0]) - ord('a')] = 0
	result = 0
	last = 0
	for c in t:
		num = ord(c) - ord('a')
		if result == 0:
			result = 1
			last = init[num]
			if last == -1:
				result = -1
				break
			continue
		last = check[last][num]
		if last == -1:
			last = init[num]
			if last == -1:
				result = -1
				break
			result += 1
	print(result)




