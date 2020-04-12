import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    m1 = num[0]
    chk = 0
    for i in range(1, n):
        m1 = max(m1, num[i])
        chk = max(chk, m1-num[i])
    re = 0
    tmp = 0
    while True:
        if tmp >= chk:
            break
        tmp += (2 ** re)
        re += 1
    print(re)
