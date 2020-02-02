
for _ in range(int(input())):
	n = int(input())
	s = input()
	check = [0] * n
	for i in range(n):
		if i == 0:
			check[0] = int(s[0])
			continue
		check[i] = check[i-1] + int(s[i])
	t = s
	chk1 = False
	for i in range(n):
		if int(t[-1:]) % 2 == 1:
			chk1 = True
			break
		t = t[:-1]

	nt = len(t)
	if not chk1 or nt <= 1:
		print(-1)
		continue

	if check[nt - 1] % 2 == 0:
		print(t)
		continue
	for i, c in enumerate(t):
		if int(c) % 2 == 1:
			if i == 0 and t[i + 1] == '0':
				continue
			if i == nt - 1:
				print(-1)
				break
			print(t[0:i] + t[i+1:nt])
			break




