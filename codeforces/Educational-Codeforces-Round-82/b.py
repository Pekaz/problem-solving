import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, g, b = list(map(int, sys.stdin.readline().split()))
    if n - int(n/2) <= g or g >= b:
        print(n)
    else:
        if int(n/2) > b:
            p = int(int(n/2)/b)
            re = (g + b) * p
            maked = re
            if int(n / 2) % b != 0:
                re += g + b
                maked += g + int(n / 2) % b
            if maked >= n:
                print(n)
                continue
            i = n - maked
            re += int(i / g) * (g + b) + i % g
            if i % g == 0:
                re -= b
        else:
            maked = int(n/2) + g
            re = g + b
            i = n - maked
            re += int(i / g) * (g + b) + i % g
            if i % g == 0:
                re -= b
        print(re)
