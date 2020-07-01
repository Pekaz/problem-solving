import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, r = list(map(int, sys.stdin.readline().rstrip().split()))
    j = min(n, r)
    if n <= r:
        j -= 1
    re = (j + 1) * int(j/2)
    if j % 2 == 1:
        re += int((j + 1)/2)
    if n <= r:
        re += 1
    print(re)

