import sys

for t in range(int(sys.stdin.readline().rstrip())):
    n, k, p = list(map(int, sys.stdin.readline().rstrip().split()))
    plates = []
    for _ in range(n):
        plates.append(list(map(int, sys.stdin.readline().rstrip().split())))
    d = []
    for _ in range(n + 1):
        d.append([0] * (p + 1))
    for i in range(1, p + 1):
        if (i - 1) >= k:
            break
        d[0][i] = d[0][i - 1] + plates[0][i - 1]
    for i in range(1, n):
        for j in range(0, p + 1):
            re = 0
            summ = 0
            for x in range(0, j + 1):
                re = max(re, d[i-1][j-x] + summ)
                if x < k:
                    summ += plates[i][x]
            d[i][j] = re
    print('Case #{}: {}'.format(t+1, d[n-1][p]))
