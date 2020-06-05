import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    t = "{0:b}".format(n)
    re = 0
    tlen = len(t)
    for i in range(tlen):
        if t[i] == '1':
            re += 2 ** (tlen - i) - 1
    print(re)
