import sys

for t in range(int(sys.stdin.readline().rstrip())):
    n, b = list(map(int, sys.stdin.readline().rstrip().split()))
    houses = list(map(int, sys.stdin.readline().rstrip().split()))
    houses.sort()
    summ = 0
    re = 0
    for i in houses:
        if summ + i > b:
            break
        summ += i
        re += 1
    print("Case #{}: {}".format(t+1, re))

