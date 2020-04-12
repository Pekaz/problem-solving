import sys
import math

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    num.sort()
    re = []
    pv = int(math.ceil(len(num)/2)) - 1
    sz = 1

    while True:
        if len(num) == len(re):
            break
        re.append(num[pv])
        pv += sz
        sz *= -1
        if sz < 0:
            sz -= 1
        else:
            sz += 1
    for i in re:
        print(i, end=' ')
    print('')
