import sys


def checkleft(a, b):
    long1 = a
    short1 = b
    if len(b) > len(a):
        long1 = b
        short1 = a
    for i in range(len(short1)):
        if long1[i] != short1[i]:
            return False
    return True


def checkright(a, b):
    long1 = a[::-1]
    short1 = b[::-1]
    if len(b) > len(a):
        long1 = b[::-1]
        short1 = a[::-1]
    for i in range(len(short1)):
        if long1[i] != short1[i]:
            return False
    return True


for t in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    p = []
    for _ in range(n):
        p.append(sys.stdin.readline().rstrip())
    pre = ''
    post = ''
    re = ''
    for i in range(n):
        if i == 0:
            pv = p[i].find('*')
            pre = p[i][:pv]
            post = p[i][pv+1:]
        else:
            pv = p[i].find('*')
            p1 = p[i][:pv]
            p2 = p[i][pv + 1:]
            if checkleft(pre, p1):
                if len(p1) > len(pre):
                    pre = p1
            else:
                re = '*'
            if checkright(post, p2):
                if len(p2) > len(post):
                    post = p2
            else:
                re = '*'

            if re == '*':
                break
    if re != '*':
        re = pre + post
    print("Case #{}: {}".format(t + 1, re))
