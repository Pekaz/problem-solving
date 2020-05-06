import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    re = 'YES'
    chk = []
    for idx, i in enumerate(a):
        if idx + i in chk:
            re = 'NO'
            break
        chk.append(idx + i)
    chk = []
    for idx, i in enumerate(a):
        if idx - i in chk:
            re = 'NO'
            break
        chk.append(idx + i)
    print(re)
