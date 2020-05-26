import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    re = int(n/2) * m
    if n % 2 == 1:
        re += int((m + 1) / 2)
    print(re)
