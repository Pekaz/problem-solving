import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    num.sort()
    re = num[::-1]
    for i in re:
        print(i, end=' ')
    print('')
