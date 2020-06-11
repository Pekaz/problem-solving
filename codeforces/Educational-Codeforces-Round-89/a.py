import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    n, m = min(n, m), max(n, m)
    re = 0
    if m - n > 1:
        re += min(m - n, n)
        n -= re
        m -= re * 2
    cnt = int(min(n, m) / 3)
    re += cnt * 2
    n -= cnt * 3
    m -= cnt * 3
    re += min(n, int(m/2))

    print(re)

