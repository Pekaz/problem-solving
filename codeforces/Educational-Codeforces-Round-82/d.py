import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = list(map(int, sys.stdin.readline().split()))
    boxes = list(map(int, sys.stdin.readline().split()))
    boxes.sort()
    