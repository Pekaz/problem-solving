import sys

for t in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip()
    s += '0'
    cnt = 0
    re = ''
    for i in s:
        if cnt < int(i):
            re += '(' * abs(cnt - int(i))
            cnt += abs(cnt - int(i))
        elif cnt > int(i):
            re += ')' * abs(cnt - int(i))
            cnt -= abs(cnt - int(i))
        re += i
    print("Case #{}: {}".format(t+1, re[:-1]))

