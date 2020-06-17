import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    s = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    b = list(map(int, sys.stdin.readline().rstrip().split()))
    s = list(s)
    s.sort(reverse=True)
    re = ['0'] * n
    re_cnt = 0
    while True:
        if re_cnt == n:
            break
        zero_cnt = 0
        zero_target = []
        for i in range(n):
            if b[i] == 0:
                zero_cnt += 1
                zero_target.append(i)
        x = 0
        while True:
            word_cnt = 0
            target = s[x]
            last = 0
            for i in range(x, len(s)):
                if s[i] == target:
                    word_cnt += 1
                else:
                    last = i
                    break
            if word_cnt >= zero_cnt:
                break
            else:
                x = last
        for i in zero_target:
            re[i] = target
            for j in range(n):
                if b[j] > 0:
                    b[j] -= abs(j-i)
            b[i] = -1
            re_cnt += 1
        while True:
            if len(s) == 0:
                break
            if target <= s[0]:
                s.remove(s[0])
            else:
                break
    for i in re:
        print(i, end='')
    print()
