import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    ppl = [[0, m, m]]
    for _ in range(n):
        ppl.append(list(map(int, sys.stdin.readline().rstrip().split())))
    i = 0
    x = m
    y = m
    enabled = True
    last = 0
    for p in ppl:
        diff = p[0] - last
        if x - diff > p[2] or y + diff < p[1]:
            enabled = False
            break
        x = max(x - diff, p[1])
        y = min(y + diff, p[2])
        last = p[0]

    if enabled:
        print('YES')
    else:
        print('NO')



