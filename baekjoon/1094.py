import sys

n = bin(int(sys.stdin.readline()))[2:]
result = 0
for i in n:
	result += int(i)
print(result)