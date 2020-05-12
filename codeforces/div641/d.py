import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    a = list(map(int, sys.stdin.readline().rstrip().split()))

    re = 'no'
    for i in range(n):
        chk = []
        if i - 1 >= 0:
            chk.append(a[i - 1])
        chk.append(a[i])
        if i + 1 < n:
            chk.append(a[i + 1])
        chk.sort()
        if len(chk) == 1 or len(chk) == 2:
            if chk[0] == k:
                re = 'yes'
        else:
            if chk[1] == k:
                re = 'yes'
    print(re)
