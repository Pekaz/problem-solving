import sys
from decimal import Decimal

for t in range(int(sys.stdin.readline().rstrip())):
    r, c = list(map(int, sys.stdin.readline().rstrip().split()))
    n = []
    for _ in range(r):
        n.append(list(map(int, sys.stdin.readline().rstrip().split())))
    re = 0
    target = []
    while True:
        chk = 0
        for i in range(r):
            for j in range(c):
                chk += n[i][j]
        re += chk
        target = []
        for i in range(r):
            for j in range(c):
                if n[i][j] == 0:
                    continue
                avg = 0.0
                cnt = 0
                for z in range(i-1, -1, -1):
                    if n[z][j] != 0:
                        avg += n[z][j]
                        cnt += 1
                        break
                for z in range(j-1, -1, -1):
                    if n[i][z] != 0:
                        avg += n[i][z]
                        cnt += 1
                        break
                for z in range(i+1, r):
                    if n[z][j] != 0:
                        avg += n[z][j]
                        cnt += 1
                        break
                for z in range(j+1, c):
                    if n[i][z] != 0:
                        avg += n[i][z]
                        cnt += 1
                        break
                if cnt > 0 and n[i][j] < Decimal(avg/cnt):
                    target.append((i, j))
        if len(target) == 0:
            break
        for il in target:
            n[il[0]][il[1]] = 0

    print("Case #{}: {}".format(t + 1, re))
