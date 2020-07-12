import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip()
    re = ''
    cnt = {}
    for i in s:
        if i not in cnt:
            cnt[i] = 1
        else:
            cnt[i] += 1
    max_v = -1
    re = ''
    for i, v in cnt.items():
        if max_v < v:
            max_v = v
            re = i
    if re == 'R':
        re = 'P'
    elif re == 'S':
        re = 'R'
    elif re == 'P':
        re = 'S'
    print(re * len(s))
