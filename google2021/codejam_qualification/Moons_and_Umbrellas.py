import sys

for t in range(int(sys.stdin.readline().rstrip())):
    x, y, s = sys.stdin.readline().rstrip().split()
    x = int(x)
    y = int(y)
    s = s.replace('?', '')
    re = 0
    for i in range(len(s) - 1):
        if s[i] + s[i+1] == 'CJ':
            re += x
        elif s[i] + s[i+1] == 'JC':
            re += y
    print("Case #{}: {}".format(t + 1, re))
