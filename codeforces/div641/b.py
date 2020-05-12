import sys

re = 0
n = 0
s = []


def goback(x, cnt):
    global re
    global n
    global s

    if re < cnt:
        re = cnt

    j = 2
    while True:
        if (x + 1) * j > n:
            break
        if s[(x + 1) * j - 1] > s[x]:
            goback((x + 1) * j - 1, cnt + 1)
        j += 1


for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    s = list(map(int, sys.stdin.readline().rstrip().split()))
    re = 0
    for i in range(n):
        goback(i, 1)
    print(re)
