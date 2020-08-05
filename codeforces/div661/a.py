import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    a.sort()
    re = 'YES'
    for i in range(n - 1):
        if a[i + 1] - a[i] > 1:
            re = 'NO'
            break
    print(re)
