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
    check = []
    mod_sum = 0
    for i in mod:
        mod_sum += i
    cnt = 0
    i = 1
    while True:
        if 0 < mod_sum - i < i:
            max_re = mod_sum - i - cnt
            if max_re < 1:
                max_re = 1
            i += max_re
            break
        mod_sum -= i
        cnt += 1
        i += 1
        if mod_sum == 0:
            break
    print(i)
