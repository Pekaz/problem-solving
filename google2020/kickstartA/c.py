import sys

for t in range(int(sys.stdin.readline().rstrip())):
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    prog = list(map(int, sys.stdin.readline().rstrip().split()))

    gap = 0
    for i in range(1, n):
        gap = max(gap, prog[i] - prog[i-1])
    a = 1
    b = gap
    re = 0
    while True:
        if a > b:
            break
        mid = int((a+b)/2)
        chk = prog[:]
        cnt = 0
        possible = True
        for i in range(1, n):
            cnt += int((chk[i] - chk[i-1])/mid)
            if (chk[i] - chk[i-1]) % mid == 0:
                cnt -= 1
            if cnt > k:
                possible = False
                break
        if possible:
            re = mid
            b = mid - 1
        else:
            a = mid + 1
    print('Case #{}: {}'.format(t+1, re))

