import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    w = list(map(int, sys.stdin.readline().rstrip().split()))
    w.sort()
    target = []
    for i in range(n):
        for j in range(i + 1, n):
            if w[i] + w[j] not in target:
                target.append(w[i] + w[j])
    re = 0
    for i in target:
        a = w.copy()
        cnt = 0
        while True:
            if len(a) == 0:
                break
            first = a.pop(0)
            try:
                idx = a.index(i - first)
                a.pop(idx)
                cnt += 1
            except ValueError:
                pass
        re = max(re, cnt)
    print(re)
