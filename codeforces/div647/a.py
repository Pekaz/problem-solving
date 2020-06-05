import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    a, b = max(a, b), min(a, b)
    re = 0
    c = 0
    while True:
        if a == b:
            break
        if b > a:
            re = -1
            break
        b *= 2
        c += 1
    if re != -1:
        re += int(c/3)
        c = c % 3
        if c > 0:
            re += 1
    print(re)





