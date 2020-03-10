import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    if n % m == 0:
        print('YES')
    else:
        print('NO')
