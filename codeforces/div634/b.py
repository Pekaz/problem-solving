import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    re = ''
    i = 0
    while True:
        re += chr(ord('a') + i)
        i = (i+1) % b
        if len(re) == n:
            break
    print(re)
