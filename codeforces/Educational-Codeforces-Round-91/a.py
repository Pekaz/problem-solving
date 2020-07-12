import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    p = list(map(int, sys.stdin.readline().rstrip().split()))
    result = False
    re = ''
    for j in range(n):
        pi = -1
        for i in range(0, j):
            if p[i] < p[j]:
                pi = i
                break
        pz = -1
        for z in range(j + 1, n):
            if p[z] < p[j]:
                pz = z
                break
        if pi != -1 and pz != -1:
            result = True
            re = str(pi + 1) + ' ' + str(j + 1) + ' ' + str(pz + 1)
            break
    if result:
        print('YES')
        print(re)
    else:
        print('NO')
