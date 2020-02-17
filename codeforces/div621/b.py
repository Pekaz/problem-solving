import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, x = list(map(int, sys.stdin.readline().rstrip().split()))
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    num.sort()
    if x in num:
        print(1)
        continue
    elif num[-1:][0] * 2 >= x:
        print(2)
        continue
    else:
        chk = x - num[-1:][0] * 2
        re = int(chk/num[-1:][0]) + 2
        if chk % num[-1:][0] != 0:
            re += 1
        print(re)
