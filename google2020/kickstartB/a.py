import sys

for t in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    re = 0
    for i in range(1, n-1):
        if num[i-1] < num[i] > num[i+1]:
            re += 1
    print("Case #{}: {}".format(t + 1, re))
