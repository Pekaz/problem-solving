import sys

for t in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    re = 0
    for i in range(n - 1):
        min_n = 101
        min_x = 0
        for j in range(i, n):
            if min_n > l[j]:
                min_n = l[j]
                min_x = j
        sub_l = l[i:min_x + 1]
        sub_l.reverse()
        l[i:min_x + 1] = sub_l
        re += min_x - i + 1
    print("Case #{}: {}".format(t + 1, re))
