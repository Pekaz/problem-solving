import sys

n,m = list(map(int, sys.stdin.readline().split()))
minimum_set = 1001
minimum_one = 1001
for _ in range(0, m):
	set_price, one_price = list(map(int, sys.stdin.readline().split()))
	if minimum_set > set_price:
		minimum_set = set_price
	if minimum_one > one_price:
		minimum_one = one_price
if minimum_one * 6 <= minimum_set:
	print(n*minimum_one)
else:
	result = int(n/6)*minimum_set
	if n%6 * minimum_one > minimum_set:
		result += minimum_set
	else:
		result += n%6 * minimum_one
	print(result)