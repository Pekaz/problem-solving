import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    x, y, n = list(map(int, sys.stdin.readline().rstrip().split()))
    re = int(n/x) * x + y
    if re > n:
        re -= x
    print(re)
