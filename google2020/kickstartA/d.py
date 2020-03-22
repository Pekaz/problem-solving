import sys

for t in range(int(sys.stdin.readline().rstrip())):
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    words = []
    for _ in range(n):
        words.append(sys.stdin.readline().rstrip())
    words.sort()
    re = 0
    while True:
        if len(words) == 0:
            break
        tar = -1
        taridx = []
        idxs = []
        bucket = []
        for idx, i in enumerate(words):
            idxs.append(idx)
            bucket.append(i)
            if len(bucket) == k:
                pnt = 0
                for j in range(1, len(bucket[0]) + 1):
                    chk = bucket[0][:j]
                    possible = True
                    for itm in bucket:
                        if chk not in itm:
                            possible = False
                    if not possible:
                        pnt = (j - 1)
                        break
                    elif j == len(bucket[0]):
                        pnt = j
                if pnt > tar:
                    tar = pnt
                    taridx = idxs[:]
                bucket.pop(0)
                idxs.pop(0)
        re += tar
        for idx in taridx[::-1]:
            words.pop(idx)
    print('Case #{}: {}'.format(t+1, re))


