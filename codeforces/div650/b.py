import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    cnt0 = 0
    cnt1 = 0
    for i in range(n):
        a[i] = a[i] % 2
        if a[i] == 0:
            cnt0 += 1
        elif a[i] == 1:
            cnt1 += 1
    if (n % 2 == 0 and cnt0 != cnt1) or (n % 2 == 1 and cnt0 != cnt1 + 1):
        print(-1)
        continue
    else:
        re = 0
        for i in range(n):
            if a[i] != i % 2:
                re += 1
        print(int(re/2))
