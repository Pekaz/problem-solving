import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    num = sys.stdin.readline().rstrip()
    x = 0
    y = 0
    cnt = 0
    for idx, i in enumerate(num):
        if i == '1':
            x = idx
            break
    rev_num = num[::-1]
    for idx, i in enumerate(rev_num):
        if i == '1':
            y = len(rev_num) - idx
            break
    for i in range(x, y):
        if num[i] == '0':
            cnt += 1
    print(cnt)
