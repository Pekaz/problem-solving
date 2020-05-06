import sys

chk = [2]
i = 1
while True:
    chk.append(chk[i-1] + i * 3 + 2)
    i += 1
    if chk[i-1] > 10**9:
        break

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    re = 0
    while True:
        if n <= 1:
            break
        a = 0
        b = len(chk) - 1
        tmp = 0
        while True:
            if a > b:
                break
            mid = int((a + b)/2)
            if chk[mid] > n:
                b = mid - 1
            else:
                tmp = chk[mid]
                a = mid + 1
        n -= tmp
        re += 1
    print(re)
