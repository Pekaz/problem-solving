import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    b = list(map(int, sys.stdin.readline().rstrip().split()))
    a.sort()
    b.sort()
    for i in a:
        print(i, end=' ')
    print('')
    for i in b:
        print(i, end=' ')
    print('')
