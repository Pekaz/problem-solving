import sys


for _ in range(int(sys.stdin.readline().rstrip())):
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    bi = sys.stdin.readline().rstrip()
    re = 0
    last = -1
    for i in range(len(bi)):
        if bi[i] == '1' or i == len(bi) - 1:
            if bi[i] == '0' and (last < i or last < 0):
                re += 1
            j = i - (k + 1)
            while True:
                if j <= last:
                    break
                j -= (k + 1)
                re += 1
            last = i + k
    print(re)

