import sys

prm = []
chk = [0] * (10**7+1)
for i in range(2, 10**7+1):
    if chk[i] == 0:
        j = 2
        prm.append(i)
        while True:
            if i * j > 10**7:
                break
            chk[i*j] = 1
            j += 1

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
d1 = []
d2 = []
# for i in nums:

