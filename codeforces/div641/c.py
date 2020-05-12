import sys

chk = [0] * 200001
prm = []
fact = {1: [1]}
for i in range(2, 200001):
    if chk[i] == 0:
        prm.append(i)
        j = 1
        while True:
            if i * j > 200000:
                break
            if i * j not in fact:
                fact[i * j] = [i]
            else:
                fact[i * j].append(i)
            chk[i * j] = 1
            j += 1

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
chk = []
for i in a:
    for val in fact[i]:
        if val not in chk:
            chk.append(val)

result = 1
chk.sort()
for target in chk:
    i = 1
    while True:
        if target == 1:
            break
        cnt = 0
        for p in a:
            if p % (target ** i) != 0:
                cnt += 1
                if cnt > 1:
                    break
        if cnt > 1:
            break
        i += 1
    result *= target ** (i-1)
print(result)

