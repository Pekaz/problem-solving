import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    a.sort()
    chk = 1
    re = 1
    for i in a:
        if chk >= i:
            re = chk + 1
        chk += 1
    print(re)
