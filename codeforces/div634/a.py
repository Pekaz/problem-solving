import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    re = int(n/2)
    if n % 2 == 0:
        re -= 1
    print(re)
