import sys

for t in range(int(sys.stdin.readline().rstrip())):
    n, d = list(map(int, sys.stdin.readline().rstrip().split()))
    cakes = list(map(int, sys.stdin.readline().rstrip().split()))
    cakes.sort()
    re = 0
    if d == 2:
        re = 1
        for i in range(n - 1):
            if cakes[i] == cakes[i + 1]:
                re = 0
    else:
        re = 2
        for i in range(n - 2):
            if cakes[i] == cakes[i + 1] == cakes[i + 2]:
                re = 0
                break
        if re == 2:
            for i in range(n - 2):
                if cakes[i] == cakes[i + 1] and n > 2:
                    re = 1
                    break
        if re == 2:
            for i in range(n):
                for j in range(i + 1, n):
                    if cakes[i] * 2 == cakes[j]:
                        re = 1
                        break
                if re == 1:
                    break

    print("Case #{}: {}".format(t + 1, re))


