import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    a1, b1, c1 = list(map(int, sys.stdin.readline().rstrip().split()))
    a2, b2, c2 = list(map(int, sys.stdin.readline().rstrip().split()))
    re = 0
    two_cnt = min(c1, b2)
    c1 -= two_cnt
    b2 -= two_cnt
    re += two_cnt * 2
    one_cnt = min(b1, b2)
    b1 -= one_cnt
    b2 -= one_cnt
    one_cnt = min(b1, a2)
    b1 -= one_cnt
    a2 -= one_cnt
    zero_cnt = min(a1, c2)
    a1 -= zero_cnt
    c2 -= zero_cnt
    minus_cnt = min(b1, c2)
    re -= minus_cnt * 2
    print(re)
