import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
a = list(map(int, sys.stdin.readline().rstrip().split()))
a.sort()
diff = []
for i in range(n - 1):
    diff.append(a[i + 1] - a[i])
