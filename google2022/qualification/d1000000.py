import sys

for t in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    d = list(map(int, sys.stdin.readline().rstrip().split()))
    d.sort()
    
    result = 0
    for i in range(n):
      if d[i] >= result + 1:
        result += 1
    print("Case #{}: {}".format(t + 1, result))