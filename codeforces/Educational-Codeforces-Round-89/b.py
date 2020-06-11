import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, x, m = list(map(int, sys.stdin.readline().rstrip().split()))
    left = x
    right = x
    for _ in range(m):
        i, j = list(map(int, sys.stdin.readline().rstrip().split()))
        if not(j < left or right < i or (left <= i and j <= right)):
            if i < left:
                left = i
            if right < j:
                right = j
    print(right-left+1)
