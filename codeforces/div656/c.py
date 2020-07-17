import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    if n == 1:
        print(0)
        continue
    x = n - 2
    inc = True
    if a[n - 2] < a[n - 1]:
        inc = False
    while True:
        if x == 0:
            break
        if inc is False and a[x - 1] > a[x]:
            break
        elif inc and a[x - 1] < a[x]:
            inc = False
        x -= 1
    print(x)

