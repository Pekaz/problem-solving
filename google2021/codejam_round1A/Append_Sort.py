import sys

for t in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    re = 0
    for i in range(1, n):
        if x[i] > x[i-1]:
            continue
        if x[i] == x[i-1]:
            x[i] *= 10
            re += 1
            continue

        x0 = str(x[i-1])
        x1 = str(x[i])
        tx0 = x0[:len(x1)]
        if int(tx0) < int(x1):
            gap = len(x0) - len(x1)
            re += gap
            x[i] *= 10**gap
        elif int(tx0) > int(x1):
            gap = len(x0) - len(x1) + 1
            re += gap
            x[i] *= 10 ** gap
        else:
            px0 = x0[len(x1)-len(x0):]
            px0_re = int(px0) + 1
            if len(str(px0_re)) > len(px0):
                re += (len(x0) - len(x1) + 1)
                x1 += '0' * (len(str(x0)) - len(x1) + 1)
                x[i] = int(x1)
            else:
                if len(str(px0_re)) < len(px0):
                    px0_re = f'{px0_re:0{len(px0)}}'
                x1 += str(px0_re)
                x[i] = int(x1)
                re += len(str(px0_re))

    print("Case #{}: {}".format(t + 1, re))
