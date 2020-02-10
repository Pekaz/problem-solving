import sys
for _ in range(int(input())):
    n = int(sys.stdin.readline().rstrip())
    num = list(map(int, sys.stdin.readline().split()))
    num.sort()
    print(num[n] - num[n-1])
