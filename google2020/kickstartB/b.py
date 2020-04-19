import sys

for t in range(int(sys.stdin.readline().rstrip())):
    n, d = list(map(int, sys.stdin.readline().rstrip().split()))
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    check = d
    re = -1
    for i in x[::-1]:
        if re == -1:
            re = int(check/i)*i
        else:
            re = min(re, int(check/i)*i)
        check = re
    print("Case #{}: {}".format(t + 1, re))
