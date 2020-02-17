import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, m = list(map(int, sys.stdin.readline().rstrip().split()))
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    re = num[0]
    for i in range(1, len(num)):
        if int(m/i) <= num[i]:
            re += int(m/i)
            break
        re += num[i]
        m -= num[i] * i

    print(re)

