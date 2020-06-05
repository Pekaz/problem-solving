import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    s = list(map(int, sys.stdin.readline().rstrip().split()))
    mx = max(s)
    re = -1
    for k in range(1, 2049):
        t = []
        for i in s:
            chk = (i ^ k)
            if chk not in t and chk in s:
                t.append(chk)
            else:
                break
        if len(t) == n:
            re = k
            break
    print(re)


