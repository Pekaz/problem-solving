import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    re = n
    for i in range(2, n + 1):
        if n % i == 0:
            re = n + i + (2*(k-1))
            break
    print(re)
