import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    x, y, a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    i = 0
    j = 1000000000
    re = 0
    while True:
        mid = int((i+j)/2)
        if x + mid * a == y - mid * b:
            print(mid)
            break
        if x + mid * a > y - mid * b:
            j = mid - 1
        elif x + mid * a < y - mid * b:
            i = mid + 1
        if i > j:
            print(-1)
            break
