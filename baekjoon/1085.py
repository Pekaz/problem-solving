import sys

x, y, w, h = map(int, sys.stdin.readline().split())
result = x
if result > w-x:
	result = w-x
if result > y:
	result = y
if result > h-y:
	result = h-y
print(result)