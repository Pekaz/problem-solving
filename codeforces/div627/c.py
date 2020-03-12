import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip() + 'E'
    chk = [0] * (len(s))
    cnt = 1
    for i in range(len(s)):
        chk[i] = cnt
        cnt += 1
        if s[i] == 'R':
            cnt = 1
    print(max(chk))
