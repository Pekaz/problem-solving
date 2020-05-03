import sys

check = {}
re = []


def goback(x):
    global check
    global re

    if x == len(check.keys()):
        return True
    for key in check:
        if check[key][0] <= x <= check[key][1] and key not in re:
            re.append(key)
            if goback(x+1):
                return True
            re = re[:-1]
    return False


for t in range(int(sys.stdin.readline().rstrip())):
    u = int(sys.stdin.readline().rstrip())
    m = []
    r = []
    re = []
    check = {}
    for i in range(10000):
        mi, ri = list(sys.stdin.readline().rstrip().split())
        m.append(mi)
        r.append(ri)
        for rc in ri:
            if rc not in check:
                check[rc] = [0, 9]
        check[ri[0]][0] = 1

    for i in range(10000):
        if int(m[i]) == -1 or len(m[i]) > len(r[i]):
            continue
        for idx, c in enumerate(r[i]):
            if idx == 0:
                if check[c][1] > int(m[i][idx]):
                    check[c][1] = int(m[i][idx])
            else:
                if check[c][1] > 9:
                    check[c][1] = 9
    goback(0)
    print("Case #{}: ".format(t + 1), end='')
    for rec in re:
        print(rec, end='')
    print('')
