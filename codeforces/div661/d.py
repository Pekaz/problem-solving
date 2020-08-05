import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    w = sys.stdin.readline().rstrip()
    rew = [0] * n
    re = 0
    end_zero = []
    end_one = []
    st = 0
    while True:
        if st >= n:
            break
        last = w[st]
        i = st + 1
        while True:
            if i >= n:
                break
            if w[i] == last:
                break
            last = w[i]
            i += 1

        if w[st] == '1' and len(end_zero) > 0:
            check = end_zero.pop(0)
        elif w[st] == '0' and len(end_one) > 0:
            check = end_one.pop(0)
        else:
            re += 1
            check = re

        for j in range(st, i):
            rew[j] = check
        if last == '0':
            end_zero.append(check)
        if last == '1':
            end_one.append(check)
        st = i
    print(re)
    for i in rew:
        print(i, end=' ')
    print('')
