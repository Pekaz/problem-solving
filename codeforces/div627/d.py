import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))
chk = [0] * n

for i in range(n):
    chk[i] = a[i] - b[i]
chk.sort()
re = 0
for i in range(1, n):
    if chk[i] > 0:
        st = 0
        ed = i - 1
        while True:
            mid = int((st + ed) / 2)
            if chk[i] + chk[mid] > 0:
                ed = mid
            else:
                st = mid + 1
            if st > ed or mid == int((st + ed) / 2):
                break
        if mid < 0:
            mid = 0
        if mid > i - 1:
            mid = i - 1
        if chk[i] + chk[mid] > 0:
            re += (i - mid)
print(re)
