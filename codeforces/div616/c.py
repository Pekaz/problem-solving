for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    num = list(map(int, input().split()))
    d = []
    for _ in range(n):
        d.append([[0] * (k + 1) for _ in range(n)])

    for i in range(0, n - (m - 1) + 1):
        d[n - (m - 1)][i][0] = (num[i] if num[i] > num[i + n - m] else num[i + n - m])
    for j in range(2, m):
        for i in range(0, n - (m - j) + 1):
            chk = j if j < k else k
            for p in range(1, chk + 1):
                if p == 0:
                    if num[i] > num[i + n - (m - j + 1)]:
                        d[n - (m - j)][i][p] = d[n - (m - (j - 1))][i + 1][p]
                    else:
                        d[n - (m - j)][i][p] = d[n - (m - (j - 1))][i][p]
                else:
                    d[n - (m - j)][i][p] = d[n - (m - (j - 1))][i + 1][p - 1]
                    if d[n - (m - j)][i][p] < d[n - (m - (j - 1))][i][p - 1]:
                        d[n - (m - j)][i][p] = d[n - (m - (j - 1))][i][p - 1]
                    if num[i] > num[i + n - (m - j)]:
                        if d[n - (m - j)][i][p] < d[n - (m - (j - 1))][i + 1][p]:
                            d[n - (m - j)][i][p] = d[n - (m - (j - 1))][i + 1][p]
                    else:
                        if d[n - (m - j)][i][p] < d[n - (m - (j - 1))][i][p]:
                            d[n - (m - j)][i][p] = d[n - (m - (j - 1))][i][p]
    print(d[n][0][k])
