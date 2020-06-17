import sys

s = []
n = 0
b = []
chk = []
re = []


def goback(si, check):
    global n
    global s
    global b
    global chk
    global re
    if si == n:
        return True
    for i in range(len(check)):
        if check[i] == 0:
            for j in range(n):
                if re[j] == '0':

                    check[i] = 1
                    re[j] = s[i]
                    can = True
                    for k in range(n):
                        if re[k] == '0':
                            continue
                        cal = 0
                        for z in range(n):
                            if re[z] != '0' and re[z] > re[k]:
                                cal += abs(chk[z][0] - chk[k][0])
                        if cal != chk[k][1]:
                            can = False
                    if can:
                        if goback(si + 1, check):
                            return True
                    check[i] = 0
                    re[j] = '0'
    return False


for _ in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    b = list(map(int, sys.stdin.readline().rstrip().split()))
    s = list(s)
    s.sort(reverse=True)
    re = ['0'] * n
    chk = []
    for idx, i in enumerate(b):
        chk.append((idx, i))
    chk.sort(key=lambda element: element[1])
    goback(0, [0]*len(s))
    result = []
    for i in range(n):
        result.append((chk[i][0], re[i]))
    result.sort(key=lambda element: element[0])
    for i in result:
        print(i[1], end='')
    print()
