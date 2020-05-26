import sys
import math

for _ in range(int(sys.stdin.readline().rstrip())):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().rstrip().split()))
    x = (x2 - x1)
    y = (y2 - y1)
    print(int(math.factorial(x+y)/(math.factorial(x)*math.factorial(y))) - ((x-1)*(y-1)))
