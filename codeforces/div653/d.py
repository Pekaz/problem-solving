import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    mod = []
    for i in a:
        if i % k > 0:
            mod.append(k - (i % k))
    if len(mod) == 0:
        print(0)
        continue
    mod.sort()
    i = 0
    while True:
        if i == len(mod):
            break
        st = i + 1
        ed = len(mod) - 1
        last = -1
        check = True
        while True:
            if st > ed:
                break
            mid = int((st + ed) / 2)
            if mod[mid] == mod[i]:
                check = False
                break
            elif mod[mid] > mod[i]:
                ed = mid - 1
            else:
                st = mid + 1

        if not check:
            tar = mod.pop(i) + k
            while True:
                ins = True
                st = i
                ed = len(mod) - 1
                last = -1
                while True:
                    if st > ed:
                        break
                    mid = int((st + ed) / 2)
                    if mod[mid] == tar:
                        ins = False
                        break
                    elif mod[mid] > tar:
                        ed = mid - 1
                    else:
                        st = mid + 1
                    last = mid
                if not ins:
                    tar += k
                else:
                    mod.insert(last + 1, tar)
                    break
        else:
            i += 1
    for i in range(1, len(mod)):
        if mod[i] % 2 == 0:
            prt = -1
        else:
            prt = 0
        if mod[i - 1] < int(mod[i] / 2) + prt:
            tar = mod.pop(i)
            if i == len(mod):
                mod.append(int(tar / 2) + prt)
                mod.append(int(tar / 2) + 1)
            else:
                mod.insert(i, int(tar / 2) + prt)
                mod.insert(i + 1, int(tar / 2) + 1)
    print(max(mod) + 1)
