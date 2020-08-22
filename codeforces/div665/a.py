import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    re = k - n
    if re < 0:
        if n % 2 == k % 2:
            re = 0
        else:
            re = 1
    print(re)
