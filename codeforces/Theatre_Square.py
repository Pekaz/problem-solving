import sys

line = sys.stdin.readline()
array = line.split(' ')
n = int(array[0])
m = int(array[1])
a = int(array[2])

re_a = int(n / a)
re_b = int(m / a)
if n % a != 0:
    re_a += 1

if m % a != 0:
    re_b += 1

print(re_a*re_b)
