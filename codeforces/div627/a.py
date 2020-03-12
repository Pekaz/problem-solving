import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    m = min(num)
    re = True
    for i in num:
        if (i - m) % 2 != 0:
            re = False
            break
    if re:
        print('YES')
    else:
        print('NO')
