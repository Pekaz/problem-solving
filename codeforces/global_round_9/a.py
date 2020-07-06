import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    c1 = 0
    c2 = 0
    i = 1
    while True:
        if a[i] - a[i - 1] > 0:
            if c1 > c2:
                a[i] *= -1
                if a[i] - a[i - 1] > 0:
                    a[i] *= -1
                    a[i - 1] *= -1
                    i -= 1
                    continue
                c2 += 1
            else:
                c1 += 1
        elif a[i] - a[i - 1] < 0:
            if c1 <= c2:
                a[i] *= -1
                if a[i] - a[i - 1] < 0:
                    a[i] *= -1
                    a[i - 1] *= -1
                    i -= 1
                    continue
                c1 += 1
            else:
                c2 += 1
        else:
            if c1 <= c2:
                c1 += 1
            else:
                c2 += 1
        i += 1
        if i == n:
            break
    for i in a:
        print(i, end=' ')
    print('')
