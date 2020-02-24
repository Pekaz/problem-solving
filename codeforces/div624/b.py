import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    p = list(map(int, sys.stdin.readline().rstrip().split()))
    t = a.copy()
    t.sort()
    re = True
    for i in range(0, n):
        if a[i] == t[i]:
            continue
        for j in range(i, n):
            if a[i] == t[j]:
                st = min(i, j)
                ed = max(i, j)
                for k in range(st + 1, ed + 1):
                    if k not in p:
                        re = False
                        break
                break
    if re:
        print('YES')
    else:
        print('NO')
