import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    ppl = [[0, m, m]]
    for _ in range(n):
        ppl.append(list(map(int, sys.stdin.readline().rstrip().split())))
    i = 0
    x = m
    y = m
    enabled = False
    last = 0
    while True:
        if i == n:
            if last != ppl[i][0]:
                diff = ppl[i][0] - last
                if ppl[i][1] >= y:
                    if y + diff < ppl[i][1]:
                        break
                elif ppl[i][2] <= x:
                    if x - diff > ppl[i][2]:
                        break
            enabled = True
            break
        diff = ppl[i+1][0] - last
        if ppl[i+1][1] >= y:
            if y + diff < ppl[i+1][1]:
                break
            else:
                x = ppl[i+1][1]
                y += diff
                if ppl[i+1][2] < y:
                    y = ppl[i+1][2]
            last = ppl[i+1][0]
        elif ppl[i+1][2] <= x:
            if x - diff > ppl[i+1][2]:
                break
            else:
                x -= diff
                y = ppl[i+1][2]
                if ppl[i+1][1] > x:
                    x = ppl[i+1][1]
            last = ppl[i + 1][0]
        elif x <= ppl[i+1][1] and ppl[i+1][2] <= y:
            x = ppl[i+1][1]
            y = ppl[i+1][2]
            last = ppl[i + 1][0]
        elif ppl[i+1][1] <= x <= ppl[i+1][2] < y:
            x -= diff
            y = ppl[i + 1][2]
            if ppl[i + 1][1] > x:
                x = ppl[i + 1][1]
            last = ppl[i + 1][0]
        elif x < ppl[i+1][1] <= y <= ppl[i+1][2]:
            x = ppl[i + 1][1]
            y += diff
            if ppl[i + 1][2] < y:
                y = ppl[i + 1][2]
            last = ppl[i + 1][0]
        i += 1

    if enabled:
        print('YES')
    else:
        print('NO')



