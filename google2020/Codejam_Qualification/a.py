import sys

for t in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    dig = []
    re_sum = 0
    for i in range(n):
        dig.append(list(map(int, sys.stdin.readline().rstrip().split())))
        re_sum += dig[i][i]
    re_x = 0
    re_y = 0
    for i in range(n):
        chk = [0] * n
        for j in range(n):
            if chk[dig[i][j]-1] == 1:
                re_x += 1
                break
            chk[dig[i][j]-1] = 1
    for i in range(n):
        chk = [0] * n
        for j in range(n):
            if chk[dig[j][i]-1] == 1:
                re_y += 1
                break
            chk[dig[j][i]-1] = 1
    print("Case #{}: {} {} {}".format(t+1, re_sum, re_x, re_y))

