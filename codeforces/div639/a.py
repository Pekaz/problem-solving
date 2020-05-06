import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    if n == 2 and m == 2:
        print('YES')
    elif n == 1 or m == 1:
        print('YES')
    else:
        print('NO')
