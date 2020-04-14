import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    num = list(map(int, sys.stdin.readline().rstrip().split()))

    chk = [0] * (n + 1)
    cntx = 0
    cnty = 0
    for i in num:
        if chk[i] == 0:
            cntx += 1
        chk[i] += 1
        cnty = max(cnty, chk[i])
    re = max(min(cnty, cntx - 1), min(cnty-1, cntx))
    print(re)
