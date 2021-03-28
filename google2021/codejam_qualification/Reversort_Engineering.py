import sys
from itertools import permutations


for t in range(int(sys.stdin.readline().rstrip())):
    n, c = list(map(int, sys.stdin.readline().rstrip().split()))

    t_l = list(permutations([i for i in range(1, n + 1)], n))
    re_l = []
    for temp_l in t_l:
        l = list(temp_l)
        target_re = l.copy()
        re = 0
        for i in range(n - 1):
            min_n = 101
            min_x = 0
            for j in range(i, n):
                if min_n > l[j]:
                    min_n = l[j]
                    min_x = j
            sub_l = l[i:min_x + 1]
            sub_l.reverse()
            l[i:min_x + 1] = sub_l
            re += min_x - i + 1
        if re == c:
            re_l = target_re
            break
    print("Case #{}: ".format(t + 1), end='')
    if len(re_l) == 0:
        print('IMPOSSIBLE')
    else:
        for i in re_l:
            print(i, end=' ')
        print('')
