import sys

n = int(sys.stdin.readline())
result = ''
length = 0
for _ in range(0, n):
	text = sys.stdin.readline()
	if len(result) == 0:
		result = text
		length = len(text)
		continue
	for i in range(0, length):
		if result[i]!=text[i]:
			result = result[:i] + '?' + result[i+1:]
print(result)
