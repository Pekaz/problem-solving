import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    num = list(map(int, sys.stdin.readline().rstrip().split()))
    num.sort()
    check = []
    result = True
    for i in num:
        if i == 0:
            continue
        chk = i
        re = True
        cnt = 0
        while True:
            if chk % k > 1:
                re = False
                break
            if chk % k == 1:
                if k ** cnt in check:
                    re = False
                    break
                check.append(k ** cnt)
            chk = int(chk / k)
            cnt += 1
            if chk < k:
                if chk % k > 1:
                    re = False
                    break
                if chk % k == 1:
                    if k ** cnt in check:
                        re = False
                        break
                    check.append(k ** cnt)
                break
        if not re:
            result = False
            break
    if result:
        print('YES')
    else:
        print('NO')



