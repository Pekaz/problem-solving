import sys

n = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))
max_len = 0
for i in num:
    bi = bin(i)[2:]
    if max_len < len(bi):
        max_len = len(bi)

st = 0
max_len -= 1
while True:
    cnt = 0
    for idx, i in enumerate(num):
        if (2 ** max_len) & i > 0:
            cnt += 1
            if cnt > 1:
                break
            if cnt == 1:
                st = idx
    if cnt == 1:
        break
    max_len -= 1
    if max_len < 0:
        break

print(num[st], end=' ')
del num[st]
for i in num:
    print(i, end=' ')
