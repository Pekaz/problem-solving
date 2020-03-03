import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
a = list(map(int, sys.stdin.readline().rstrip().split()))

if n <= m:
    re = 1
    for i in range(n):
        for j in range(i + 1, n):
            re *= abs(a[i]-a[j])
            if re > m:
                re %= m
    print(re % m)
else:
    print(0)
