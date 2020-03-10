import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
k = m - n + 2
print(int((k + 1) * k / 2) % 998244353)
