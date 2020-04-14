import sys

max_num = 27

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    re = 0
    for i in range(1, max_num):
        for j in range(1, max_num):
            chk = []
            cntj = 0
            stj = -1
            edj = -1
            for k in num:
                if k == i or k == j:
                    if k == j:
                        if stj == -1:
                            stj = len(chk)
                        edj = len(chk)
                        cntj += 1
                    chk.append(k)
            if i == j:
                re = max(re, len(chk))
            elif len(chk) > 0 and stj >= 0 and edj >= 0:
                cnti = min(stj, len(chk)-(edj+1)) * 2
                re = max(re, cnti + cntj)
    print(re)

