import sys

max_num = 201

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    chk = []
    for i in range(n):
        if i == 0:
            chk.append([0]*max_num)
        else:
            chk.append(chk[i-1].copy())
        chk[i][num[i]] += 1
    re = 0
    for i in range(1, max_num):
        st = -1
        ed = -1
        midleft = -1
        midright = -1
        cnt = 0
        leftpv = int(chk[n - 1][i] / 2)
        rightpv = leftpv + 1
        if chk[n - 1][i] % 2 == 1:
            rightpv += 1
        for j in range(n):
            if num[j] == i:
                if st == -1:
                    st = j
                ed = j
                cnt += 1
                if cnt == leftpv:
                    midleft = j
                elif cnt == rightpv:
                    midright = j
        st -= 1
        if st < 0:
            st = 0
        midright -= 1
        if midright < 0:
            midright = 0
        for j in range(1, max_num):
            re = max(re, min(chk[st][j], chk[n-1][j] - chk[ed][j]) + chk[n-1][i])
            re = max(re, leftpv * 2 + (chk[midright][j] - chk[midleft][j]))
    print(re)


