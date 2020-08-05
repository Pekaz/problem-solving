import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    b = list(map(int, sys.stdin.readline().rstrip().split()))
    amin = min(a)
    bmin = min(b)
    for i in range(n):
        a[i] -= amin
        b[i] -= bmin
    re = 0
    for i in range(n):
        re += max(a[i], b[i])
    print(re)
